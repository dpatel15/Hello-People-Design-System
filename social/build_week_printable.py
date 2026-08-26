# =============================================================================
# HELLO PEOPLE, week printable PDF builder
# A shareable / printable / emailable PDF: thumbnail images beside every day's
# captions, then all reel scripts. Small enough to email (~5MB) but complete.
# The full-res PNGs live in weeks/<date>/images/ and are downloadable from
# week.html (per-image click + a Download-all ZIP button).
# Run:  python3 build_week_printable.py <week-folder>
# =============================================================================
import sys, os, csv, base64, re, html, glob, io
from PIL import Image  # Pillow

DAYS = [("mon","Monday"),("tue","Tuesday"),("wed","Wednesday"),("thu","Thursday"),
        ("fri","Friday"),("sat","Saturday"),("sun","Sunday")]

def esc(s): return html.escape(s or "")
def bold(s): return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

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

def thumb_data_uri(path, max_w=520, quality=78):
    img = Image.open(path).convert("RGB")
    if img.width > max_w:
        h = int(img.height * (max_w / img.width))
        img = img.resize((max_w, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def day_of(name):
    n=name.lower()
    for tok,full in DAYS:
        if tok in n: return full
    return None

def build(week_dir):
    week_dir=week_dir.rstrip("/")
    label=os.path.basename(week_dir)
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

    def post_row(r):
        parts=[f'<div class="pf">{esc(r.get("Platform",""))} <span class="fmt">{esc(r.get("Format",""))}</span></div>']
        parts.append(f'<div class="copy">{esc(r.get("Post copy","")).replace(chr(10),"<br>")}</div>')
        if r.get("Hashtags"): parts.append(f'<div class="meta"><b>Hashtags</b> {esc(r["Hashtags"])}</div>')
        if r.get("CTA"): parts.append(f'<div class="meta"><b>CTA</b> {esc(r["CTA"])}</div>')
        if r.get("Alt text"): parts.append(f'<div class="meta"><b>Alt text</b> {esc(r["Alt text"])}</div>')
        return f'<div class="post">{"".join(parts)}</div>'

    day_sections=[]
    for d in order:
        rs=byday[d]
        angle=rs[0].get("Angle","")
        full=None
        for tok,fu in DAYS:
            if str(d).lower().startswith(tok) or str(d).lower()==fu.lower(): full=fu
        gimgs=img_groups.get(full or "",[])
        thumbs="".join(f'<figure><img src="{thumb_data_uri(p)}" alt="{esc(os.path.basename(p))}"><figcaption>{esc(os.path.basename(p))}</figcaption></figure>' for p in gimgs)
        day_sections.append(f"""
        <section class="day">
          <div class="dayhead"><span class="daytag">{esc(str(d))}</span><span class="angle">{esc(angle)}</span></div>
          <div class="gallery">{thumbs}</div>
          <div class="posts">{''.join(post_row(r) for r in rs)}</div>
        </section>""")

    html_out=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Hello People, week {esc(label)} (printable)</title>
<style>
@page{{size:794px 1123px;margin:0}}
:root{{--blue:#1D50CF;--ink:#1B1E27;--muted:#565B6A;--line:#E6E7EE;--quiet:#E4EAF9}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#fff;color:var(--ink);font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.cover{{padding:80px 60px 60px;min-height:1123px;position:relative}}
.cover h1{{font-family:'Poppins',sans-serif;font-weight:800;font-size:56px;line-height:1.05;letter-spacing:-.02em;margin-top:16px}}
.hl{{background:var(--blue);color:#fff;padding:.02em .14em;border-radius:7px}}
.eyebrow{{font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}}
.lede{{color:var(--muted);font-size:16px;line-height:1.55;margin-top:20px;max-width:60ch}}
.note{{margin-top:26px;padding:16px 18px;border:1px solid var(--line);border-radius:12px;background:var(--quiet);color:#123FA8;font-size:13.5px;line-height:1.5}}
.wrap{{padding:36px 40px}}
.day{{border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:18px;page-break-inside:avoid;background:#fff}}
.dayhead{{display:flex;align-items:baseline;gap:12px;margin-bottom:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:8px}}
.daytag{{font-family:Poppins,sans-serif;font-weight:800;color:var(--blue);font-size:18px}}
.angle{{color:var(--muted);font-size:13.5px}}
.gallery{{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-bottom:12px}}
figure{{margin:0}}figure img{{width:100%;border:1px solid var(--line);border-radius:6px;display:block}}
figcaption{{font-size:9px;color:var(--muted);margin-top:2px;text-align:center;word-break:break-all;line-height:1.15}}
.posts{{display:flex;flex-direction:column;gap:8px}}
.post{{border:1px solid var(--line);border-radius:8px;padding:10px 12px;page-break-inside:avoid}}
.pf{{font-weight:700;font-size:12px;color:var(--ink);margin-bottom:5px}}
.fmt{{color:var(--muted);font-weight:500;font-size:11px;margin-left:6px}}
.copy{{font-size:12px;line-height:1.5;color:var(--ink)}}
.meta{{font-size:11px;color:var(--muted);margin-top:5px}}.meta b{{color:var(--ink)}}
h2.section{{font-family:Poppins,sans-serif;font-weight:800;font-size:24px;color:var(--blue);margin:22px 40px 12px;page-break-before:always}}
.reels{{padding:0 40px 40px;font-size:12.5px;line-height:1.55}}
.reels h2{{font-family:Poppins,sans-serif;color:var(--blue);font-size:20px;margin-top:16px}}
.reels h3{{font-family:Poppins,sans-serif;margin-top:16px;font-size:15px}}
.reels p{{margin:5px 0}}.reels li{{margin:3px 0 3px 22px}}
.reels hr{{border:0;border-top:1px solid var(--line);margin:14px 0}}
</style></head>
<body>
<div class="cover">
  <div class="eyebrow">Say hello to less busywork</div>
  <h1>Week <span class="hl">{esc(label)}</span></h1>
  <div class="lede"><strong>{esc(theme)}</strong>. This is the printable, shareable version of the week. Thumbnails, all captions per platform, and every reel script.</div>
  <div class="note">Full-resolution images are in <code>weeks/{esc(label)}/images/</code> and are one-click downloadable from <code>week.html</code> (per image, plus a "Download all as ZIP" button).</div>
</div>
<h2 class="section">Posts by day</h2>
<div class="wrap">
  {''.join(day_sections)}
</div>
<h2 class="section">Reel scripts</h2>
<div class="reels">{md_light(reels)}</div>
</body></html>"""
    tmp=os.path.join(week_dir,"week-print.html")
    open(tmp,"w",encoding="utf-8").write(html_out)
    print("wrote",tmp,f"({len(html_out)//1024} KB, {len(rows)} posts, {len(imgs)} images)")

if __name__=="__main__":
    if len(sys.argv)<2:
        print("usage: python3 build_week_printable.py <week-folder>"); sys.exit(1)
    build(sys.argv[1])
