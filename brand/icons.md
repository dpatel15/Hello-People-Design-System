# Hello People Icons

Live browser: `web/icons.html` (searchable). Files in `assets/icons/`:

- `assets/icons/brand/` — 24 **custom Hello People icons** (prefixed `hp-`).
- `assets/icons/lucide/` — the **full [Lucide](https://lucide.dev) library**
  (2,025 icons, ISC-licensed, `LICENSE` included).

So every regularly-used icon is already in the repo, and they all share one look.

## Why this setup

We don't hand-draw a general icon library, we vendor Lucide (a mature, modern set
on a 24px grid with a 2px stroke) and add our own icons only for the concepts
Hello People sells. Because Lucide uses the same grid, our brand icons and the
library sit together seamlessly.

## The grid (non-negotiable)

- **24 x 24 viewBox**, **2px stroke**, **round caps and joins**, line style only.
- **`fill="none"`, `stroke="currentColor"`** so an icon inherits the surrounding
  text color and works in light, dark, and on solid blue with no edits.
- Resize the **whole icon**, never the stroke. Common sizes: 18, 20, 24, 28.

## Finding an icon

Open `web/icons.html` and search by name (e.g. "calendar", "phone", "chart"), or
browse `assets/icons/lucide/`. Every file is named for what it is.

## Our brand set

**Brand & domain (16):** `hp-workflow`, `hp-automate`, `hp-voice-agent`,
`hp-phone-agent`, `hp-chat-ai`, `hp-time-saved`, `hp-audit`, `hp-integration`,
`hp-reporting`, `hp-growth`, `hp-booking`, `hp-review`, `hp-email`, `hp-team`,
`hp-launch`, `hp-trust`.

**UI defaults (8):** `hp-arrow-right`, `hp-check`, `hp-close`, `hp-menu`,
`hp-chevron-right`, `hp-search`, `hp-external-link`, `hp-play` (curated favorites,
also available in Lucide).

## How to use

Inline the SVG (best, so `currentColor` and CSS work):

```html
<span class="icon" aria-hidden="true"><!-- paste the .svg contents --></span>
```

Or reference the file and control color via CSS mask:

```css
.icon{
  width:24px;height:24px;background:currentColor;
  -webkit-mask:url(assets/icons/lucide/calendar.svg) center/contain no-repeat;
          mask:url(assets/icons/lucide/calendar.svg) center/contain no-repeat;
}
```

At scale in a real app, install `lucide` (or `lucide-react` / `lucide-vue`) from
npm instead of copying files, and keep our brand icons alongside.

## Rules

1. **currentColor, not hardcoded.** Let the icon take the text color.
2. **Line, not fill.** Outline only. A single icon may take the brand gradient for
   one hero moment (like the logo bubble), never as the default.
3. **Pair icons with a label.** They support words, they do not replace them.
   Never use color alone to carry meaning.
4. **One weight.** Do not mix stroke widths. If an icon looks heavy, size it down.
5. **New brand icons match the grid** (24px / 2px), `hp-` prefix, into
   `assets/icons/brand/`.
