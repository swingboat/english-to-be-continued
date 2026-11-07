// Targeted browser QA for the publication section, using the project taste-skill runtime.
import assert from 'node:assert/strict';
import {mkdirSync, writeFileSync} from 'node:fs';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {resolve, dirname} from 'node:path';
import {Browser} from '../../.agents/skills/taste-skill/scripts/lib/cdp.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../..');
const out = resolve(root, '.taste-skill/publishing-limits/sections');
mkdirSync(out, {recursive:true});
const browser = await Browser.launch();
const results = [];
const capturesOnly = process.argv.includes('--captures-only');
try {
  const page = await browser.newPage({reducedMotion:true});
  await page.send('Network.enable');
  await page.send('Network.emulateNetworkConditions', {offline:true, latency:0, downloadThroughput:0, uploadThroughput:0});
  for (const n of (capturesOnly ? [1,3,15] : Array.from({length:15},(_,i)=>i+1))) {
    await page.goto(pathToFileURL(resolve(root, `episodes/book-01/ep-${String(n).padStart(3,'0')}.html`)).href, {settleMs:50});
    for (const width of [1440,768,390]) {
      await page.setViewport({width,height:1000,mobile:width<600});
      const result = await page.eval(async () => {
        await document.fonts.ready;
        const section = document.querySelector('#publishing');
        section.scrollIntoView({block:'start',behavior:'instant'});
        await Promise.all([...section.querySelectorAll('img')].map(i=>i.decode()));
        const text = id => section.querySelector('#'+id).textContent;
        const topics = [...section.querySelectorAll('.publish-topic')].map(e=>e.textContent);
        const downloads = [...section.querySelectorAll('.cover-download')];
        const rect = section.querySelector('.publishing-fields').getBoundingClientRect();
        return {
          width:innerWidth,documentWidth:document.documentElement.scrollWidth,
          overflow:[...section.querySelectorAll('.publishing-field,dt,small,.publish-copy,.publishing-hint,.publish-cover,.cover-download')].filter(e=>e.clientWidth>0 && e.scrollWidth>e.clientWidth+1).map(e=>e.className||e.tagName),
          titleUnits:text('publish-title').length,
          captionUnits:(text('publish-description')+'\n'+topics.join(' ')).length,
          topics:topics.length,uniqueTopics:new Set(topics).size,
          keywords:section.querySelectorAll('.publish-keyword').length,
          covers:section.querySelectorAll('.publish-cover img').length,
          downloads:downloads.length,
          downloadMatchesPreview:downloads.every(a=>a.href===a.closest('figure').querySelector('img').src),
          audio:document.querySelectorAll('audio').length,
          externalResources:performance.getEntriesByType('resource').filter(r=>!r.name.startsWith('data:')).map(r=>r.name),
          clip:{x:Math.max(0,rect.left-12), y:Math.max(0,scrollY+rect.top-12),width:rect.width+24,height:rect.height+24}
        };
      });
      assert.equal(result.documentWidth,width);
      assert.deepEqual(result.overflow,[]);
      assert.ok(result.titleUnits<=30 && result.captionUnits<=1000);
      assert.equal(result.topics,5); assert.equal(result.uniqueTopics,5);
      assert.equal(result.keywords,30); assert.equal(result.covers,2); assert.equal(result.downloads,2);
      assert.equal(result.downloadMatchesPreview,true);
      assert.deepEqual(result.externalResources,[]);
      if ([1,3,15].includes(n)) {
        await page.setViewport({width,height:Math.ceil(result.clip.height+40),mobile:width<600});
        await page.eval(() => document.querySelector('.publishing-fields').scrollIntoView({block:'start',behavior:'instant'}));
        const skip = await page.eval(() => { const e=document.querySelector('.skip'); return !e || e.getBoundingClientRect().bottom<0 || getComputedStyle(e).display==='none'; });
        assert.equal(skip,true,'Unfocused skip link must not cover publication copy');
        await page.screenshot({path:resolve(out,`ep-${String(n).padStart(3,'0')}-${width}.jpg`),fullPage:false,quality:82});
      }
      delete result.clip;
      results.push({episode:n,...result});
    }
    assert.deepEqual(page.consoleErrors,[]);
  }
} finally {
  await browser.close();
}
if (!capturesOnly) writeFileSync(resolve(here,'publishing-limits-browser-verification.json'),JSON.stringify({status:'passed',offline:true,checks:results},null,2)+'\n');
console.log(JSON.stringify({status:'passed',episodes:capturesOnly?3:15,viewportChecks:results.length,widths:[1440,768,390],screenshots:out}));
