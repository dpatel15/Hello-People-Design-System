const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs = require('fs');
const dims = {
  '01-post-mon':[1080,1080],'02-story-mon':[1080,1920],'03-beforeafter-tue':[1080,1080],
  '04-carousel-1-cover':[1080,1350],'05-carousel-2':[1080,1350],'06-carousel-3':[1080,1350],
  '07-carousel-4':[1080,1350],'08-carousel-5-cta':[1080,1350]
};
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
