const root = 'file:///Users/huyin/Swingboat/english-to-be-continued/episodes/book-01/';
await page.goto(root + 'ep-002.html', {waitUntil: 'load'});
await page.emulateMedia({reducedMotion: 'reduce'});
const initial = await tabbit.observe({frames: 'none', maxChars: 1500});
const reports = [];
const screenshots = [];
for (let n = 2; n <= 15; n++) {
  const ep = String(n).padStart(3, '0');
  await page.goto(root + 'ep-' + ep + '.html', {waitUntil: 'load'});
  await page.setViewportSize({width: 1440, height: 1000});
  await page.getByRole('link', {name: '抖音发布', exact: true}).click();
  await expect(page.getByRole('heading', {name: '抖音发布资料。', exact: true})).toBeVisible();
  await page.locator('.publish-cover-title').scrollIntoViewIfNeeded();
  await page.locator('.publish-cover img').evaluateAll(imgs => Promise.all(imgs.map(i => i.decode())));
  const structure = await page.evaluate(() => ({
    keywords: document.querySelectorAll('.publish-keyword').length,
    unique: new Set([...document.querySelectorAll('.publish-keyword')].map(n => n.textContent)).size,
    topics: document.querySelectorAll('.publish-topic').length,
    scenes: document.querySelectorAll('.scene').length,
    panels: document.querySelectorAll('.scene-picture svg').length,
    subtitles: document.querySelectorAll('.subtitle-item').length,
    cards: document.querySelectorAll('.word-card').length,
    images: [...document.querySelectorAll('.publish-cover img')].map(i => ({width: i.naturalWidth, height: i.naturalHeight, complete: i.complete})),
    links: [...document.querySelectorAll('.cover-download')].map(a => ({name: a.download, embedded: a.href.startsWith('data:image/png;base64,'), sameAsPreview: a.href === a.closest('figure').querySelector('img').src})),
    resources: performance.getEntriesByType('resource').map(r => r.name).filter(s => !s.startsWith('data:'))
  }));
  expect(structure.keywords).toBe(30); expect(structure.unique).toBe(30);
  expect(structure.topics).toBe(5); expect(structure.scenes).toBe(8); expect(structure.panels).toBe(8);
  expect(structure.subtitles).toBe(n === 4 ? 24 : 22);
  expect(structure.cards).toBe([11, 13, 14].includes(n) ? 6 : 5);
  expect(structure.links.every(a => a.name && a.embedded && a.sameAsPreview)).toBe(true);
  expect(structure.images[0].width * 3).toBe(structure.images[0].height * 4);
  expect(structure.images[1].width * 4).toBe(structure.images[1].height * 3);
  expect(structure.images.every(i => i.complete && i.width > 0)).toBe(true);
  expect(structure.resources).toEqual([]);
  const layouts = [];
  for (const [width, height] of [[375, 950], [768, 1000], [1440, 1000], [812, 375]]) {
    await page.setViewportSize({width, height});
    await page.locator('#publishing').scrollIntoViewIfNeeded();
    const layout = await page.evaluate(() => ({
      width: innerWidth,
      document: document.documentElement.scrollWidth,
      overflow: [...document.querySelectorAll('.publishing-field,.publish-copy,.publish-cover,.cover-download,.voice-en,.caption-zh')].filter(n => n.scrollWidth > n.clientWidth + 1).map(n => n.id || n.className)
    }));
    expect(layout.document).toBe(width); expect(layout.overflow).toEqual([]); layouts.push(layout);
  }
  const firstWord = page.locator('.word-links a').first();
  const target = await firstWord.getAttribute('href');
  await firstWord.click();
  expect(await page.evaluate(() => location.hash)).toBe(target);
  await expect(page.locator(target)).toBeVisible();
  await page.locator('#scene-1 .dialogue-reference summary').click();
  await expect(page.locator('#scene-1 .dialogue-reference .dialogue')).toBeVisible();
  await page.locator('#scene-1 .dialogue-reference summary').click();
  if (n === 2) {
    await page.setViewportSize({width: 1440, height: 1000});
    await page.locator('#publishing').scrollIntoViewIfNeeded();
    screenshots.push({name: 'publishing-batch-desktop-text.png', receipt: await page.screenshot({fullPage: false})});
  }
  if (n === 14) {
    await page.setViewportSize({width: 375, height: 950});
    await page.locator('#publish-cover-3x4').scrollIntoViewIfNeeded();
    screenshots.push({name: 'publishing-batch-mobile-review.png', receipt: await page.screenshot({fullPage: false})});
    const review = page.locator('.core-review-card').first();
    await review.locator('.core-review-answer summary').click();
    await expect(review.locator('.core-review-answer[open]')).toBeVisible();
    await review.locator('.core-review-answer summary').click();
  }
  if (n === 15) {
    await page.setViewportSize({width: 1440, height: 1000});
    await page.locator('.publish-cover-title').scrollIntoViewIfNeeded();
    screenshots.push({name: 'publishing-batch-desktop-family.png', receipt: await page.screenshot({fullPage: false})});
  }
  reports.push({episode: n, structure, layouts, publishingNavVerified: true, wordLinkVerified: true, referenceDialogueVerified: true});
}
await page.setViewportSize({width: 1440, height: 1000});
await page.emulateMedia({reducedMotion: 'no-preference'});
await page.goto(root + 'ep-015.html#publishing', {waitUntil: 'load'});
return {status: 'passed', initialObservation: initial.snapshot.slice(0, 600), reports, screenshots};
