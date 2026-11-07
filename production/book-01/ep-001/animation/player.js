(() => {
  'use strict';
  const audioPlayers = [...document.querySelectorAll('audio')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  if ('IntersectionObserver' in window && !reduce.matches) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) {
        entry.target.classList.add('entering');
        observer.unobserve(entry.target);
      }
    }, {threshold: .06});
    document.querySelectorAll('.section-head h2,.section-head>p,.scene-heading,.scene-picture,.word-definition,.cast-listen,.publish-cover-heading').forEach(el => observer.observe(el));
    reduce.addEventListener('change', () => { if (reduce.matches) observer.disconnect(); });
  }

  const data = JSON.parse(document.querySelector('#animation-data').textContent);
  const root = document.querySelector('.cinema');
  const player = document.querySelector('.animation-player');
  const canvas = document.querySelector('#animation-canvas');
  const ctx = canvas.getContext('2d', {alpha: false});
  const playButton = document.querySelector('#animation-play');
  const heroButton = document.querySelector('.cinema-play');
  const stageButton = document.querySelector('.stage-play');
  const restartButton = document.querySelector('#animation-restart');
  const soundButton = document.querySelector('#animation-sound');
  const fullButton = document.querySelector('#animation-fullscreen');
  const progress = document.querySelector('#animation-progress');
  const clock = document.querySelector('#animation-clock');
  const en = document.querySelector('#animation-en');
  const zh = document.querySelector('#animation-zh');
  const word = document.querySelector('#stage-word');
  const status = document.querySelector('#animation-status');
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  let time = 0, playing = false, ready = false, started = false, lastFrame = 0, raf = 0;
  let sound = true, audioContext, master;
  const sounding = new Set();
  const images = {};
  let sceneRenderer;

  const loadImage = (key, src) => new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => { images[key] = img; resolve(); };
    img.onerror = () => reject(new Error('无法读取内嵌的动画素材'));
    img.src = src;
  });

  // All effects are synthesized locally. No speech synthesis, remote audio or audition dialogue.
  function ensureAudio() {
    if (!sound) return;
    const Audio = window.AudioContext || window.webkitAudioContext;
    if (!Audio) {
      sound = false;
      soundButton.disabled = true;
      soundButton.textContent = '音效不可用';
      soundButton.setAttribute('aria-pressed', 'false');
      return;
    }
    if (!audioContext) {
      audioContext = new Audio();
      master = audioContext.createGain();
      master.gain.value = .38;
      master.connect(audioContext.destination);
    }
    audioContext.resume().catch(() => {});
  }
  function note(frequency, duration = .3, delay = 0, volume = .13, type = 'sine', target) {
    if (!sound || !audioContext || audioContext.state !== 'running') return;
    const oscillator = audioContext.createOscillator();
    const gain = audioContext.createGain();
    const at = audioContext.currentTime + delay;
    oscillator.type = type;
    oscillator.frequency.setValueAtTime(frequency, at);
    if (target) oscillator.frequency.exponentialRampToValueAtTime(target, at + duration);
    gain.gain.setValueAtTime(.001, at);
    gain.gain.exponentialRampToValueAtTime(volume, at + .012);
    gain.gain.exponentialRampToValueAtTime(.001, at + duration);
    oscillator.connect(gain); gain.connect(master);
    oscillator.onended = () => { sounding.delete(oscillator); oscillator.disconnect(); gain.disconnect(); };
    sounding.add(oscillator);
    oscillator.start(at); oscillator.stop(at + duration + .03);
  }
  function quiet() {
    for (const oscillator of sounding) { try { oscillator.stop(); } catch {} }
    sounding.clear();
  }
  const effects = [
    {at: 3.9, run: () => note(320, .28, 0, .07, 'triangle', 700)},
    {at: 5.7, run: () => { note(523, .22, 0, .08); note(784, .3, .12, .06); }},
    {at: 12.1, run: () => note(220, .3, 0, .08, 'triangle', 140)}
  ];
  const melody = [261.63, 329.63, 392, 329.63, 293.66, 349.23, 440, 349.23];
  function audioBetween(from, to) {
    if (!sound || to - from > .4) return;
    for (const effect of effects) if (effect.at >= from && effect.at < to) effect.run();
    const first = Math.ceil(from / .8), last = Math.floor(to / .8);
    for (let beat = first; beat <= last; beat++) {
      const at = beat * .8;
      const volume=.026 * Math.max(0,Math.min(1,(data.duration-at)/1.5));
      note(melody[beat % melody.length], .32, 0, Math.max(.002,volume), 'sine');
    }
  }
  function draw(t) {
    if (ready && sceneRenderer) sceneRenderer.render(t);
  }
  let currentCue = '';
  function captions(t) {
    const cue = data.cues.find(c => t >= c.at && t < c.until) || data.cues[data.cues.length-1];
    if (cue.source !== currentCue) {
      en.textContent=cue.en; zh.textContent=cue.zh; currentCue=cue.source;
      canvas.setAttribute('aria-label',cue.shot);
    }
    const volunteer=t>=4.6 && t<8;
    const goal=t>=8.3 && t<11.7;
    word.classList.toggle('is-visible',volunteer || goal);
    word.children[0].textContent=volunteer?'volunteer':'goal';
    word.children[1].textContent=volunteer?'自愿做；主动报名':'目标';
  }
  const formatTime = seconds => `${Math.floor(seconds/60)}:${String(Math.floor(seconds)%60).padStart(2,'0')}`;
  function updateUI() {
    const seconds = Math.min(data.duration, Math.floor(time));
    progress.value = String(time);
    progress.setAttribute('aria-valuetext', `${time.toFixed(1)} 秒，共 ${data.duration} 秒`);
    clock.textContent = `${formatTime(seconds)} / ${formatTime(data.duration)}`;
    playButton.textContent = playing ? '暂停' : time >= data.duration ? '重播' : '播放';
    playButton.setAttribute('aria-label', playing ? '暂停动画' : time >= data.duration ? '重新播放动画' : '播放动画');
    heroButton.textContent = playing ? '暂停动画' : time >= data.duration ? '重播动画' : started ? '继续播放' : '播放动画';
    root.classList.toggle('has-started', started);
  }
  function frame(now) {
    if (!playing) return;
    const previous = time;
    time = Math.min(data.duration, time + Math.min(.05, (now - lastFrame) / 1000));
    lastFrame = now;
    draw(time); captions(time); updateUI(); audioBetween(previous, time);
    if (time >= data.duration) { pause(); status.textContent = '试演结束。可以重播，或向下阅读完整剧本与五个学习单词。'; }
    else raf = requestAnimationFrame(frame);
  }
  function play() {
    if (!ready || playing) return;
    if (time >= data.duration) time = 0;
    started = true; playing = true;
    audioPlayers.forEach(a => a.pause());
    ensureAudio();
    status.textContent = reduce.matches ? '已减少次要摆动，保留举手动作与双语字幕。' : '连续动作试演：老师提问，分身举手，门外小帅探头。当前含音效与字幕，正式英文解说待配音。';
    lastFrame = performance.now(); updateUI();
    draw(time); captions(time);
    raf = requestAnimationFrame(frame);
  }
  function pause() {
    playing = false; cancelAnimationFrame(raf); quiet(); updateUI();
    if (started && time < data.duration) status.textContent = '已暂停。可继续播放、拖动进度，或选择一个剧情瞬间。';
  }
  function seek(value) {
    if (!ready) return;
    time = clamp(Number(value) || 0, 0, data.duration);
    started = true;
    if (time === data.duration) pause();
    lastFrame = performance.now(); quiet();
    draw(time); captions(time); updateUI();
  }
  for (const button of [playButton, heroButton, stageButton]) button.addEventListener('click', () => playing ? pause() : play());
  restartButton.addEventListener('click', () => { seek(0); play(); });
  progress.addEventListener('input', () => seek(progress.value));
  document.querySelectorAll('[data-seek]').forEach(button => button.addEventListener('click', () => { seek(button.dataset.seek); }));
  soundButton.addEventListener('click', () => {
    sound = !sound; soundButton.textContent = sound ? '音效：开' : '音效：关';
    soundButton.setAttribute('aria-pressed', String(sound));
    if (sound) ensureAudio(); else quiet();
  });
  if (!player.requestFullscreen) fullButton.hidden = true;
  fullButton.addEventListener('click', async () => {
    try { if (document.fullscreenElement) await document.exitFullscreen(); else await player.requestFullscreen(); }
    catch { status.textContent = '当前浏览器不支持全屏，可在页面内继续观看。'; }
  });
  document.addEventListener('fullscreenchange', () => { fullButton.textContent = document.fullscreenElement ? '退出全屏' : '全屏'; });
  document.addEventListener('visibilitychange', () => { if (document.hidden && playing) pause(); });
  window.addEventListener('pagehide', pause);
  for (const audio of audioPlayers) audio.addEventListener('play', () => {
    pause();
    for (const other of audioPlayers) if (other !== audio) other.pause();
  });
  reduce.addEventListener('change', () => { if (ready) draw(time); });
  window.episodeAnimation = Object.freeze({play, pause, seek, get state() { return {ready, playing, time, duration: data.duration, sound, reducedMotion: reduce.matches}; }});
  Promise.all(Object.entries(data.assets).map(([key, src]) => loadImage(key, src))).then(() => {
    if (!ctx) throw new Error('当前浏览器不支持 Canvas 动画');
    sceneRenderer=createEpisodeScene(ctx,images,reduce);
    ready=true;
    progress.max=String(data.duration);
    root.classList.add('animation-ready');
    [playButton, heroButton, stageButton, restartButton, progress].forEach(el => { el.disabled = false; });
    draw(0); captions(0); updateUI();
  }).catch(error => {
    status.textContent = `${error.message}。可继续阅读下方完整剧本、漫画与单词。`;
    heroButton.textContent = '画面暂不可用';
  });
})();
