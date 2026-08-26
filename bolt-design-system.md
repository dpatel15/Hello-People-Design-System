# Hello People, design system context for AI builders (bolt.new, v0, Lovable, Cursor)

Paste this whole file at the start of your prompt. It is everything an AI needs
to build screens that look, feel, and sound like Hello People. It is
self-contained: the exact tokens and component classes are included below, so the
tool does not have to fetch anything.

Hello People is an AI automation and growth studio. The brand promise:
**human on the surface, engineered underneath.** Tagline: *Say hello to less busywork.*

---

## 0. Non-negotiable rules (follow these every time)

1. **Never use an em dash or an en dash** anywhere in copy, code, or comments.
   Use a comma, colon, period, or parentheses instead, and write "to" for ranges
   (e.g. "Mon to Fri", "120 to 320ms"). A normal hyphen in words like "follow-up"
   is fine. This is a hard client rule.
2. **95 / 5 color.** About 95% flat neutrals plus **solid `--hp-blue`** doing the
   real work. The **gradient earns only ~5%**: reserve it for the logo, one hero
   moment, and the closing call-to-action band. Never use the gradient as a
   default background or on general buttons.
3. **Style with the semantic tokens** (`--hp-bg`, `--hp-text`, `--hp-surface`,
   `--hp-border`, `--hp-accent` ...), not raw hex. Semantic tokens adapt to
   light and dark automatically.
4. **Type:** Poppins for display/headings, Inter for body. Big, confident
   headlines with tight tracking. Generous whitespace, space is a feature.
5. **Voice:** plain and human. Sell the outcome, not the tech. No buzzwords.
6. **Primary button is solid blue** (`.hp-btn--primary`), never gradient.

---

## 1. Brand colors (for reference; use the tokens, not these hex values directly)

| Role | Light | Dark | Meaning |
|---|---|---|---|
| Link Blue (`--hp-blue`, the workhorse) | `#1D50CF` | `#3D6DE4` | trust, the tech |
| Bridge Violet (`--hp-violet`) | `#903DA4` | `#A84EBD` | machine meets human |
| People Magenta (`--hp-magenta`) | `#E0497C` | `#EC5C90` | warmth, humanity |
| Signature gradient | `linear-gradient(120deg,#1D50CF,#903DA4,#E0497C)` | (brightened) | logo + hero + CTA only |
| Ink / text | `#1B1E27` | `#F2F3F8` | primary text |

---

## 2. Setup (tell the tool to do this once)

**Fonts.** Load Poppins (600, 700, 800) and Inter (400, 500, 600) from Google
Fonts. In the HTML `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
```

**Styles.** Create two global CSS files, `tokens.css` then `components.css`
(exact contents in sections 4 and 5 below), and import them in that order before
any app styles. In a React/Vite bolt project, import them in `main.jsx`/`main.tsx`
or `index.css`:

```css
@import "./tokens.css";
@import "./components.css";
```

**Dark mode** works out of the box: it follows the OS setting, or you can force it
with `data-theme="dark"` / `data-theme="light"` on the `<html>` element.

---

## 3. How to use it

- Backgrounds: `var(--hp-bg)` (page), `var(--hp-surface)` (cards), `var(--hp-surface-2)` (alt sections).
- Text: `var(--hp-text)`, `var(--hp-text-strong)` (headings), `var(--hp-text-muted)` (secondary).
- Borders: `var(--hp-border)`. Accent: `var(--hp-accent)` (solid blue).
- Radius: `var(--hp-radius-md)` / `--hp-radius-lg` / `--hp-radius-xl`. Shadows: `var(--hp-shadow-sm/md/lg)`.
- Spacing scale: `var(--hp-space-1..12)` (4px base).

**Component classes** (from `components.css`):

```html
<!-- Buttons: primary is SOLID blue; gradient is CTA-band only -->
<a class="hp-btn hp-btn--primary">Book an audit</a>
<a class="hp-btn hp-btn--ghost">See what we automate</a>
<a class="hp-btn hp-btn--primary hp-btn--lg">Big call to action</a>

<!-- Eyebrow + heading -->
<span class="hp-eyebrow">What we do</span>
<h2>Two ways we give you your time back</h2>

<!-- Card -->
<div class="hp-card hp-card--interactive">
  <span class="hp-card__icon"><!-- 24px line icon --></span>
  <h3 class="hp-card__title">Workflow automation</h3>
  <p class="hp-card__body">The busywork runs on its own, correctly, every time.</p>
</div>

<!-- Badge, note, form field -->
<span class="hp-badge hp-badge--blue">Most popular</span>
<div class="hp-note hp-note--info">Heads up, this is an info note.</div>
<div class="hp-field">
  <label class="hp-label" for="email">Email</label>
  <input class="hp-input" id="email" type="email" placeholder="you@company.com">
</div>
```

**Icons:** use line icons on a 24px grid, 2px stroke, round caps,
`fill="none" stroke="currentColor"`. Lucide (lucide.dev) matches this exactly, so
tell the tool to use `lucide-react` and let icons inherit the text color.

---

## 4. tokens.css (paste as-is)

```css
/* =============================================================================
   HELLO PEOPLE DESIGN TOKENS
   Single source of truth for color, type, space, radius, elevation & motion.
   Everything downstream (components, site, decks) reads from these variables.
   Change a value here → it updates everywhere.

   Brand colors are read from the master logo SVG (Clod Design vectors):
     wordmark gradient  #1D50CF → #903DA4 → #E0497C
     ring (deep blue)   #0154B8
     "Hello" charcoal   #3F454C

   Layers:
   1. PRIMITIVES, raw brand values. Never reference these directly in UI.
   2. SEMANTIC, role-based tokens (bg, text, border…). Use THESE in UI.
   3. THEMING, semantic tokens re-mapped for dark mode.
   ============================================================================= */

:root {
  /* ---------------------------------------------------------------------------
     1. PRIMITIVES
     --------------------------------------------------------------------------- */

  /* Brand core, exact values from the logo */
  --hp-blue:        #1D50CF;   /* Link Blue, trust, intelligence, "the tech" */
  --hp-violet:      #903DA4;   /* Bridge Violet, where machine meets human */
  --hp-magenta:     #E0497C;   /* People Magenta, warmth, energy, humanity */

  /* Brand tints / shades (for hovers, fills, focus rings) */
  --hp-blue-800:    #0154B8;   /* deep ring blue */
  --hp-blue-700:    #123FA8;
  --hp-blue-600:    #1D50CF;
  --hp-blue-500:    #3A6BE0;
  --hp-blue-100:    #E4EAF9;
  --hp-magenta-700: #C43D6E;
  --hp-magenta-600: #E0497C;
  --hp-magenta-100: #FBE6EE;

  /* The signature gradient, ONE token, used everywhere, so it never drifts */
  --hp-gradient:        linear-gradient(120deg, #1D50CF 0%, #903DA4 52%, #E0497C 100%);
  --hp-gradient-135:    linear-gradient(135deg, #1D50CF 0%, #903DA4 52%, #E0497C 100%);
  --hp-gradient-soft:   linear-gradient(120deg, rgba(29,80,207,.12), rgba(144,61,164,.12), rgba(224,73,124,.12));
  --hp-gradient-text:   linear-gradient(120deg, #1D50CF, #903DA4, #E0497C);

  /* Neutrals, cool-biased (a hint of blue) so they read "chosen", not default grey */
  --hp-ink-950: #0C0D12;
  --hp-ink-900: #14161D;
  --hp-ink-800: #1B1E27;   /* primary text / dominant dark ground */
  --hp-ink-700: #2A2E39;
  --hp-ink-600: #3F454C;   /* the logo's "Hello" charcoal */
  --hp-ink-500: #565B6A;
  --hp-ink-400: #6B6F7D;   /* muted / secondary text */
  --hp-ink-300: #9195A3;
  --hp-ink-200: #C9CCD5;
  --hp-ink-150: #DDDFE7;
  --hp-ink-100: #E6E7EE;   /* hairline borders */
  --hp-ink-75:  #EFF0F4;
  --hp-ink-50:  #F4F4F8;   /* surface fills */
  --hp-ink-25:  #FAFAFC;   /* page paper */
  --hp-white:   #FFFFFF;

  /* Feedback (semantic status, distinct from the brand accent) */
  --hp-success: #12A150;
  --hp-success-bg: #E7F6EE;
  --hp-warning: #C77700;
  --hp-warning-bg: #FBF0DC;
  --hp-danger:  #E5484D;
  --hp-danger-bg: #FCE9E9;
  --hp-info:    #1D50CF;
  --hp-info-bg: #E4EAF9;

  /* ---------------------------------------------------------------------------
     TYPOGRAPHY
     --------------------------------------------------------------------------- */
  --hp-font-display: "Poppins", "Segoe UI", system-ui, -apple-system, sans-serif;
  --hp-font-body:    "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  --hp-font-mono:    "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;

  /* Type scale, 1rem base, ~1.25 (major third) */
  --hp-text-xs:   0.75rem;    /* 12 */
  --hp-text-sm:   0.875rem;   /* 14 */
  --hp-text-base: 1rem;       /* 16 */
  --hp-text-md:   1.125rem;   /* 18 */
  --hp-text-lg:   1.25rem;    /* 20 */
  --hp-text-xl:   1.5rem;     /* 24 */
  --hp-text-2xl:  1.875rem;   /* 30 */
  --hp-text-3xl:  2.25rem;    /* 36 */
  --hp-text-4xl:  3rem;       /* 48 */
  --hp-text-5xl:  3.75rem;    /* 60 */
  --hp-text-6xl:  4.5rem;     /* 72 */

  --hp-weight-regular:  400;
  --hp-weight-medium:   500;
  --hp-weight-semibold: 600;
  --hp-weight-bold:     700;
  --hp-weight-extra:    800;

  --hp-leading-tight:   1.12;
  --hp-leading-snug:    1.25;
  --hp-leading-normal:  1.55;
  --hp-leading-relaxed: 1.7;

  --hp-tracking-tight:  -0.02em;
  --hp-tracking-snug:   -0.01em;
  --hp-tracking-normal: 0;
  --hp-tracking-wide:   0.08em;
  --hp-tracking-caps:   0.16em;   /* uppercase eyebrows / labels */

  --hp-measure: 65ch;             /* comfortable reading width */

  /* ---------------------------------------------------------------------------
     SPACING, 4px base scale
     --------------------------------------------------------------------------- */
  --hp-space-0:  0;
  --hp-space-1:  0.25rem;   /* 4  */
  --hp-space-2:  0.5rem;    /* 8  */
  --hp-space-3:  0.75rem;   /* 12 */
  --hp-space-4:  1rem;      /* 16 */
  --hp-space-5:  1.5rem;    /* 24 */
  --hp-space-6:  2rem;      /* 32 */
  --hp-space-7:  2.5rem;    /* 40 */
  --hp-space-8:  3rem;      /* 48 */
  --hp-space-9:  4rem;      /* 64 */
  --hp-space-10: 5rem;      /* 80 */
  --hp-space-11: 6rem;      /* 96 */
  --hp-space-12: 8rem;      /* 128 */

  /* ---------------------------------------------------------------------------
     RADIUS
     --------------------------------------------------------------------------- */
  --hp-radius-xs:   6px;
  --hp-radius-sm:   10px;
  --hp-radius-md:   14px;
  --hp-radius-lg:   20px;
  --hp-radius-xl:   28px;
  --hp-radius-pill: 999px;

  /* ---------------------------------------------------------------------------
     ELEVATION, soft, cool-tinted shadows (never harsh black)
     --------------------------------------------------------------------------- */
  --hp-shadow-sm:  0 1px 2px rgba(20,22,34,.05), 0 1px 3px rgba(20,22,34,.05);
  --hp-shadow-md:  0 2px 6px rgba(20,22,34,.06), 0 8px 24px rgba(20,22,34,.07);
  --hp-shadow-lg:  0 4px 12px rgba(20,22,34,.08), 0 24px 56px rgba(20,22,34,.10);
  --hp-shadow-brand: 0 6px 18px rgba(29,80,207,.18), 0 18px 48px rgba(224,73,124,.14);

  /* ---------------------------------------------------------------------------
     MOTION
     --------------------------------------------------------------------------- */
  --hp-ease:        cubic-bezier(.2, .7, .3, 1);   /* calm, confident */
  --hp-ease-out:    cubic-bezier(0, 0, .2, 1);
  --hp-duration-1:  120ms;
  --hp-duration-2:  200ms;
  --hp-duration-3:  320ms;

  /* Layout */
  --hp-container:   1120px;
  --hp-container-narrow: 760px;

  /* ---------------------------------------------------------------------------
     2. SEMANTIC TOKENS (LIGHT), use these in UI, not the primitives above
     --------------------------------------------------------------------------- */
  --hp-bg:            var(--hp-ink-25);
  --hp-bg-elevated:   var(--hp-white);
  --hp-surface:       var(--hp-white);
  --hp-surface-2:     var(--hp-ink-50);
  --hp-surface-inset: var(--hp-ink-75);

  --hp-text:          var(--hp-ink-800);
  --hp-text-strong:   var(--hp-ink-900);
  --hp-text-muted:    var(--hp-ink-400);
  --hp-text-subtle:   var(--hp-ink-300);
  --hp-text-on-brand: var(--hp-white);

  --hp-border:        var(--hp-ink-100);
  --hp-border-strong: var(--hp-ink-200);

  --hp-accent:        var(--hp-blue);
  --hp-accent-hover:  var(--hp-blue-800);
  --hp-accent-quiet:  var(--hp-blue-100);
  --hp-focus-ring:    color-mix(in srgb, var(--hp-blue) 45%, transparent);
}

/* ---------------------------------------------------------------------------
   3. THEMING, dark mode  (values from the on-dark-bright logo variant)
   Order matters: OS-dark first (guarded so an explicit light choice wins),
   then explicit [data-theme="dark"] so the toggle wins in both directions.
   Only tokens are re-mapped here; components never restyle inside these blocks.
   --------------------------------------------------------------------------- */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --hp-blue:    #3D6DE4;
    --hp-violet:  #A84EBD;
    --hp-magenta: #EC5C90;
    --hp-gradient:      linear-gradient(120deg, #3D6DE4 0%, #A84EBD 52%, #E0497C 100%);
    --hp-gradient-soft: linear-gradient(120deg, rgba(61,109,228,.16), rgba(168,78,189,.16), rgba(224,73,124,.16));
    --hp-gradient-text: linear-gradient(120deg, #3D6DE4, #A84EBD, #EC5C90);

    --hp-bg:            var(--hp-ink-950);
    --hp-bg-elevated:   var(--hp-ink-900);
    --hp-surface:       #20242E;
    --hp-surface-2:     #191C24;
    --hp-surface-inset: #272C37;

    --hp-text:          #F2F3F8;
    --hp-text-strong:   #FFFFFF;
    --hp-text-muted:    #9195A3;
    --hp-text-subtle:   #6B6F7D;

    --hp-border:        #2F333E;
    --hp-border-strong: #3B4150;

    --hp-accent:        #3D6DE4;
    --hp-accent-hover:  #6188EC;
    --hp-accent-quiet:  rgba(61,109,228,.14);
    --hp-focus-ring:    color-mix(in srgb, #3D6DE4 55%, transparent);

    --hp-shadow-sm:  0 1px 2px rgba(0,0,0,.4);
    --hp-shadow-md:  0 2px 8px rgba(0,0,0,.45), 0 10px 30px rgba(0,0,0,.4);
    --hp-shadow-lg:  0 4px 14px rgba(0,0,0,.5), 0 26px 60px rgba(0,0,0,.5);
    --hp-shadow-brand: 0 6px 22px rgba(61,109,228,.35), 0 20px 55px rgba(224,73,124,.22);

    --hp-success-bg: rgba(18,161,80,.14);
    --hp-warning-bg: rgba(199,119,0,.16);
    --hp-danger-bg:  rgba(229,72,77,.16);
    --hp-info-bg:    rgba(61,109,228,.14);
  }
}

:root[data-theme="dark"] {
  --hp-blue:    #3D6DE4;
  --hp-violet:  #A84EBD;
  --hp-magenta: #EC5C90;
  --hp-gradient:      linear-gradient(120deg, #3D6DE4 0%, #A84EBD 52%, #E0497C 100%);
  --hp-gradient-soft: linear-gradient(120deg, rgba(61,109,228,.16), rgba(168,78,189,.16), rgba(224,73,124,.16));
  --hp-gradient-text: linear-gradient(120deg, #3D6DE4, #A84EBD, #EC5C90);

  --hp-bg:            var(--hp-ink-950);
  --hp-bg-elevated:   var(--hp-ink-900);
  --hp-surface:       #20242E;
  --hp-surface-2:     #191C24;
  --hp-surface-inset: #272C37;

  --hp-text:          #F2F3F8;
  --hp-text-strong:   #FFFFFF;
  --hp-text-muted:    #9195A3;
  --hp-text-subtle:   #6B6F7D;

  --hp-border:        #2F333E;
  --hp-border-strong: #3B4150;

  --hp-accent:        #3D6DE4;
  --hp-accent-hover:  #6188EC;
  --hp-accent-quiet:  rgba(61,109,228,.14);
  --hp-focus-ring:    color-mix(in srgb, #3D6DE4 55%, transparent);

  --hp-shadow-sm:  0 1px 2px rgba(0,0,0,.4);
  --hp-shadow-md:  0 2px 8px rgba(0,0,0,.45), 0 10px 30px rgba(0,0,0,.4);
  --hp-shadow-lg:  0 4px 14px rgba(0,0,0,.5), 0 26px 60px rgba(0,0,0,.5);
  --hp-shadow-brand: 0 6px 22px rgba(61,109,228,.35), 0 20px 55px rgba(224,73,124,.22);

  --hp-success-bg: rgba(18,161,80,.14);
  --hp-warning-bg: rgba(199,119,0,.16);
  --hp-danger-bg:  rgba(229,72,77,.16);
  --hp-info-bg:    rgba(61,109,228,.14);
}
```

---

## 5. components.css (paste as-is)

```css
/* =============================================================================
   HELLO PEOPLE COMPONENTS
   Reusable UI classes built entirely on tokens.css. Prefix: .hp-
   Load order:  tokens.css  →  components.css
   Rule of the system: solid --hp-blue is the workhorse; the gradient is
   reserved for the logo, one hero moment, and the closing CTA band.
   ============================================================================= */

/* ---------------------------------------------------------------- Primitives */
.hp-eyebrow{
  font-family:var(--hp-font-body);font-size:var(--hp-text-xs);font-weight:700;
  letter-spacing:var(--hp-tracking-caps);text-transform:uppercase;color:var(--hp-text-muted);
}
.hp-grad-text{
  background:var(--hp-gradient-text);-webkit-background-clip:text;background-clip:text;color:transparent;
}

/* --------------------------------------------------------------------- Button */
.hp-btn{
  display:inline-flex;align-items:center;justify-content:center;gap:.55em;
  font-family:var(--hp-font-body);font-weight:600;font-size:.98rem;line-height:1;
  padding:.8em 1.4em;border-radius:var(--hp-radius-md);border:1px solid transparent;
  cursor:pointer;text-decoration:none;white-space:nowrap;
  transition:transform var(--hp-duration-2) var(--hp-ease),
             box-shadow var(--hp-duration-2) var(--hp-ease),
             background var(--hp-duration-2) var(--hp-ease);
}
.hp-btn:focus-visible{outline:3px solid var(--hp-focus-ring);outline-offset:2px}
.hp-btn[disabled],.hp-btn.is-disabled{opacity:.5;pointer-events:none}
.hp-btn .hp-btn__arrow{transition:transform var(--hp-duration-2) var(--hp-ease)}
.hp-btn:hover .hp-btn__arrow{transform:translateX(3px)}

.hp-btn--primary{background:var(--hp-blue);color:#fff;box-shadow:0 8px 20px rgba(29,80,207,.22)}
.hp-btn--primary:hover{transform:translateY(-2px);background:var(--hp-blue-800)}
.hp-btn--ghost{background:var(--hp-surface);color:var(--hp-text-strong);border-color:var(--hp-border-strong)}
.hp-btn--ghost:hover{transform:translateY(-2px);box-shadow:var(--hp-shadow-md)}
.hp-btn--subtle{background:var(--hp-accent-quiet);color:var(--hp-accent)}
.hp-btn--subtle:hover{transform:translateY(-2px)}
.hp-btn--white{background:#fff;color:#14161D}
.hp-btn--white:hover{transform:translateY(-2px)}
/* Gradient button, CTA band ONLY. Do not use in general UI. */
.hp-btn--gradient{background:var(--hp-gradient);color:#fff;box-shadow:var(--hp-shadow-brand)}
.hp-btn--gradient:hover{transform:translateY(-2px)}

.hp-btn--sm{font-size:.86rem;padding:.6em 1em;border-radius:var(--hp-radius-sm)}
.hp-btn--lg{font-size:1.06rem;padding:.95em 1.7em}
.hp-btn--block{display:flex;width:100%}

/* ---------------------------------------------------------------- Icon button */
.hp-icon-btn{
  width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;
  border-radius:var(--hp-radius-sm);border:1px solid var(--hp-border);background:var(--hp-surface);
  color:var(--hp-text);cursor:pointer;transition:box-shadow var(--hp-duration-2) var(--hp-ease)}
.hp-icon-btn:hover{box-shadow:var(--hp-shadow-sm)}
.hp-icon-btn:focus-visible{outline:3px solid var(--hp-focus-ring);outline-offset:2px}

/* --------------------------------------------------------------- Badge / Pill */
.hp-badge{
  display:inline-flex;align-items:center;gap:.4em;font-family:var(--hp-font-body);
  font-size:var(--hp-text-xs);font-weight:600;line-height:1;padding:.42em .7em;
  border-radius:var(--hp-radius-pill);border:1px solid transparent}
.hp-badge--blue{background:var(--hp-accent-quiet);color:var(--hp-accent)}
.hp-badge--muted{background:var(--hp-surface-2);color:var(--hp-text-muted);border-color:var(--hp-border)}
.hp-badge--success{background:var(--hp-success-bg);color:var(--hp-success)}
.hp-badge--warning{background:var(--hp-warning-bg);color:var(--hp-warning)}
.hp-badge--danger{background:var(--hp-danger-bg);color:var(--hp-danger)}
.hp-badge--outline{background:transparent;color:var(--hp-text);border-color:var(--hp-border-strong)}
.hp-badge--dot::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor}

/* ------------------------------------------------------------------ Card */
.hp-card{
  background:var(--hp-surface);border:1px solid var(--hp-border);
  border-radius:var(--hp-radius-lg);box-shadow:var(--hp-shadow-sm);padding:var(--hp-space-6)}
.hp-card--interactive{transition:transform var(--hp-duration-3) var(--hp-ease),box-shadow var(--hp-duration-3) var(--hp-ease)}
.hp-card--interactive:hover{transform:translateY(-4px);box-shadow:var(--hp-shadow-lg)}
.hp-card--flat{box-shadow:none}
.hp-card__icon{
  width:46px;height:46px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;
  background:var(--hp-accent-quiet);color:var(--hp-accent);margin-bottom:var(--hp-space-4)}
.hp-card__title{font-family:var(--hp-font-display);font-size:var(--hp-text-lg);font-weight:600;
  color:var(--hp-text-strong);margin:0 0 .4em}
.hp-card__body{color:var(--hp-text-muted);font-size:.96rem;margin:0}

/* ------------------------------------------------------------------ Forms */
.hp-field{display:flex;flex-direction:column;gap:.5em}
.hp-label{font-size:var(--hp-text-sm);font-weight:600;color:var(--hp-text)}
.hp-label .hp-req{color:var(--hp-danger)}
.hp-input,.hp-textarea,.hp-select{
  font-family:var(--hp-font-body);font-size:1rem;color:var(--hp-text);
  background:var(--hp-surface);border:1px solid var(--hp-border-strong);
  border-radius:var(--hp-radius-md);padding:.7em .9em;width:100%;
  transition:border-color var(--hp-duration-2) var(--hp-ease),box-shadow var(--hp-duration-2) var(--hp-ease)}
.hp-input::placeholder,.hp-textarea::placeholder{color:var(--hp-text-subtle)}
.hp-input:focus,.hp-textarea:focus,.hp-select:focus{
  outline:none;border-color:var(--hp-accent);box-shadow:0 0 0 3px var(--hp-focus-ring)}
.hp-textarea{min-height:120px;resize:vertical}
.hp-field--error .hp-input,.hp-field--error .hp-textarea{border-color:var(--hp-danger)}
.hp-help{font-size:var(--hp-text-sm);color:var(--hp-text-muted)}
.hp-field--error .hp-help{color:var(--hp-danger)}

/* ------------------------------------------------------------------ Note / Callout */
.hp-note{
  display:flex;gap:.75em;padding:var(--hp-space-4) var(--hp-space-5);
  border-radius:var(--hp-radius-md);border:1px solid var(--hp-border);
  background:var(--hp-surface-2);color:var(--hp-text);font-size:.95rem}
.hp-note--info{background:var(--hp-info-bg);border-color:transparent}
.hp-note--success{background:var(--hp-success-bg);border-color:transparent}
.hp-note--warning{background:var(--hp-warning-bg);border-color:transparent}
.hp-note--danger{background:var(--hp-danger-bg);border-color:transparent}
.hp-note__title{font-weight:600;margin:0 0 .2em}

/* ------------------------------------------------------------------ Divider */
.hp-divider{height:1px;background:var(--hp-border);border:0;margin:var(--hp-space-6) 0}

/* ------------------------------------------------------------------ Layout helpers */
.hp-container{width:100%;max-width:var(--hp-container);margin-inline:auto;padding-inline:var(--hp-space-5)}
.hp-stack{display:flex;flex-direction:column}
.hp-cluster{display:flex;flex-wrap:wrap;align-items:center;gap:var(--hp-space-3)}
```

---

## 6. A ready-to-use starter prompt for bolt.new

Copy everything above (sections 0 to 5), then add a line like this at the end:

> Using the Hello People design system above, set up `tokens.css` and
> `components.css` exactly as given and import them globally, load Poppins and
> Inter from Google Fonts, and use only the semantic `--hp-` variables and `.hp-`
> classes for styling. Solid `--hp-blue` is the primary color; use the gradient
> only for the logo and one closing call-to-action band. Never use em or en
> dashes. Now build me: **[describe the screen or app you want]**.

The tokens and components are also hosted (public) if you prefer to link them:

- `https://cdn.jsdelivr.net/gh/dpatel15/Hello-People-Design-System/tokens/tokens.css`
- `https://cdn.jsdelivr.net/gh/dpatel15/Hello-People-Design-System/components/components.css`
