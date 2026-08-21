# =============================================================================
# HELLO PEOPLE, social slide generator
# Renders on-brand post/story/carousel slides from the design system.
# Run:  python3 generate.py  &&  node render.cjs   (outputs PNGs beside the HTML)
#
# LOCKED VISUAL RULES (do not drift):
#   - Background: warped grid + ribbons SVG, soft center wash for legibility.
#   - Headline: Poppins 800; key words wrapped in a solid-blue .hl block
#     (white .hl on the blue slide). Body: Inter.
#   - Contextual illustration: ONE faint line illustration, relevant to the
#     slide's message, placed in an otherwise empty band. Skip it where the
#     slide is already full (e.g. the feed post and before/after).
#       * stroke-width = 0.3   (fine hairline)
#       * opacity      = 0.15  (light, same on light AND dark slides)
#     Add new illustrations to the P{} library, matching the topic.
#   - Always sign off with the logo + @hellopeople_agency.
#   - Copy follows brand voice: plain, human, no em/en dashes, lead CTA.
# =============================================================================
# Build on-brand social slides from the Hello People design system.
CSS = """
@import "../assets/fonts/hello-people-fonts-social.css";
:root{
  --blue:#1D50CF; --violet:#903DA4; --magenta:#E0497C; --ink:#1B1E27;
  --ink2:#3F454C; --muted:#565B6A; --line:#E6E7EE;
  --grad:linear-gradient(120deg,#1D50CF 0%,#903DA4 52%,#E0497C 100%);
}
*{margin:0;padding:0;box-sizing:border-box}
.slide{position:relative;overflow:hidden;background:#fff;color:var(--ink);
  font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.bg{position:absolute;inset:0;background:#fff url(../assets/social/backgrounds/hello-people-bg-grid-ribbons.svg) center/cover no-repeat}
.wash{position:absolute;inset:0;background:radial-gradient(120% 70% at 50% 50%,rgba(255,255,255,.92) 40%,rgba(255,255,255,0) 100%)}
.c{position:relative;z-index:2;display:flex;flex-direction:column;height:100%}
.eyebrow{font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
h1{font-family:'Poppins',sans-serif;font-weight:800;color:var(--ink);line-height:1.06;letter-spacing:-.02em}
.body{color:var(--ink2);line-height:1.5}
.hl{background:var(--blue);color:#fff;padding:.04em .16em;border-radius:8px;
  box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hlg{background:var(--grad);color:#fff;padding:.04em .16em;border-radius:8px;
  box-decoration-break:clone;-webkit-box-decoration-break:clone}
.list{display:flex;flex-direction:column}
.item{display:flex;align-items:flex-start;gap:22px;color:var(--ink)}
.tick{flex:none;border-radius:50%;background:#E7F6EE;color:#12A150;display:flex;align-items:center;justify-content:center}
.foot{margin-top:auto;display:flex;align-items:center;justify-content:space-between;position:relative;z-index:3}
.foot img{height:52px;width:auto}
.handle{font-weight:600;color:var(--muted)}
.num{font-family:'Poppins',sans-serif;font-weight:800;color:var(--blue);line-height:1}
.pill{display:inline-flex;align-items:center;gap:14px;background:#fff;border:2px solid var(--line);
  border-radius:999px;font-weight:600;color:var(--ink)}
.dot{width:14px;height:14px;border-radius:50%;background:var(--blue)}
/* light contextual illustration, fills space without pulling the eye */
.illo{position:absolute;z-index:1;pointer-events:none;color:var(--blue);opacity:.15}
.illo svg{width:100%;height:100%;display:block}
/* blue variant */
.slide--blue{background:var(--blue);color:#fff}
.slide--blue .bg{opacity:.14;mix-blend-mode:screen}
.slide--blue .wash{display:none}
.slide--blue h1{color:#fff}
.slide--blue .eyebrow{color:#c7d6f7}
.slide--blue .hl{background:#fff;color:var(--blue)}
.slide--blue .body{color:#e8eefc}
.slide--blue .handle{color:#c7d6f7}
.slide--blue .illo{color:#fff;opacity:.15}
.swipe{display:inline-flex;align-items:center;gap:12px;font-weight:700;color:var(--blue)}
.slide--blue .swipe{color:#fff}
"""

# Light line illustrations (Lucide-style, 24 grid) sized big and faint.
def illo(name, style):
    P = {
      # fast reply / follow-up: send (paper plane)
      "send":'<path d="M14.54 9.46 22 2 15.6 22a.55.55 0 0 1-1 0l-3.6-8.1L2.9 10.3a.55.55 0 0 1 0-1L22 2"/>',
      # reminders: calendar with clock
      "calclock":'<path d="M21 7.5V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h4"/><path d="M16 2v4M8 2v4M3 10h18"/><circle cx="17.5" cy="17.5" r="4.5"/><path d="M17.5 15.6v2l1.4 1"/>',
      # DMs: two chat bubbles
      "dms":'<path d="M14 9a2 2 0 0 1-2 2H6l-4 4V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2z"/><path d="M10 9h8a2 2 0 0 1 2 2v9l-4-4h-4a2 2 0 0 1-2-2"/>',
      # cover: checklist of tasks
      "tasks":'<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8M13 12h8M13 18h8"/>',
      # CTA: audit / clipboard check
      "audit":'<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M9 2h6a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z"/><path d="m9 14 2 2 4-4"/>',
      # time / what eats your week: clock
      "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    }
    return f'<div class="illo" style="{style}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="0.3" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg></div>'

def page(w,h,inner,cls="",extra=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.slide{{width:{w}px;height:{h}px}}</style></head>
<body><div class="slide {cls}"><div class="bg"></div><div class="wash"></div>
{extra}<div class="c">{inner}</div></div></body></html>"""

TICK='<span class="tick" style="width:52px;height:52px"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>'
def foot(white=False):
    lg = "../assets/logo/hello-people-logo-white.svg" if white else "../assets/logo/hello-people-logo.svg"
    return f'<div class="foot"><img src="{lg}"><span class="handle">@hellopeople_agency</span></div>'

slides = {}

# ---- Mon: IG feed post 1080x1080 (already full, no illo)
slides["01-post-mon.html"] = page(1080,1080, f"""
<div style="padding:84px 84px 70px;height:100%;display:flex;flex-direction:column">
  <span class="eyebrow" style="font-size:24px">AI in real life</span>
  <h1 style="font-size:82px;margin-top:26px">Everyone says<br>use <span class="hl">AI</span>.<br>Nobody says<br>what for.</h1>
  <p class="body" style="font-size:30px;margin-top:30px">Here is what it actually does in a workday:</p>
  <div class="list" style="gap:22px;margin-top:30px;font-size:31px;font-weight:600">
    <div class="item">{TICK}<span>Chases your unpaid invoices</span></div>
    <div class="item">{TICK}<span>Books appointments, no phone tag</span></div>
    <div class="item">{TICK}<span>Answers the same 10 questions</span></div>
  </div>
  {foot()}
</div>""")

# ---- Mon: IG story 1080x1920 (clock illo fills lower gap)
slides["02-story-mon.html"] = page(1080,1920, f"""
<div style="padding:300px 84px 320px;height:100%;display:flex;flex-direction:column">
  <span class="eyebrow" style="font-size:26px">AI in real life</span>
  <h1 style="font-size:96px;margin-top:34px">What eats<br>most of your<br><span class="hl">week?</span></h1>
  <div style="display:flex;flex-direction:column;gap:26px;margin-top:70px">
    <span class="pill" style="font-size:34px;padding:26px 40px"><span class="dot"></span>Admin and data entry</span>
    <span class="pill" style="font-size:34px;padding:26px 40px"><span class="dot"></span>Chasing follow-ups</span>
    <span class="pill" style="font-size:34px;padding:26px 40px"><span class="dot"></span>Phone tag</span>
  </div>
  <p class="body" style="font-size:30px;margin-top:60px">Tap to vote. We automate the winner.</p>
  {foot()}
</div>""", extra=illo("clock","right:70px;bottom:360px;width:300px;height:300px"))

# ---- Tue: Before / after 1080x1080 (full, no illo)
slides["03-beforeafter-tue.html"] = page(1080,1080, f"""
<div style="padding:80px 80px 66px;height:100%;display:flex;flex-direction:column">
  <span class="eyebrow" style="font-size:24px">AI in real life</span>
  <h1 style="font-size:64px;margin-top:22px">Same task.<br>A fraction of the <span class="hl">time.</span></h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:44px;flex:1">
    <div style="background:#fff;border:2px solid var(--line);border-radius:28px;padding:40px;display:flex;flex-direction:column">
      <div style="font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)">Before, by hand</div>
      <div class="body" style="font-size:27px;margin-top:18px;line-height:1.45">Two people, most of two days, copy and paste, missed follow-ups.</div>
      <div style="margin-top:auto;font-family:'Poppins';font-weight:800;font-size:52px;color:var(--ink)">16 hrs</div>
    </div>
    <div style="background:var(--blue);color:#fff;border-radius:28px;padding:40px;display:flex;flex-direction:column">
      <div style="font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:.9">After, automated</div>
      <div style="font-size:27px;margin-top:18px;line-height:1.45;color:#eaf0fd">One system, running on its own, correct every time.</div>
      <div style="margin-top:auto;font-family:'Poppins';font-weight:800;font-size:52px">2 hrs</div>
    </div>
  </div>
  <div style="margin-top:30px">{foot()}</div>
</div>""")

# ---- Wed: CAROUSEL 1080x1350 (5 slides)
CW,CH=1080,1350
slides["04-carousel-1-cover.html"] = page(CW,CH, f"""
<div style="padding:96px 84px 78px;height:100%;display:flex;flex-direction:column">
  <span class="eyebrow" style="font-size:24px">AI in real life</span>
  <h1 style="font-size:96px;margin-top:28px">3 tasks you can<br>hand to <span class="hl">AI</span><br>this week</h1>
  <p class="body" style="font-size:30px;margin-top:30px">Start with the one you dread most.</p>
  <div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between">
    <span class="swipe" style="font-size:28px">Swipe <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
    <img src="../assets/logo/hello-people-logo.svg" style="height:48px">
  </div>
</div>""", extra=illo("tasks","right:76px;bottom:300px;width:330px;height:330px"))

def car(n,title,sub,ill):
    return page(CW,CH, f"""
<div style="padding:96px 84px 78px;height:100%;display:flex;flex-direction:column">
  <div class="num" style="font-size:150px">0{n}</div>
  <h1 style="font-size:78px;margin-top:8px">{title}</h1>
  <p class="body" style="font-size:34px;margin-top:26px;max-width:20ch">{sub}</p>
  <div style="margin-top:auto"><span class="handle" style="font-size:26px">@hellopeople_agency</span></div>
</div>""", extra=illo(ill,"right:78px;bottom:150px;width:340px;height:340px"))
slides["05-carousel-2.html"]=car(1,'Lead <span class="hl">follow-ups</span>','A reply within 5 minutes, every time, not when someone remembers.','send')
slides["06-carousel-3.html"]=car(2,'Appointment <span class="hl">reminders</span>','Fewer no-shows, zero effort from your team.','calclock')
slides["07-carousel-4.html"]=car(3,'First reply to <span class="hl">DMs</span>','Nobody sits waiting while you are busy with a client.','dms')

slides["08-carousel-5-cta.html"] = page(CW,CH, f"""
<div style="padding:96px 84px 82px;height:100%;display:flex;flex-direction:column">
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <span class="eyebrow" style="font-size:24px">Say hello to less busywork</span>
    <h1 style="font-size:92px;margin-top:28px">Want the list for<br>your <span class="hl">business?</span></h1>
    <p class="body" style="font-size:34px;margin-top:30px;max-width:24ch">Comment AUDIT and we will send you where to start, free.</p>
  </div>
  {foot(white=True)}
</div>""","slide--blue", extra=illo("audit","right:80px;bottom:210px;width:330px;height:330px"))

for name,html in slides.items():
    open(name,"w",encoding="utf-8").write(html)
print("wrote", len(slides), "slides")
