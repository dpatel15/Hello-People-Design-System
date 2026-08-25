# =============================================================================
# HELLO PEOPLE, social slide generator (canonical template)
# Renders on-brand post/story/carousel slides from the design system.
# Run:  python3 generate.py  &&  node render.cjs   (outputs PNGs beside the HTML)
#
# LOCKED VISUAL RULES (do not drift):
#   1. Background: warped grid + ribbons SVG, soft center wash for legibility.
#   2. Headline: Poppins 800; key words wrapped in a solid-blue .hl block
#      (white .hl on the blue slide). Body: Inter.
#   3. Vertical alignment (center-then-expand): content sits vertically
#      centered in the space between the top padding and the pinned bottom
#      footer. Short content stays middle; longer content grows outward from
#      the middle. Never top-anchor content just because the slide has empty
#      room below. Covers keep the "Swipe" cue at the bottom-left.
#   4. Every slide carries the Hello People logo mark + handle
#      @dhairyapatel.official at the bottom, carousel or story, cover or CTA.
#   5. Contextual illustration: ONE faint line illustration, relevant to the
#      slide's message, anchored to the LOWER band of a carousel slide
#      (roughly bottom:180-190px) so it never sits next to or behind the copy.
#      Stories keep their own placement. Skip it where the slide is already
#      full (e.g. the before/after data card).
#       * stroke-width = 0.3   (fine hairline)
#       * opacity      = 0.15  (light, same on light AND dark slides)
#      Add new illustrations to the P{} library, matching the topic.
#   6. IG-native sizes only: 1080x1350 carousel, 1080x1920 story, 1080x1080
#      for single feed posts and before/after data cards.
#   7. Copy follows brand voice: plain, human, no em/en dashes, lead CTA.
# =============================================================================
HANDLE = "@dhairyapatel.official"       # regular sign-off (personal, for reach)
HANDLE_CTA = "@hellopeople.ca"           # CTA / lead-magnet sign-off (company, for capture)

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
/* Frame: padding top+bottom, a centered stage, a pinned footer at the bottom. */
.c{position:relative;z-index:2;display:flex;flex-direction:column;height:100%}
.stage{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}
.eyebrow{font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
h1{font-family:'Poppins',sans-serif;font-weight:800;color:var(--ink);line-height:1.06;letter-spacing:-.02em}
.body{color:var(--ink2);line-height:1.5}
.hl{background:var(--blue);color:#fff;padding:.04em .16em;border-radius:8px;
  box-decoration-break:clone;-webkit-box-decoration-break:clone}
.list{display:flex;flex-direction:column}
.item{display:flex;align-items:flex-start;gap:22px;color:var(--ink)}
.tick{flex:none;border-radius:50%;background:#E7F6EE;color:#12A150;display:flex;align-items:center;justify-content:center}
.foot{display:flex;align-items:center;justify-content:space-between;position:relative;z-index:3;gap:20px}
.foot img{height:44px;width:auto}
.handle{font-weight:600;color:var(--muted);font-size:22px}
.foot .swipe{margin-left:auto}
.num{font-family:'Poppins',sans-serif;font-weight:800;color:var(--blue);line-height:1}
.pill{display:inline-flex;align-items:center;gap:14px;background:#fff;border:2px solid var(--line);
  border-radius:999px;font-weight:600;color:var(--ink)}
.dot{width:14px;height:14px;border-radius:50%;background:var(--blue)}
.illo{position:absolute;z-index:1;pointer-events:none;color:var(--blue);opacity:.15}
.illo svg{width:100%;height:100%;display:block}
.slide--blue{background:var(--blue);color:#fff}
.slide--blue .bg{opacity:.14;mix-blend-mode:screen}
.slide--blue .wash{display:none}
.slide--blue h1{color:#fff}
.slide--blue .eyebrow{color:#c7d6f7}
.slide--blue .hl{background:#fff;color:var(--blue)}
.slide--blue .body{color:#e8eefc}
.slide--blue .handle{color:#c7d6f7}
.slide--blue .illo{color:#fff;opacity:.15}
.swipe{display:inline-flex;align-items:center;gap:12px;font-weight:700;color:var(--blue);font-size:22px}
.slide--blue .swipe{color:#fff}
.code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:24px;line-height:1.5;color:var(--ink2);background:#F4F6FB;border:1px solid var(--line);border-radius:16px;padding:24px 26px}
.slide--blue .code{background:rgba(255,255,255,.09);border-color:rgba(255,255,255,.28);color:#eaf0fd}
"""

# ---------- Illustration library ----------
P = {
  "send":'<path d="M14.54 9.46 22 2 15.6 22a.55.55 0 0 1-1 0l-3.6-8.1L2.9 10.3a.55.55 0 0 1 0-1L22 2"/>',
  "calclock":'<path d="M21 7.5V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h4"/><path d="M16 2v4M8 2v4M3 10h18"/><circle cx="17.5" cy="17.5" r="4.5"/><path d="M17.5 15.6v2l1.4 1"/>',
  "dms":'<path d="M14 9a2 2 0 0 1-2 2H6l-4 4V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2z"/><path d="M10 9h8a2 2 0 0 1 2 2v9l-4-4h-4a2 2 0 0 1-2-2"/>',
  "tasks":'<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8M13 12h8M13 18h8"/>',
  "audit":'<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M9 2h6a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z"/><path d="m9 14 2 2 4-4"/>',
  "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
}

def illo(name, style):
    return f'<div class="illo" style="{style}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="0.3" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg></div>'

SWIPE_SVG = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TICK='<span class="tick" style="width:52px;height:52px"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>'

def foot(white=False, with_swipe=False, handle=None):
    lg = "../assets/logo/hello-people-logo-white.svg" if white else "../assets/logo/hello-people-logo.svg"
    swipe = f'<span class="swipe">Swipe {SWIPE_SVG}</span>' if with_swipe else ''
    h = handle if handle is not None else HANDLE
    return f'<div class="foot"><img src="{lg}"><span class="handle">{h}</span>{swipe}</div>'

# Every slide is built through frame(): consistent padding, centered stage,
# pinned bottom footer with the logo + handle (rules 3 and 4 above).
def frame(w, h, pad, stage_inner, cls="", extra="", white_foot=False, with_swipe=False, handle=None):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.slide{{width:{w}px;height:{h}px}}</style></head>
<body><div class="slide {cls}"><div class="bg"></div><div class="wash"></div>
{extra}
<div class="c" style="padding:{pad}">
  <div class="stage">{stage_inner}</div>
  {foot(white=white_foot, with_swipe=with_swipe, handle=handle)}
</div></div></body></html>"""

CW,CH = 1080,1350   # carousel
SW,SH = 1080,1920   # story

# ---------- Building blocks (canonical patterns) ----------
def carousel_cover(eyebrow_text, headline_html, sub, illustration):
    inner = f"""
    <div>
      <span class="eyebrow" style="font-size:24px">{eyebrow_text}</span>
      <h1 style="font-size:92px;margin-top:26px">{headline_html}</h1>
      <p class="body" style="font-size:30px;margin-top:28px">{sub}</p>
    </div>"""
    return frame(CW, CH, "96px 84px 84px", inner,
                 extra=illo(illustration, "right:70px;bottom:190px;width:300px;height:300px"),
                 with_swipe=True)

def carousel_numbered(n, title_html, sub, ill):
    inner = f"""
    <div style="max-width:900px;margin:0 auto;text-align:left">
      <div class="num" style="font-size:150px">0{n}</div>
      <h1 style="font-size:74px;margin-top:8px">{title_html}</h1>
      <p class="body" style="font-size:32px;margin-top:26px;max-width:22ch">{sub}</p>
    </div>"""
    return frame(CW, CH, "96px 84px 84px", inner,
                 extra=illo(ill, "right:70px;bottom:190px;width:280px;height:280px"))

def carousel_code(n, title_html, code_text, ill):
    inner = f"""
    <div style="max-width:900px;margin:0 auto">
      <div class="num" style="font-size:120px">0{n}</div>
      <h1 style="font-size:56px;margin-top:6px">{title_html}</h1>
      <div class="code" style="margin-top:32px">{code_text}</div>
    </div>"""
    return frame(CW, CH, "96px 84px 84px", inner,
                 extra=illo(ill, "right:70px;bottom:180px;width:220px;height:220px"))

def carousel_cta(headline_html, sub, keyword, ill="audit"):
    inner = f"""
    <div>
      <span class="eyebrow" style="font-size:24px">Say hello to less busywork</span>
      <h1 style="font-size:82px;margin-top:28px">{headline_html}</h1>
      <p class="body" style="font-size:34px;margin-top:30px;max-width:24ch">{sub}</p>
      <p style="font-size:36px;margin-top:26px;font-weight:700"><span class="hl">{keyword}</span></p>
    </div>"""
    return frame(CW, CH, "96px 84px 84px", inner, cls="slide--blue",
                 extra=illo(ill, "right:70px;bottom:180px;width:300px;height:300px"),
                 white_foot=True, handle=HANDLE_CTA)

def story_slide(eyebrow_text, headline_html, body, ill=None):
    ex = illo(ill, "right:70px;top:70%;transform:translateY(-50%);width:280px;height:280px") if ill else ""
    inner = f"""
    <div>
      <span class="eyebrow" style="font-size:26px">{eyebrow_text}</span>
      <h1 style="font-size:88px;margin-top:30px">{headline_html}</h1>
      <p class="body" style="font-size:32px;margin-top:40px;line-height:1.45;max-width:22ch">{body}</p>
    </div>"""
    return frame(SW, SH, "220px 84px 220px", inner, extra=ex)

def before_after(headline_html, before_label, before_body, before_num,
                 after_label, after_body, after_num, eyebrow_text="AI in real life"):
    inner = f"""
    <div>
      <span class="eyebrow" style="font-size:24px">{eyebrow_text}</span>
      <h1 style="font-size:60px;margin-top:22px">{headline_html}</h1>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:38px">
        <div style="background:#fff;border:2px solid var(--line);border-radius:28px;padding:32px;display:flex;flex-direction:column;min-height:340px">
          <div style="font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)">{before_label}</div>
          <div class="body" style="font-size:26px;margin-top:14px;line-height:1.45">{before_body}</div>
          <div style="margin-top:auto;font-family:'Poppins';font-weight:800;font-size:52px;color:var(--ink)">{before_num}</div>
        </div>
        <div style="background:var(--blue);color:#fff;border-radius:28px;padding:32px;display:flex;flex-direction:column;min-height:340px">
          <div style="font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:.9">{after_label}</div>
          <div style="font-size:26px;margin-top:14px;line-height:1.45;color:#eaf0fd">{after_body}</div>
          <div style="margin-top:auto;font-family:'Poppins';font-weight:800;font-size:52px">{after_num}</div>
        </div>
      </div>
    </div>"""
    return frame(1080, 1080, "80px 80px 66px", inner)

# ---------- Sample: a full carousel + story + before/after set ----------
# Reference set. Copy this file for a new week, keep the helpers, swap the
# content. The locked rules (frame, foot, illustration position) are inherited.
slides = {}

slides["01-carousel-cover.html"] = carousel_cover(
    "AI in real life",
    "3 tasks you can<br>hand to <span class=\"hl\">AI</span><br>this week",
    "Start with the one you dread most.",
    "tasks")

slides["02-carousel-item.html"] = carousel_numbered(
    1, 'Lead <span class="hl">follow-ups</span>',
    "A reply within 5 minutes, every time, not when someone remembers.", "send")

slides["03-carousel-item.html"] = carousel_numbered(
    2, 'Appointment <span class="hl">reminders</span>',
    "Fewer no-shows, zero effort from your team.", "calclock")

slides["04-carousel-item.html"] = carousel_numbered(
    3, 'First reply to <span class="hl">DMs</span>',
    "Nobody sits waiting while you are busy with a client.", "dms")

slides["05-carousel-cta.html"] = carousel_cta(
    "Want the list for<br>your <span class=\"hl\">business?</span>",
    "Comment AUDIT and we will send you where to start, free.",
    "Comment AUDIT")

slides["06-story.html"] = story_slide(
    "AI in real life",
    "What eats<br>most of your<br><span class=\"hl\">week?</span>",
    "Tap to vote: admin, follow-ups, phone tag. We automate the winner.",
    "clock")

slides["07-beforeafter.html"] = before_after(
    "Same task.<br>A fraction of the <span class=\"hl\">time.</span>",
    "Before, by hand",
    "Two people, most of two days, copy and paste, missed follow-ups.",
    "16 hrs",
    "After, automated",
    "One system, running on its own, correct every time.",
    "2 hrs")

for name,html in slides.items():
    open(name,"w",encoding="utf-8").write(html)
print("wrote", len(slides), "slides")
