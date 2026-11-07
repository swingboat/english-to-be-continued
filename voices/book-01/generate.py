#!/usr/bin/env python3
"""Generate named character auditions with the existing local Qwen3-TTS engine."""

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent
DEFAULT_ENGINE = Path('/Users/huyin/Swingboat/audio-research/experiments/tts/qwen3-tts')


def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine-root', type=Path, default=DEFAULT_ENGINE)
    parser.add_argument('--only', nargs='+', help='Exact Chinese character names from cast.json')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    config = json.loads((ROOT / 'cast.json').read_text(encoding='utf-8'))
    voices = config['voices']
    if len({v['name'] for v in voices}) != len(voices):
        parser.error('Duplicate character names in cast.json')
    if args.only:
        unknown = set(args.only) - {v['name'] for v in voices}
        if unknown:
            parser.error(f'Unknown characters: {sorted(unknown)}')
        voices = [v for v in voices if v['name'] in args.only]
    for voice in voices:
        name = voice['name']
        if name in ('.', '..') or any(c in name for c in '/\\\0'):
            parser.error(f'Invalid character name: {name!r}')
    model_path = (
        args.engine_root.resolve() / 'cache/huggingface/hub'
        / ('models--' + config['model'].replace('/', '--'))
        / 'snapshots' / config['revision']
    )
    if not (model_path / 'config.json').is_file():
        parser.error(f'Cached model not found: {model_path}')
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        parser.error('ffmpeg and ffprobe are required')
    for voice in voices:
        output = ROOT / 'characters' / voice['name']
        if not args.dry_run and output.exists() and any(output.iterdir()):
            parser.error(f'Character audio already exists: {output}')
        print(f"{voice['name']} ({voice['gender']}, {voice['age']}) -> {output / (voice['name'] + '.wav')}", flush=True)
    if args.dry_run:
        return

    # Reuse the installed environment and model cache, with no model download.
    os.environ['HF_HUB_OFFLINE'] = '1'
    os.environ['HF_HUB_DISABLE_XET'] = '1'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    import mlx.core as mx
    import numpy as np
    from mlx_audio.audio_io import write
    from mlx_audio.tts.utils import load_model

    environment = {
        'python': sys.version.split()[0],
        'executable': sys.executable,
        'platform': platform.platform(),
        'machine': platform.machine(),
        'hardware': subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'], text=True).strip(),
        'packages': {p: importlib.metadata.version(p) for p in ('mlx-audio', 'mlx', 'numpy')},
        'ffmpeg': subprocess.check_output(['ffmpeg', '-version'], text=True).splitlines()[0],
    }
    print('Loading cached VoiceDesign model...', flush=True)
    model = load_model(str(model_path))
    for voice in voices:
        name = voice['name']
        output = ROOT / 'characters' / name
        output.mkdir(parents=True, exist_ok=True)
        text = voice['text'].strip()
        instruction = voice['instruct'] + ' ' + config['common_direction']
        (output / f'{name}.txt').write_text(text + '\n', encoding='utf-8')
        (output / '音色描述.txt').write_text(instruction + '\n', encoding='utf-8')
        mx.random.seed(voice['seed'])
        print(f'Generating {name}...', flush=True)
        started = time.perf_counter()
        chunks = []
        sample_rate = None
        for result in model.generate_voice_design(
            text=text, instruct=instruction, language=config['language'],
            **config['generation'], verbose=False,
        ):
            chunks.append(result.audio)
            if sample_rate is not None and sample_rate != result.sample_rate:
                raise RuntimeError(f'Inconsistent sample rate for {name}')
            sample_rate = result.sample_rate
        if not chunks:
            raise RuntimeError(f'No audio generated for {name}')
        audio = np.asarray(mx.concatenate(chunks)).reshape(-1)
        elapsed = time.perf_counter() - started
        if not audio.size or not np.isfinite(audio).all():
            raise RuntimeError(f'Empty or nonfinite audio for {name}')
        peak = float(np.max(np.abs(audio)))
        rms = float(np.sqrt(np.mean(audio.astype(np.float64) ** 2)))
        if peak <= 0 or peak >= 1.0 or rms <= 0:
            raise RuntimeError(f'Silent or overloaded waveform for {name}: {peak=}, {rms=}')
        seconds = audio.size / sample_rate
        if not 3 <= seconds < config['generation']['max_tokens'] / 12 - 1:
            raise RuntimeError(f'Unexpected duration or possible token limit for {name}: {seconds}')
        wav = output / f'{name}.wav'
        mp3 = output / f'{name}.mp3'
        write(wav, audio, sample_rate)
        subprocess.run(['ffmpeg', '-v', 'error', '-n', '-i', str(wav), '-codec:a', 'libmp3lame', '-b:a', '128k', str(mp3)], check=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-xerror', '-i', str(mp3), '-f', 'null', '-'], check=True)
        probe = json.loads(subprocess.check_output([
            'ffprobe', '-v', 'error', '-show_entries', 'stream=sample_rate,channels:format=duration',
            '-of', 'json', str(mp3),
        ], text=True))
        stream = probe['streams'][0]
        if int(stream['sample_rate']) != sample_rate or stream['channels'] != 1:
            raise RuntimeError(f'Unexpected MP3 audio properties for {name}')
        record = {
            'name': name,
            'created_at': datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),
            'status': 'generated-awaiting-listening-review',
            'character': voice,
            'model': config['model'],
            'revision': config['revision'],
            'model_path': str(model_path),
            'generation': config['generation'],
            'language': config['language'],
            'full_instruction': instruction,
            'environment': environment,
            'sample_rate': sample_rate,
            'channels': 1,
            'samples': int(audio.size),
            'duration_seconds': round(seconds, 3),
            'generation_seconds': round(elapsed, 3),
            'peak': peak,
            'rms': rms,
            'mp3_duration_seconds': float(probe['format']['duration']),
            'checks': {'finite_waveform': True, 'peak_below_full_scale': True, 'mp3_full_decode': True},
            'listening_review': {'gender': 'pending', 'age': 'pending', 'personality': 'pending', 'pronunciation_and_completeness': 'pending'},
            'identity_note': 'VoiceDesign candidate only; the seed is not a persistent speaker identity. Shared voice_identity does not guarantee matching timbre.',
            'files': {p.name: {'bytes': p.stat().st_size, 'sha256': digest(p)} for p in (wav, mp3, output / f'{name}.txt', output / '音色描述.txt')},
        }
        save_json(output / '生成记录.json', record)
        print(f'DONE {name}: {seconds:.2f}s audio, {elapsed:.2f}s generation, peak {peak:.3f}', flush=True)
        del chunks, audio
        mx.clear_cache()
    print(f'Completed {len(voices)} named character auditions.', flush=True)


if __name__ == '__main__':
    main()
