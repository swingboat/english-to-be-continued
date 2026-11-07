import { Browser, sleep } from '../../../../.agents/skills/taste-skill/scripts/lib/cdp.mjs';
import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync, unlinkSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
const root=resolve('.'), here=join(root,'production/book-01/ep-003'), out=join(here,'checks');
const data=JSON.parse(readFileSync(join(here,'episode.json'),'utf8'));
const before=JSON.parse(readFileSync(join(out,'before-current-rules.json'),'utf8'));
const cast=JSON.parse(readFileSync(join(root,'voices/book-01/cast.json'),'utf8'));
const publishing=JSON.parse(readFileSync(join(here,'publishing/publishing.json'),'utf8'));
const source=readFileSync(join(root,'episodes/book-01/ep-003.html'),'utf8');
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const report={};
// Story and teaching content must survive this rules update exactly.
for(const key of ['words','review_words','supplemental_review_words','continuity','art']) assert.deepEqual(data[key],before.episode[key]);
for(let i=0;i<data.scenes.length;i++){
 const old=before.episode.scenes[i], scene=data.scenes[i];
 for(const key of ['id','panel','name','place','shot','action','sound']) assert.deepEqual(scene[key],old[key]);
 assert.deepEqual(scene.cues.map(({voices,...cue})=>cue),old.cues);
 assert.deepEqual(scene.narration.map(({kind,voice,quoted_character,...n})=>n),old.narration);
}
for(const [name,sha] of Object.entries(before.other_episodes)) assert.equal(hash(readFileSync(join(root,'episodes/book-01',name))),sha);
report.other_episodes_unchanged=Object.keys(before.other_episodes).length;
const refs=[...source.matchAll(/<audio\b[^>]*src="data:audio\/wav;base64,([^"]+)"/g)];
assert.equal(refs.length,3);
report.embedded_voices=data.voice_cast.map((member,i)=>{
 const v=cast.voices.find(v=>v.name===member.name), bytes=readFileSync(join(root,'voices/book-01',v.selection.reference_audio));
 assert.equal(hash(Buffer.from(refs[i][1],'base64')),hash(bytes));
 assert.equal(hash(bytes),v.selection.reference_audio_sha256);
 assert(source.includes(readFileSync(join(root,'voices/book-01',v.selection.reference_text),'utf8').trim().replaceAll('&','&amp;').replaceAll("'",'&#x27;')));
 return {name:member.name,sha256:hash(bytes),status:v.selection.provisional?'暂定采用':'已选定'};
});
const storyboard=source.match(/\.panel-raster\{background-image:url\("data:image\/png;base64,([^\"]+)"\)/);
assert(storyboard);assert.equal(hash(Buffer.from(storyboard[1],'base64')),hash(readFileSync(join(here,'storyboard.png'))));
assert(!/<video\b/i.test(source)); assert(!/\b(?:src|href)="https?:/i.test(source));
const browser=await Browser.launch();
try{
 const page=await browser.newPage({width:1440,height:900});
 await page.send('Network.enable');
 await page.send('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:0,uploadThroughput:0});
 await page.goto('file://'+join(root,'episodes/book-01/ep-003.html'));
 const content=await page.eval(()=>({
  scenes:document.querySelectorAll('.scene').length,
  captions:[...document.querySelectorAll('.subtitle-item')].map(el=>({id:el.id.replace('subtitle-',''),en:el.querySelector('.voice-en').textContent,zh:el.querySelector('.caption-zh').textContent})),
  audio:[...document.querySelectorAll('audio')].map(a=>({autoplay:a.autoplay,paused:a.paused,controls:a.controls})),
  status:[...document.querySelectorAll('.voice-status')].map(el=>el.textContent),
  keywords:[...document.querySelectorAll('.publish-keyword')].map(el=>el.textContent.replace(/，$/,'')),
  missingLinks:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash),
  headings:[...document.querySelectorAll('h1')].map(h=>h.textContent),
  images:[...document.querySelectorAll('.publish-cover img')].map(i=>({width:i.naturalWidth,height:i.naturalHeight})),
  casts:[...document.querySelectorAll('.cast-card')].map(el=>({name:el.querySelector('h3').textContent,text:el.textContent}))
 }));
 assert.equal(content.scenes,8);assert.equal(content.headings.length,1);
 assert.deepEqual(content.captions,data.scenes.flatMap(s=>s.narration.map(({id,en,zh})=>({id,en,zh}))));
 assert.equal(content.captions.length,22);assert.deepEqual(content.missingLinks,[]);
 assert.equal(content.keywords.length,30);assert.equal(new Set(content.keywords).size,30);assert.deepEqual(content.keywords,publishing.keywords);
 assert.deepEqual(content.status,['已选定','已选定','暂定采用']);
 assert(content.audio.every(a=>!a.autoplay && a.paused && a.controls));
 for(const member of content.casts){
  for(const label of ['性别 / 年龄感','性格','音色特征','本集用途','参考语音','对应文本','英文试听文本']) assert(member.text.includes(label));
 }
 report.content={scenes:8,caption_pairs:22,dialogue_entries:31,words:5,unique_keywords:30,missing_links:0};
 report.audio_playback=[];
 for(let i=0;i<3;i++){
  const played=await page.eval(async index=>{
   const players=[...document.querySelectorAll('audio')], a=players[index];
   await a.play(); await new Promise(r=>setTimeout(r,350));
   const result={currentTime:a.currentTime,duration:a.duration,error:a.error?.code??null,otherPaused:players.every(p=>p===a||p.paused)};
   return result;
  },i);
  assert(played.currentTime>0 && played.duration>0 && played.error===null && played.otherPaused);
  report.audio_playback.push(played);
 }
 await page.eval(()=>document.querySelectorAll('audio').forEach(a=>a.pause()));
 const downloads=join(out,'offline-downloads');mkdirSync(downloads,{recursive:true});
 await browser.send('Browser.setDownloadBehavior',{behavior:'allow',downloadPath:downloads,eventsEnabled:true});
 await page.eval(()=>document.querySelectorAll('.cover-download').forEach(a=>a.click()));
 for(let tries=0;tries<40 && publishing.covers.some(c=>!existsSync(join(downloads,c.download_name)));tries++)await sleep(150);
 report.cover_downloads=publishing.covers.map(c=>{
  const path=join(downloads,c.download_name);assert(existsSync(path));
  assert.equal(hash(readFileSync(path)),hash(readFileSync(join(here,'publishing',c.file))));
  const r={filename:c.download_name,ratio:c.id,sha256:hash(readFileSync(path))};unlinkSync(path);return r;
 });
 // Open native disclosures through keyboard activation and inspect the real file page.
 await page.eval(()=>{document.documentElement.style.scrollBehavior='auto';});
 await page.send('Page.bringToFront');
 await page.send('Emulation.setFocusEmulationEnabled',{enabled:true});
 const summary=await page.eval(()=>{const s=document.querySelector('#scene-7 .dialogue-reference summary');s.scrollIntoView();s.focus();return s.textContent;});
 await page.send('Input.dispatchKeyEvent',{type:'keyDown',key:'Enter',code:'Enter',text:'\r',unmodifiedText:'\r',windowsVirtualKeyCode:13});
 await page.send('Input.dispatchKeyEvent',{type:'keyUp',key:'Enter',code:'Enter',windowsVirtualKeyCode:13});
 assert(await page.eval(()=>document.querySelector('#scene-7 .dialogue-reference').open));
 await page.eval(()=>{document.querySelector('#scene-7').scrollIntoView();});await sleep(950);
 await page.screenshot({path:join(out,'desktop-scene-7-current-rules.jpg')});
 for(const w of [1440,768,390,375]){
  await page.setViewport({width:w,height:w<700?844:900});
  const dims=await page.eval(()=>({viewport:innerWidth,scroll:document.documentElement.scrollWidth}));assert(dims.scroll<=dims.viewport);
  await page.eval(()=>document.querySelector('#cast').scrollIntoView());await sleep(950);
  await page.screenshot({path:join(out,`cast-${w}.jpg`)});
  await page.eval(()=>{const el=document.querySelector('.voice-files');el.open=true;el.scrollIntoView();});await sleep(100);
  if(w===390)await page.screenshot({path:join(out,'mobile-voice-transcript.jpg')});
 }
 await page.setViewport({width:390,height:844});
 await page.eval(()=>document.querySelector('#word-in-person').scrollIntoView());await sleep(950);await page.screenshot({path:join(out,'mobile-vocabulary-current-rules.jpg')});
 const reduced=await browser.newPage({width:390,height:844,reducedMotion:true});
 await reduced.goto('file://'+join(root,'episodes/book-01/ep-003.html'));
 assert.equal(await reduced.eval(()=>document.getAnimations().length),0);
 await reduced.close();
 const plain=await browser.newPage({width:390,height:844});
 await plain.send('Emulation.setScriptExecutionDisabled',{value:true});
 await plain.goto('file://'+join(root,'episodes/book-01/ep-003.html'));
 const fallback=await plain.eval(()=>({captionCount:document.querySelectorAll('.subtitle-item').length,opacity:getComputedStyle(document.querySelector('.scene-picture')).opacity,audio:document.querySelectorAll('audio[controls]').length}));
 assert.equal(fallback.captionCount,22);assert.equal(fallback.opacity,'1');assert.equal(fallback.audio,3);
 report.no_script=fallback;report.reduced_motion='no active animation';report.offline_file_url=true;
 report.console_errors=page.consoleErrors;assert.equal(page.consoleErrors.length,0);
 await page.close();await plain.close();
}finally{await browser.close();}
report.html_sha256=hash(Buffer.from(source));
writeFileSync(join(out,'current-rules-verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
