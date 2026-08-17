# Hello People — Design System

**Say hello to less busywork.**

The single source of truth for the Hello People brand and product — so everything
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
│   ├── visual-language.md        ← color & type meaning, the 90/10 rule, space, motion
│   ├── voice-and-tone.md         ← how we write
│   └── logo.md                   ← logo usage, clear space, don'ts
├── tokens/                       ← the machine-readable design decisions
│   ├── tokens.css                ← CSS custom properties (use these in code)
│   └── tokens.json               ← platform-agnostic tokens (Figma / Tailwind / native)
└── assets/
    └── logo/                     ← the logo, in vector
        ├── hello-people-logo.svg        (light backgrounds)
        ├── hello-people-logo-dark.svg   (dark backgrounds)
        └── hello-people-mark.svg        (icon only)
```

---

## Quick start (for code)

```html
<link rel="stylesheet" href="tokens/tokens.css">
```

```css
.button-primary {
  background: var(--hp-gradient);
  color: var(--hp-text-on-brand);
  border-radius: var(--hp-radius-md);
  box-shadow: var(--hp-shadow-brand);
  font-family: var(--hp-font-display);
}
.card {
  background: var(--hp-surface);
  border: 1px solid var(--hp-border);
  border-radius: var(--hp-radius-md);
  box-shadow: var(--hp-shadow-md);
}
```

**Rule:** style with the **semantic** tokens (`--hp-bg`, `--hp-text`, `--hp-border`,
`--hp-accent`…), not the raw primitives. Semantic tokens adapt to light/dark
automatically. Dark mode works out of the box (OS setting) or via
`data-theme="dark"` / `data-theme="light"` on `<html>`.

Fonts to load: **Poppins** (600/700/800) + **Inter** (400/500/600).

---

## The three rules that keep it premium

1. **90 / 10 color** — ~90% flat neutrals + one solid color; the gradient earns ~10%.
2. **Space is a feature** — when unsure, add more.
3. **Sell the outcome, not the tech** — plain, human words. See `voice-and-tone.md`.

---

## Roadmap

- [x] Brand foundation, voice & tone, visual language
- [x] Design tokens (CSS + JSON) — matched to the master logo
- [x] Logo — master vectors (light / dark / mono / mark / favicon)
- [x] Homepage — flagship page built on the system
- [ ] Component library — buttons, cards, nav, forms, badges, sections (extracted from the homepage)
- [ ] Living guidelines site (interactive, hosted)
- [ ] Social media templates (IG / LinkedIn / ad creative)
- [ ] Proposal & deck template

---

## Status

`v0.2` — foundation + flagship homepage. Colors matched exactly to the master
logo SVG. Components get extracted from the homepage next.

*Contributions follow the brand rules above — if it doesn't serve them, it doesn't ship.*
