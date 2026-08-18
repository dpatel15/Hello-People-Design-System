# Hello People Design System

**Say hello to less busywork.**

The single source of truth for the Hello People brand and product, so everything
we make (website, social, decks, product UI) looks, sounds, and feels like *us*.

> **Human on the surface. Engineered underneath.** We're the warm face on powerful
> automation, and this system exists to keep that promise consistent everywhere.

---

## What's here

```
Hello-People-Design-System/
├── README.md                     ← you are here
├── brand/                        ← the guidelines (the "why" + rules)
│   ├── foundation.md             ← the idea, personality, taglines, how people should FEEL
│   ├── visual-language.md        ← color & type meaning, the 95/5 rule, space, motion
│   ├── voice-and-tone.md         ← how we write
│   └── logo.md                   ← logo usage, clear space, don'ts
├── tokens/                       ← the machine-readable design decisions
│   ├── tokens.css                ← CSS custom properties (use these in code)
│   └── tokens.json               ← platform-agnostic tokens (Figma / Tailwind / native)
├── components/
│   └── components.css            ← reusable UI classes (.hp-btn, .hp-card, .hp-badge…)
├── web/                          ← pages built on the system (self-contained)
│   ├── index.html                ← flagship homepage
│   ├── guidelines.html           ← living, interactive style guide (open this!)
│   ├── social.html               ← social templates, minimal kit
│   └── social-structured.html    ← social templates, structured kit (warped grid)
└── assets/
    ├── fonts/hello-people-fonts.css  ← embedded Poppins + Inter (offline-ready)
    └── logo/                     ← the logo, in vector
        ├── hello-people-logo.svg / -dark / -white / -black
        ├── hello-people-mark.svg / -dark / -white / -black
        └── hello-people-favicon.svg / -dark
```

---

## Quick start (for code)

```html
<link rel="stylesheet" href="tokens/tokens.css">
<link rel="stylesheet" href="components/components.css">
<!-- then use the classes -->
<a class="hp-btn hp-btn--primary">Book an audit</a>
<div class="hp-card">…</div>
```

Or build your own on the tokens (primary is **solid blue**, not gradient):

```css
.button-primary {
  background: var(--hp-blue);          /* solid, gradient is reserved */
  color: #fff;
  border-radius: var(--hp-radius-md);
  font-family: var(--hp-font-body);
}
```

**Rule:** style with the **semantic** tokens (`--hp-bg`, `--hp-text`, `--hp-border`,
`--hp-accent`…), not the raw primitives. Semantic tokens adapt to light/dark
automatically. Dark mode works out of the box (OS setting) or via
`data-theme="dark"` / `data-theme="light"` on `<html>`.

Fonts to load: **Poppins** (600/700/800) + **Inter** (400/500/600).

---

## The three rules that keep it premium

1. **95 / 5 color**, ~95% flat neutrals + solid blue; the gradient earns ~5%.
2. **Space is a feature**, when unsure, add more.
3. **Sell the outcome, not the tech**, plain, human words. See `voice-and-tone.md`.

---

## Roadmap

- [x] Brand foundation, voice & tone, visual language
- [x] Design tokens (CSS + JSON), matched to the master logo
- [x] Logo, master vectors (light / dark / mono / mark / favicon)
- [x] Homepage, flagship page built on the system (light/dark)
- [x] Component library, buttons, cards, badges, forms, notes (`components/components.css`)
- [x] Living guidelines site, interactive style guide (`web/guidelines.html`)
- [x] Social media system, two families (minimal + structured), 11 templates,
      reusable warped-grid background SVGs (`web/social*.html`, `assets/social/`)
- [ ] Proposal & deck template
- [ ] Refactor homepage onto `components.css` classes

---

## Status

`v0.3`, foundation, tokens, master logo, flagship homepage, component library,
and a living guidelines site. Next: social templates + proposal/deck.

*Contributions follow the brand rules above, if it doesn't serve them, it doesn't ship.*
