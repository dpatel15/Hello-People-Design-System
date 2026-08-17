# Hello People — Visual Language

How color, type, space, and motion do their emotional job. Pairs with
`foundation.md` (the strategy) and `../tokens/tokens.css` (the exact values).

---

## Color

We use **three brand colors on a large, calm neutral canvas.** The neutrals are
the brand as much as the gradient is — restraint is the point.

### What each color says

| Color | Token | Feels like | Use for |
|---|---|---|---|
| **Link Blue** `#1D50CF` | `--hp-blue` | Trust, intelligence, stability. "The tech is solid." | Primary actions, links, active states, focus rings, data/UI. The default brand color when you need *one*. |
| **Bridge Violet** `#903DA4` | `--hp-violet` | Transition, imagination, the meeting point. | Mostly *inside* the gradient. Rarely used solid. |
| **People Magenta** `#E0497C` | `--hp-magenta` | Warmth, energy, humanity. "There are people here." | Human touches — a highlight, an underline, the "." in the wordmark, one small emphasis per view. |
| **Ink** `#1B1E27` | `--hp-ink-800` | Grounded, premium, serious. | Headlines and the dominant dark ground. The logo's "Hello" uses a softer `#3F454C` (`--hp-ink-600`). |
| **Neutrals** `#6B6F7D → #FAFAFC` | `--hp-ink-*` | Calm, spacious, considered. | ~90% of every surface. Cool-biased so they feel chosen. |

> **Rule of thumb:** Blue does the *work*, Magenta adds the *warmth*, the gradient
> is the *signature moment*, and neutrals hold it all together.

### The signature gradient

`--hp-gradient` = `linear-gradient(120deg, #1D50CF, #903DA4, #E0497C)`

It runs **blue → violet → magenta**: cool to warm, machine to human. That
direction is the story — never reverse it arbitrarily. It lives in exactly one
token so it's identical on the site, a deck, and a social post.

**Where the gradient is allowed:**
- ✅ One primary CTA per screen
- ✅ A single hero accent (a headline word, a rule, a key icon/graphic)
- ✅ The logo's "AI" bubble and the "." in the wordmark
- ✅ A soft, low-opacity wash (`--hp-gradient-soft`) behind a feature block — sparingly

**Where it is banned:**
- ❌ Full-page or full-section solid gradient backgrounds
- ❌ On top of small body text (illegible; use it for display only)
- ❌ More than one strong gradient element competing in the same view

### The 90 / 10 rule

Roughly **90%** of any surface is flat — ink, paper, one solid color. The gradient
earns the other **~10%.** This single discipline is what separates a confident,
premium brand from the generic "AI slop" look. When in doubt, use less.

### Accessibility (non-negotiable)

- Body text meets **WCAG AA** (≥ 4.5:1). Ink `#1B1E27` on Paper `#FAFAFC` clears this easily.
- Magenta and Blue are for **large text, icons, and fills** — check contrast before using either for small text on white (magenta on white is borderline for body sizes).
- Never put small text directly on the gradient. White on the gradient is fine at display sizes.
- Color is never the *only* signal (pair with icon/label/weight).

---

## Typography

Two families, each with a clear job. This pairing was chosen to sound like the
brand: **warm and geometric** for display, **quiet and legible** for reading.

### Display — **Poppins**
Rounded, geometric, friendly. It echoes the logo's wordmark directly, so
headlines feel unmistakably "us." Used with restraint and tight tracking, Poppins
reads confident and modern, not childish.
- Weights: **700 (Bold)** for headlines, **600 (SemiBold)** for subheads.
- Tracking: slightly tight (`--hp-tracking-tight`) on large sizes.
- `text-wrap: balance` on headings.

### Body & UI — **Inter**
A neutral, highly legible workhorse built for screens. It gets out of the way and
lets the content (and the occasional Poppins headline) carry the personality.
- Weights: **400** body, **500/600** for UI labels and emphasis.
- Line length ~**65 characters** (`--hp-measure`); line-height `1.55–1.7` for text.

### Utility — **JetBrains Mono**
For code, tokens, metrics, and any "engineered" moment where monospace signals
precision. Optional, used lightly.

### Hierarchy rules
- One `h1` per page. Don't skip levels for looks.
- Uppercase **eyebrows/labels** get wide tracking (`--hp-tracking-caps`) and muted color.
- Numbers that line up in columns use `font-variant-numeric: tabular-nums`.
- Size and weight create hierarchy — **not** color. Save color for meaning.

### The type scale
Defined in tokens (`--hp-text-xs … --hp-text-6xl`, ~1.25 ratio). Stay on the
scale; don't invent one-off sizes.

---

## Space & layout

- **Space is a feature.** When unsure, add more. Crowding reads as cheap and anxious.
- 4px spacing scale (`--hp-space-*`). Compose spacing with flex/grid `gap`, not
  ad-hoc margins.
- Content column max ~`1120px`; reading text max ~`760px`.
- Align to a grid. Optical alignment beats mathematical when they disagree.

---

## Elevation & shape

- **Radius:** medium-soft (`--hp-radius-md` 14px is the default for cards/inputs;
  pill for chips/tags). Soft enough to feel human, tight enough to feel premium.
  Avoid `rounded-everything` and avoid hard 0px corners.
- **Shadows:** soft and cool-tinted (`--hp-shadow-*`), never harsh black. Use the
  brand-tinted shadow (`--hp-shadow-brand`) only under the primary gradient CTA.
- Prefer a **hairline border + subtle shadow** over heavy drop shadows.

---

## Motion

Calm and confident, never bouncy or attention-seeking.
- Standard easing `--hp-ease`; durations 120–320ms.
- Micro-interactions: a 1px lift + shadow on hover; smooth focus rings.
- Reveal-on-scroll is fine if subtle. **Always** honor `prefers-reduced-motion`.
- Motion should feel like *competence*, not decoration. If it draws attention to
  itself, cut it.

---

## Imagery & iconography (direction)

- **Photography:** real people, real workplaces, natural light. Candid over
  posed. Absolutely no glossy "robot handshake" or blue-glow-circuit stock.
- **Icons:** single-weight line icons (rounded joins to match Poppins). One set,
  consistent stroke. Occasional gradient fill for a hero icon only.
- **Graphics:** simple, geometric, lots of negative space. When we illustrate
  "automation," show *before → after / time saved*, not sci-fi abstractions.

---

*Visual Language v0.2 — colors matched exactly to the master logo SVG.*
