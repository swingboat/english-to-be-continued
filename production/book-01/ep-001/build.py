#!/usr/bin/env python3
"""Build episode 001: offline animation study, complete script, art, words and cast."""
import base64
import hashlib
import html
import json
import re
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE.parent))
from publishing import publishing_replacements

data = json.loads((HERE / 'episode.json').read_text())
voice_settings = json.loads((HERE / 'voice-settings.json').read_text())
voice_root = ROOT / 'voices/book-01'
voices = {v['name']: v for v in json.loads((voice_root / 'cast.json').read_text())['voices']}
image = (HERE / 'storyboard.png').read_bytes()
width, height = struct.unpack('>II', image[16:24])

def esc(value):
    return html.escape(str(value), quote=True)

def uri(path, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode(Path(path).read_bytes()).decode()

def mark(value):
    return re.sub(r'\b(confidence|volunteer|goal|challenge|schedule)\b', lambda m: f'<a class="keyword" href="#word-{m[0].lower()}">{m[0]}</a>', esc(value), flags=re.I)

def art(panel, label):
    x, y, w, h = data['art']['panels'][panel]
    style = f'aspect-ratio:{w}/{h};background-size:{width/w*100:.8f}% {height/h*100:.8f}%;background-position:{x/(width-w)*100:.8f}% {y/(height-h)*100:.8f}%'
    return f'<div class="panel-raster" role="img" aria-label="{esc(label)}" style="{style}"></div>'

cast_cards = []
for index, member in enumerate(voice_settings['cast'], 1):
    voice = voices[member['name']]
    selection = voice['selection']
    status = ('暂定采用' if selection.get('provisional') else '已选定') if selection.get('status') == 'selected' else '待确认'
    audio_path = voice_root / selection['reference_audio']
    text_path = voice_root / selection['reference_text']
    assert audio_path.is_file() and text_path.is_file()
    assert hashlib.sha256(audio_path.read_bytes()).hexdigest() == selection['reference_audio_sha256']
    feedback = voice_root / selection['review']
    assert json.loads(feedback.read_text()), f'Missing audition record: {feedback}'
    rows = [('性别 / 年龄感', f"{voice['gender']} · {voice['age']} 岁左右"), ('性格', voice['personality']), ('音色特征', voice['direction_zh']), ('本集用途', member['usage'])]
    profile = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in rows)
    files = ''.join(f'<div><dt>{label}</dt><dd><strong>{esc(path.name)}</strong><code>{esc(path.relative_to(ROOT).as_posix())}</code></dd></div>' for label, path in [('参考语音', audio_path), ('对应文本', text_path)])
    cast_cards.append(f'<article class="cast-card" id="cast-{index}" aria-labelledby="cast-name-{index}"><div class="cast-listen"><h3 id="cast-name-{index}">{esc(voice["name"])}</h3><p class="voice-status">{status}</p><audio controls preload="none" aria-label="播放{esc(voice["name"])}的参考语音" src="{uri(audio_path,"audio/wav")}">请使用支持音频的浏览器。</audio><p class="cast-note">人物音色参考 · 英文试听</p></div><div class="cast-profile"><dl class="cast-details">{profile}</dl><dl class="cast-details reference-paths">{files}</dl><details class="voice-files"><summary>对应英文试听文本</summary><blockquote lang="en">{esc(text_path.read_text().strip())}</blockquote></details></div></article>')

contents, scripts = [], []
for scene in data['scenes']:
    n = scene['id']
    contents.append(f'<a href="#scene-{n}" class="scene-link">{esc(scene["name"])}</a>')
    lines = []
    for cue in scene['cues']:
        if cue.get('quiz'):
            continue
        text = f'<span class="dialogue-en" lang="en">{mark(cue["en"])}</span><span class="dialogue-zh">{esc(cue["zh"])}</span>' if 'en' in cue else esc(cue['text'])
        lines.append(f'<li><span class="speaker">{esc(cue["who"])}</span><span class="dialogue-text">{text}</span></li>')
    captions = ''.join(f'<li class="subtitle-item" id="subtitle-{esc(line["id"])}"><span class="caption-index">{esc(line["id"])}</span><div class="caption-text"><p class="voice-en" lang="en">{mark(line["en"])}</p><p class="caption-zh" lang="zh-CN">{esc(line["zh"])}</p></div></li>' for line in scene['narration'])
    direction = voice_settings['scenes'][str(n)]
    narration = f'<section class="narration-block" aria-label="本格英文解说及中英字幕"><h4>英文解说与双语字幕</h4><p class="narration-direction"><strong>小帅 · 英文解说语气</strong>{esc(direction["narration"])}</p><ol class="subtitle-list">{captions}</ol></section>'
    invitations = ''
    if n == 6:
        rows = ''.join(f'<tr><th scope="row">{esc(i["name"])}</th><td>{esc(i["from"])}</td><td>{esc(i["time"])}</td><td>{esc(i["status"])}</td></tr>' for i in data['invitations'])
        invitations = '<div class="table-wrap"><table><caption>夹板上的三项待确认邀请</caption><thead><tr><th scope="col">活动</th><th scope="col">邀请方</th><th scope="col">时间</th><th scope="col">状态</th></tr></thead><tbody>' + rows + '</tbody></table></div>'
    scripts.append(f'<li><article class="scene" id="scene-{n}" aria-labelledby="scene-title-{n}"><div class="scene-heading"><h3 id="scene-title-{n}">{esc(scene["name"])}</h3><p class="scene-place">{esc(scene["place"])}</p></div><div class="scene-body"><figure class="scene-picture">{art(scene["panel"],scene["shot"])}<figcaption>分镜 {n} · {esc(scene["name"])}</figcaption></figure><div class="scene-script"><p class="action"><strong>动作</strong>{esc(scene["action"])}</p>{narration}<details class="dialogue-reference"><summary>角色对白参考与语气</summary><p class="dialogue-note">角色对白与英文解说分别录制；解说中的引语仍由小帅转述。</p><p class="narration-direction">{esc(direction["roles"])}</p><ol class="dialogue">{"".join(lines)}</ol></details>{invitations}<details class="direction"><summary>分镜与音效说明</summary><p>{esc(scene["shot"])}</p><p><strong>音效：</strong>{esc(scene["sound"])}</p></details></div></div></article></li>')

cards = []
for i, w in enumerate(data['words'], 1):
    cards.append(f'<article class="word-card" id="word-{esc(w["word"])}" aria-labelledby="word-title-{i}"><div class="word-definition"><h3 id="word-title-{i}" lang="en">{esc(w["word"])}</h3><p class="meaning"><span>{esc(w["part"])}</span>{esc(w["meaning"])}</p><a class="scene-reference" href="#scene-{w["scene"]}">回到故事第 {w["scene"]} 格</a></div><div class="word-example"><blockquote lang="en">{esc(w["expression"])}</blockquote><p class="example-zh">{esc(w["translation"])}</p><p class="story-question">想一想：{esc(w["question"])}</p><p class="word-source">{esc(w["source"])}</p></div></article>')

timeline = json.loads((HERE / 'animation/timeline.json').read_text())
by_id = {line['id']: line for scene in data['scenes'] for line in scene['narration']}
for cue in timeline['cues']:
    cue.update({k: by_id[cue['source']][k] for k in ('en', 'zh')})
timeline['assets'] = {key: uri(HERE / 'animation' / value, 'image/png') for key, value in timeline['assets'].items()}
assert timeline['duration'] == 16 and len(timeline['cues']) == 4
assert all(a['until'] == b['at'] for a, b in zip(timeline['cues'], timeline['cues'][1:]))

replacements = {
    'SHEET_URI': 'data:image/png;base64,' + base64.b64encode(image).decode(),
    'ANIMATION_POSTER': art(3, '教室中的分身举手自荐，班主任在旁边。'),
    'CONTENTS': ''.join(contents), 'SCRIPT_SCENES': ''.join(scripts), 'WORD_CARDS': ''.join(cards),
    'WORD_LINKS': ''.join(f'<a href="#word-{esc(w["word"])}" lang="en">{esc(w["word"])}</a>' for w in data['words']),
    'CAST_CARDS': ''.join(cast_cards),
    'CONTINUITY_END': ''.join(f'<li>{esc(x)}</li>' for x in data['continuity']['end']),
    'CONTINUITY_PROPS': ''.join(f'<li>{esc(x)}</li>' for x in data['continuity']['props']),
    'ANIMATION_DATA': json.dumps(timeline, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'),
    'FONT_CSS': '\n'.join('@font-face{font-family:"Schibsted Grotesk";font-style:normal;font-weight:'+str(weight)+';font-display:swap;src:url('+uri(HERE / f'assets/schibsted-grotesk-{weight}.ttf','font/ttf')+') format("truetype");}' for weight in (400, 600, 800)),
    'PAGE_CSS': (HERE / 'page.css').read_text(),
    'ANIMATION_CSS': (HERE / 'animation/player.css').read_text(),
    'PAGE_JS': (HERE / 'animation/scene.js').read_text() + '\n' + (HERE / 'animation/player.js').read_text(),
}
replacements.update(publishing_replacements(HERE))
section = re.sub(r'<p class="kicker">.*?</p>', '', replacements['PUBLISHING_SECTION'])
replacements['PUBLISHING_SECTION'] = section.replace('</span>，<span class="publish-keyword">', '，</span><span class="publish-keyword">')
template = (HERE / 'page.template').read_text()
for key, value in replacements.items():
    template = template.replace('@@' + key + '@@', value)
assert not re.search(r'@@[A-Z_]+@@', template)
assert len(data['scenes']) == 8 and sum(len(s['narration']) for s in data['scenes']) == 23
assert template.count('<audio ') == 4 and not re.search(r'<video\b', template, flags=re.I)
assert all(w['meaning'] and w['expression'] and w['translation'] for w in data['words'])
out = ROOT / 'episodes/book-01/ep-001.html'
out.write_text(template)
print(json.dumps({'output': str(out), 'bytes': out.stat().st_size, 'animation_seconds': timeline['duration'], 'scenes': 8, 'subtitle_pairs': 23, 'words': len(cards), 'cast': 4, 'offline': True, 'video_exported': False}, ensure_ascii=False))
