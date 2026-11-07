import assert from 'node:assert/strict';
import {mkdirSync,writeFileSync} from 'node:fs';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {resolve} from 'node:path';
import {Browser,sleep} from '../../../../.agents/skills/taste-skill/scripts/lib/cdp.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const out=resolve(root,'production/book-01/ep-001/checks/continuous');mkdirSync(out,{recursive:true});
const browser=await Browser.launch();
const report={checks:[],screenshots:[],requests:[],errors:[]};
const check=(name,value)=>{assert(value,name);report.checks.push(name);};
async function shot(page,name){await sleep(220);await page.screenshot({path:resolve(out,name),quality:90});report.screenshots.push(name);}
async function click(page,selector){
 const p=await page.eval(s=>{const e=document.querySelector(s);e.scrollIntoView({behavior:'instant',block:'center'});const r=e.getBoundingClientRect();return{x:r.x+r.width/2,y:r.y+r.height/2};},selector);
 await page.send('Input.dispatchMouseEvent',{type:'mousePressed',button:'left',clickCount:1,...p});
 await page.send('Input.dispatchMouseEvent',{type:'mouseReleased',button:'left',clickCount:1,...p});
}
try{
 const page=await browser.newPage({width:1440,height:1000});await page.send('Network.enable');
 browser.on(page.sessionId,'Network.requestWillBeSent',e=>{if(/^https?:/.test(e.request.url))report.requests.push(e.request.url);});
 await page.goto(pathToFileURL(resolve(root,'episodes/book-01/ep-001.html')).href,{settleMs:1200});
 check('offline assets ready, no autoplay',await page.eval('episodeAnimation.state.ready && !episodeAnimation.state.playing && [...document.querySelectorAll("audio")].every(a=>a.paused)'));
 check('8 scenes, 23 bilingual pairs, 5 words, 4 cast references',await page.eval('document.querySelectorAll("article.scene").length===8 && document.querySelectorAll(".subtitle-item").length===23 && document.querySelectorAll(".word-card").length===5 && document.querySelectorAll("audio[controls]").length===4'));
 check('publishing copy and both offline covers retained',await page.eval('new Set([...document.querySelectorAll(".publish-keyword")].map(x=>x.textContent)).size===30 && document.querySelectorAll(".publish-topic").length<=5 && document.querySelectorAll("a.cover-download[download]").length===2 && [...document.querySelectorAll("a.cover-download")].every(a=>a.href.startsWith("data:image/png;base64,"))'));
 await shot(page,'desktop-poster.jpg');
 const contact=[];
 for(const t of [0,3.8,4.3,4.8,5.3,5.8,8,10,12,16]){
  await page.eval(t=>{scrollTo(0,0);episodeAnimation.seek(t);},t);
  contact.push({t,src:await page.eval('document.querySelector("canvas").toDataURL("image/jpeg",.9)')});
  if([0,4.3,4.8,5.8,12].includes(t))await shot(page,`desktop-${String(t).replace('.','-')}.jpg`);
 }
 const helper=await browser.newPage({width:1440,height:1470});
 await helper.eval(frames=>{
  document.body.style.cssText='margin:0;padding:20px;background:#102724;color:white;font:18px system-ui;display:grid;grid-template-columns:1fr 1fr;gap:20px';
  document.body.innerHTML=frames.map(f=>`<figure style="margin:0"><figcaption>${f.t.toFixed(1)} s</figcaption><img style="width:100%;display:block" src="${f.src}"></figure>`).join('');
  return Promise.all([...document.images].map(i=>i.decode()));
 },contact);
 await helper.screenshot({path:resolve(out,'contact-sheet.jpg'),fullPage:true,quality:90});report.screenshots.push('contact-sheet.jpg');await helper.close();
 report.temporal=await page.eval(()=>{
  const source=document.querySelector('#animation-canvas');const c=document.createElement('canvas');c.width=192;c.height=108;
  const ctx=c.getContext('2d',{willReadFrequently:true});let previous=null,max=0,sum=0,worstAt=0;const rows=[];
  for(let i=0;i<=480;i++){
   const t=i/30;episodeAnimation.seek(t);ctx.drawImage(source,0,0,192,108);
   const pixels=ctx.getImageData(0,0,192,108).data;
   if(previous){let d=0;for(let k=0;k<pixels.length;k+=4)d+=Math.abs(pixels[k]-previous[k])+Math.abs(pixels[k+1]-previous[k+1])+Math.abs(pixels[k+2]-previous[k+2]);
    d/=192*108*3*255;sum+=d;if(d>max){max=d;worstAt=t;}if(i%30===0)rows.push({at:t,difference:d});}
   previous=pixels;
  }
  return{sample_fps:30,frames:481,mean_difference:sum/480,max_difference:max,worst_at:worstAt,seconds:rows};
 });
 check('no abrupt canvas frame changes at 30 fps sampling',report.temporal.max_difference<.015);
 await page.eval('episodeAnimation.seek(0);scrollTo(0,0)');await click(page,'.cinema-play');await sleep(500);
 check('click starts playback',await page.eval('episodeAnimation.state.playing && episodeAnimation.state.time>.2'));
 await click(page,'#animation-play');const paused=await page.eval('episodeAnimation.state.time');await sleep(200);
 check('pause holds time',Math.abs(await page.eval('episodeAnimation.state.time')-paused)<.01);
 await click(page,'[data-seek="4"]');check('chapter seeks without autoplay',await page.eval('episodeAnimation.state.time===4 && !episodeAnimation.state.playing'));
 await page.eval('document.querySelector("#animation-progress").focus()');
 await page.send('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});
 await page.send('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});
 check('keyboard seek works',await page.eval('episodeAnimation.state.time>4'));
 await click(page,'#animation-sound');check('sound toggle state',await page.eval('!episodeAnimation.state.sound'));
 // Play the entire shot in real time as well as comparing individual canvas frames.
 report.playback=await page.eval(()=>new Promise(resolve=>{
  const gaps=[];let previous=performance.now(),start=previous;
  episodeAnimation.seek(0);episodeAnimation.play();
  function inspect(now){gaps.push(now-previous);previous=now;
   if(episodeAnimation.state.time>=16&&!episodeAnimation.state.playing){const ordered=[...gaps].sort((a,b)=>a-b);resolve({wall_seconds:(now-start)/1000,rendered_frames:gaps.length,median_frame_ms:ordered[Math.floor(ordered.length/2)],p95_frame_ms:ordered[Math.floor(ordered.length*.95)],max_frame_ms:Math.max(...gaps),final:episodeAnimation.state});}
   else requestAnimationFrame(inspect);
  }requestAnimationFrame(inspect);
 }));
 check('full shot plays to 16 seconds and stops',report.playback.final.time===16&&!report.playback.final.playing);
 await click(page,'#animation-restart');await sleep(120);check('replay restarts',await page.eval('episodeAnimation.state.playing && episodeAnimation.state.time<1'));
 await page.eval('document.querySelector("audio").play()');await sleep(200);
 check('offline audition decodes and pauses animation',await page.eval('!episodeAnimation.state.playing&&!document.querySelector("audio").paused&&Number.isFinite(document.querySelector("audio").duration)'));await page.eval('document.querySelector("audio").pause()');
 for(const width of [768,390,375]){
  await page.setViewport({width,height:width===768?1024:844,mobile:width<600});
  for(const t of [0,4.8,5.8,12]){await page.eval(t=>{scrollTo(0,0);episodeAnimation.seek(t);},t);await shot(page,`${width}-${String(t).replace('.','-')}.jpg`);}
  check(`no horizontal overflow at ${width}`,await page.eval('document.documentElement.scrollWidth<=innerWidth'));
 }
 report.errors.push(...page.consoleErrors);
 const reduced=await browser.newPage({width:390,height:844,mobile:true,reducedMotion:true});await reduced.goto(pathToFileURL(resolve(root,'episodes/book-01/ep-001.html')).href,{settleMs:600});
 check('reduced motion has no autoplay and retains illustration',await reduced.eval('episodeAnimation.state.ready&&episodeAnimation.state.reducedMotion&&!episodeAnimation.state.playing'));
 await reduced.eval('episodeAnimation.seek(5.8)');await shot(reduced,'reduced-motion.jpg');report.errors.push(...reduced.consoleErrors);
 check('no external resource requests',report.requests.length===0);check('no browser errors',report.errors.length===0);report.passed=true;
}finally{await browser.close();writeFileSync(resolve(out,'verification.json'),JSON.stringify(report,null,2));}
console.log(JSON.stringify({passed:report.passed,checks:report.checks.length,temporal:report.temporal,playback:report.playback},null,2));
