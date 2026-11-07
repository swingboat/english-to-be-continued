import { Browser, sleep } from '../../../../.agents/skills/taste-skill/scripts/lib/cdp.mjs';
import { resolve, join } from 'node:path';
const root=resolve('.'),out=join(root,'production/book-01/ep-004/checks');
const browser=await Browser.launch();
try{
 const page=await browser.newPage({width:1440,height:1000});
 await page.goto('file://'+join(root,'episodes/book-01/ep-004.html'));
 await page.eval(()=>document.documentElement.style.scrollBehavior='auto');
 for(const width of [1440,390]){
  await page.setViewport({width,height:width===390?844:1000});
  for(const selector of ['#words','#cast','#publishing','#publish-cover-4x3','#publish-cover-3x4','.publishing-research','.continuity-section']){
   await page.eval(s=>document.querySelector(s).scrollIntoView(),selector);await sleep(950);
   await page.screenshot({path:join(out,`final-${selector.replace(/^[#.]/,'')}-${width}.jpg`)});
  }
 }
 await page.close();
}finally{await browser.close();}
console.log('Final section screenshots captured.');
