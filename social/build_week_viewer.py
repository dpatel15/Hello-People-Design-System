# =============================================================================
# HELLO PEOPLE, week viewer builder v2
# Adds:
#  - per-image download (click = save PNG; a small download badge on hover)
#  - "Download all images (ZIP)" button at the top (JSZip embedded inline)
# Run:  python3 build_week_viewer_v2.py <path-to-week-folder> <path-to-jszip.min.js>
# =============================================================================
import sys, os, csv, base64, re, html, glob

DAYS = [("mon","Monday"),("tue","Tuesday"),("wed","Wednesday"),("thu","Thursday"),
        ("fri","Friday"),("sat","Saturday"),("sun","Sunday")]

def esc(s): return html.escape(s or "")

def bold(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

def md_light(t):
    out=[]
    for line in t.splitlines():
        l=line.rstrip()
        if l.startswith("## "): out.append(f"<h3>{esc(l[3:])}</h3>")
        elif l.startswith("# "): out.append(f"<h2>{esc(l[2:])}</h2>")
        elif l.startswith("- "): out.append(f"<li>{bold(esc(l[2:]))}</li>")
        elif l.strip()=="---": out.append("<hr>")
        elif l.strip()=="": out.append("<br>")
        else: out.append(f"<p>{bold(esc(l))}</p>")
    return "\n".join(out)

def img_data_uri(path):
    ext = path.rsplit(".",1)[-1].lower()
    mime = "image/png" if ext=="png" else ("image/jpeg" if ext in ("jpg","jpeg") else "image/"+ext)
    with open(path,"rb") as f:
        return f"data:{mime};base64,"+base64.b64encode(f.read()).decode()

def day_of(name):
    n=name.lower()
    for tok,full in DAYS:
        if tok in n: return full
    return None

def build(week_dir, jszip_path):
    week_dir=week_dir.rstrip("/")
    label=os.path.basename(week_dir)
    jszip = open(jszip_path, "r", encoding="utf-8").read()
    rows=[]
    csvp=os.path.join(week_dir,"content.csv")
    theme=""
    if os.path.exists(csvp):
        with open(csvp,encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows.append(r); theme=theme or r.get("Theme","")
    order=[]; byday={}
    for r in rows:
        d=r.get("Day") or r.get("Date") or "Other"
        if d not in byday: byday[d]=[]; order.append(d)
        byday[d].append(r)
    imgs=sorted(glob.glob(os.path.join(week_dir,"images","*")))
    img_groups={}
    for p in imgs:
        d=day_of(os.path.basename(p)) or "More"
        img_groups.setdefault(d,[]).append(p)
    reels=""
    rp=os.path.join(week_dir,"reel-scripts.md")
    if os.path.exists(rp): reels=open(rp,encoding="utf-8").read()

    def post_card(r):
        parts=[f'<div class="pf">{esc(r.get("Platform",""))}<span class="fmt">{esc(r.get("Format",""))}</span></div>']
        parts.append(f'<div class="copy">{esc(r.get("Post copy","")).replace(chr(10),"<br>")}</div>')
        if r.get("Hashtags"): parts.append(f'<div class="meta"><b>Hashtags</b> {esc(r["Hashtags"])}</div>')
        if r.get("CTA"): parts.append(f'<div class="meta"><b>CTA</b> {esc(r["CTA"])}</div>')
        if r.get("Alt text"): parts.append(f'<div class="meta"><b>Alt text</b> {esc(r["Alt text"])}</div>')
        return f'<div class="post">{"".join(parts)}</div>'

    def img_fig(p):
        base = os.path.basename(p)
        uri = img_data_uri(p)
        # Single copy of the data URI (on the <img>). A wrapping <a> lifts it
        # to its href at load time via JS so click-to-download still works, but
        # the HTML source stores the payload only once.
        return (
            f'<figure>'
            f'<a class="dl" href="#" download="{esc(base)}" title="Download {esc(base)}">'
            f'<img data-name="{esc(base)}" src="{uri}" alt="{esc(base)}">'
            f'<span class="badge" aria-hidden="true">&#8595;</span>'
            f'</a>'
            f'<figcaption>{esc(base)}</figcaption>'
            f'</figure>'
        )

    day_sections=[]
    for d in order:
        rs=byday[d]
        angle=rs[0].get("Angle","")
        full=None
        for tok,fu in DAYS:
            if str(d).lower().startswith(tok) or str(d).lower()==fu.lower(): full=fu
        gimgs=img_groups.get(full or "",[])
        imghtml="".join(img_fig(p) for p in gimgs)
        day_sections.append(f"""
        <section class="day">
          <div class="dayhead"><span class="daytag">{esc(str(d))}</span><span class="angle">{esc(angle)}</span></div>
          {f'<div class="gallery">{imghtml}</div>' if imghtml else ''}
          <div class="posts">{''.join(post_card(r) for r in rs)}</div>
        </section>""")

    leftover=[]
    matched_groups=set()
    for d in order:
        for tok,fu in DAYS:
            if str(d).lower().startswith(tok): matched_groups.add(fu)
    for g,ps in img_groups.items():
        if g not in matched_groups:
            leftover+=ps
    leftover_html=""
    if leftover:
        leftover_html='<section class="day"><div class="dayhead"><span class="daytag">More images</span></div><div class="gallery">'+ "".join(img_fig(p) for p in leftover) +'</div></section>'

    html_out=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hello People, week {esc(label)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--blue:#1D50CF;--ink:#1B1E27;--muted:#565B6A;--line:#E6E7EE;--bg:#F7F8FB;--quiet:#E4EAF9}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,system-ui,sans-serif}}
h1,h2,h3{{font-family:Poppins,sans-serif}}
.top{{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--line);padding:14px 24px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}}
.top h1{{font-size:18px;margin:0}}.top .sub{{color:var(--muted);font-size:13px}}
.nav a{{color:var(--blue);text-decoration:none;font-weight:600;font-size:13px;margin-left:14px}}
.actions{{display:flex;gap:8px;align-items:center}}
.btn{{background:var(--blue);color:#fff;font-weight:700;font-size:13px;padding:10px 14px;border-radius:10px;border:0;cursor:pointer}}
.btn:disabled{{opacity:.6;cursor:default}}
.btn.secondary{{background:#fff;color:var(--blue);border:1px solid var(--line)}}
.wrap{{max-width:1000px;margin:0 auto;padding:24px}}
.hint{{background:var(--quiet);color:#123FA8;border-radius:10px;padding:12px 16px;font-size:13.5px;margin-bottom:20px}}
.day{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px;margin-bottom:22px}}
.dayhead{{display:flex;align-items:baseline;gap:14px;margin-bottom:14px;flex-wrap:wrap}}
.daytag{{font-family:Poppins;font-weight:800;color:var(--blue);font-size:20px}}
.angle{{color:var(--muted);font-size:15px}}
.gallery{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin-bottom:16px}}
figure{{margin:0}}
.dl{{position:relative;display:block;border:1px solid var(--line);border-radius:10px;overflow:hidden;cursor:pointer;text-decoration:none;color:inherit}}
.dl img{{width:100%;display:block;transition:transform .15s ease}}
.dl:hover img{{transform:scale(1.02)}}
.dl .badge{{position:absolute;top:6px;right:6px;background:rgba(29,80,207,.92);color:#fff;font-weight:700;font-size:14px;line-height:1;padding:6px 8px;border-radius:8px;opacity:0;transform:translateY(-4px);transition:opacity .15s ease, transform .15s ease}}
.dl:hover .badge, .dl:focus-visible .badge{{opacity:1;transform:translateY(0)}}
figcaption{{font-size:11px;color:var(--muted);margin-top:4px;text-align:center;word-break:break-all}}
.posts{{display:grid;gap:12px}}
.post{{border:1px solid var(--line);border-radius:12px;padding:14px 16px}}
.pf{{font-weight:700;color:var(--ink);font-size:14px;margin-bottom:8px}}
.fmt{{color:var(--muted);font-weight:500;margin-left:8px;font-size:12px}}
.copy{{white-space:normal;font-size:14.5px;line-height:1.55}}
.meta{{font-size:12.5px;color:var(--muted);margin-top:8px}}.meta b{{color:var(--ink)}}
.reels{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:8px 24px 24px}}
.reels h2{{color:var(--blue)}} .reels h3{{margin-top:22px}} .reels hr{{border:0;border-top:1px solid var(--line);margin:18px 0}}
.reels li{{margin:4px 0}} .reels p{{margin:6px 0;line-height:1.5}}
.progress{{font-size:12px;color:var(--muted);margin-left:6px}}
</style></head>
<body>
<div class="top">
  <div><h1>Hello People, content week</h1><div class="sub">{esc(label)} &middot; {esc(theme)}</div></div>
  <div class="actions">
    <button id="dl-zip" class="btn" type="button">Download all images (ZIP)</button>
    <span id="dl-progress" class="progress"></span>
    <div class="nav"><a href="#posts">Posts</a><a href="#reels">Reels</a></div>
  </div>
</div>
<div class="wrap">
  <div class="hint">Everything for the week in one page. <strong>Click any image to download the PNG.</strong> Use the ZIP button at the top for all 42 at once. Each day shows its images, captions for every platform, and the reel scripts at the end.</div>
  <h2 id="posts">Posts by day</h2>
  {''.join(day_sections)}
  {leftover_html}
  <h2 id="reels" style="margin-top:30px">Reel scripts</h2>
  <div class="reels">{md_light(reels) if reels else '<p>No reel scripts found.</p>'}</div>
</div>
<script>
{jszip}
</script>
<script>
(function(){{
  // Lift each image's data URI onto its anchor's href once, so clicks download.
  var anchors=document.querySelectorAll('.dl');
  anchors.forEach(function(a){{
    var img=a.querySelector('img');
    if (img && img.src) a.setAttribute('href', img.src);
  }});
  var btn=document.getElementById('dl-zip'), prog=document.getElementById('dl-progress');
  btn.addEventListener('click', async function(){{
    btn.disabled=true; prog.textContent='Packing...';
    var zip=new JSZip();
    var imgs=document.querySelectorAll('.dl img');
    var i=0;
    for (var img of imgs) {{
      var name=img.getAttribute('data-name');
      var b64=img.src.split(',')[1];
      zip.file(name, b64, {{base64:true}});
      i++; prog.textContent='Packing '+i+' of '+imgs.length+'...';
      await new Promise(r=>setTimeout(r,0));
    }}
    prog.textContent='Zipping...';
    var blob = await zip.generateAsync({{type:'blob'}}, function(m){{
      prog.textContent='Zipping '+Math.round(m.percent)+'%';
    }});
    var url=URL.createObjectURL(blob);
    var a=document.createElement('a');
    a.href=url; a.download='hello-people-week-{esc(label)}.zip';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function(){{URL.revokeObjectURL(url);}}, 5000);
    prog.textContent='Done. '+imgs.length+' images downloaded.';
    btn.disabled=false;
  }});
}})();
</script>
</body></html>"""
    out=os.path.join(week_dir,"week.html")
    open(out,"w",encoding="utf-8").write(html_out)
    print("wrote",out,f"({len(html_out)//1024} KB, {len(rows)} posts, {len(imgs)} images)")

if __name__=="__main__":
    if len(sys.argv)<3:
        print("usage: python3 build_week_viewer_v2.py <week-folder> <jszip-min-js>"); sys.exit(1)
    build(sys.argv[1], sys.argv[2])
