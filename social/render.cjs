const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs = require('fs');
// Auto-size each .html file by its filename suffix.
// Naming convention: use "-story" for 1080x1920, "-beforeafter" or "-post" for
// 1080x1080, "-carousel-*", "-cover", "-item", "-cta", or "-code" for 1080x1350.
const CAROUSEL = [1080,1350], STORY = [1080,1920], SQUARE = [1080,1080];
function pickDims(base){
  const n = base.toLowerCase();
  if (n.includes('-story')) return STORY;
  if (n.includes('-beforeafter') || n.includes('-post')) return SQUARE;
  return CAROUSEL;
}
const dims = {};
for (const f of fs.readdirSync('.').sort()) {
  if (!f.endsWith('.html')) continue;
  const base = f.replace(/\.html$/,'');
  dims[base] = pickDims(base);
}
(async () => {
  const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const [name,[w,h]] of Object.entries(dims)) {
    const ctx = await b.newContext({ viewport:{width:w,height:h}, deviceScaleFactor:2 });
    const p = await ctx.newPage();
    await p.goto('file://'+process.cwd()+'/'+name+'.html', { waitUntil:'networkidle' });
    await p.waitForTimeout(400);
    await p.screenshot({ path:name+'.png' });
    await ctx.close();
    console.log('rendered', name, w+'x'+h, '@2x');
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
