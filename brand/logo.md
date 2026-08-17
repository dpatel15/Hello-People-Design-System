# Hello People — Logo Guidelines

Files live in [`/assets/logo`](../assets/logo).

---

## The assets

| File | Use |
|---|---|
| `hello-people-logo.svg` | Primary horizontal lockup — for **light** backgrounds |
| `hello-people-logo-dark.svg` | Horizontal lockup — for **dark** backgrounds ("Hello" turns light) |
| `hello-people-mark.svg` | Icon only (the two speech bubbles) — avatars, favicons, app icons, tight spaces |

> **Status:** these SVGs are a faithful vector recreation of the supplied raster
> logo. When the final master SVG arrives, it replaces these files 1:1 and the
> wordmark text should be **converted to outlines** so it renders identically
> without Poppins installed. (Right now the wordmark uses live Poppins text.)

---

## Anatomy

- **The mark** — two speech bubbles: an open blue *ring* bubble (the human /
  listening) locking into a gradient *"AI"* bubble (the intelligence). Together
  they say "bridging humans and AI."
- **The wordmark** — **Hello** (ink/charcoal) stacked over **People.** (gradient),
  set in Poppins Bold. The **period is part of the logo** — it makes it a statement.

---

## Clear space & minimum size

- **Clear space:** keep padding around the logo equal to the height of the "H" in
  "Hello" on all sides. Nothing intrudes into it.
- **Minimum size:** horizontal lockup no smaller than **140px** wide (≈ 32px tall)
  on screen; the **mark** no smaller than **24px**. Below that, use the mark, not
  the lockup.

---

## Backgrounds

- On **light** backgrounds → `hello-people-logo.svg`.
- On **dark** backgrounds → `hello-people-logo-dark.svg`.
- On **photos or busy backgrounds** → place on a solid neutral chip/panel first,
  or use a single-color version (see below). Never let the gradient fight a busy image.
- Maintain contrast. If the mark's colors don't hold up, switch to mono.

---

## Single-color / mono (to be added)

For one-color contexts (engraving, faxable docs, a partner's dark UI, watermarks):
- **Mono dark:** entire logo in Ink `#1B1E27`.
- **Mono light:** entire logo in `#FFFFFF`.
- Keep the shapes; drop the gradient. *(Mono SVGs will be added to `/assets/logo`.)*

---

## Don'ts

- ❌ Don't recolor the gradient or swap the blue/magenta.
- ❌ Don't stretch, squash, rotate, or skew.
- ❌ Don't add drop shadows, outlines, or glows to the logo.
- ❌ Don't put the charcoal ("light") lockup on a dark background (use the dark file).
- ❌ Don't place the full-color logo on a busy photo without a neutral chip.
- ❌ Don't re-typeset the wordmark in a different font.
- ❌ Don't separate "People" from its period, or the mark's two bubbles.
- ❌ Don't crowd it — respect the clear space.

---

## Favicon / app icon

Use the **mark** (`hello-people-mark.svg`) on a Paper `#FAFAFC` (light) or Ink
`#0C0D12` (dark) rounded square. Keep generous padding so the bubbles don't touch
the edges.

---

*Logo Guidelines v0.1*
