# Hello People Icons

Files in `assets/icons/` (24 SVGs). Live showcase: `web/icons.html`.

## The system

- **Base set: [Lucide](https://lucide.dev)** (MIT). Modern line icons on a 24px
  grid with a 2px stroke, hundreds of them. Use Lucide for any common UI or
  utility icon so we never reinvent the wheel.
- **Custom brand icons** (in `assets/icons/`, prefixed `hp-`): drawn on the same
  grid for the concepts Hello People sells, so services and features feel custom,
  not stock.

Everything shares one look, so Lucide and our icons sit together seamlessly.

## The grid (non-negotiable)

- **24 x 24 viewBox**, **2px stroke**, **round caps and joins**, line style only.
- **`fill="none"`, `stroke="currentColor"`** so the icon inherits the surrounding
  text color and works in light, dark, and on solid blue with no edits.
- Resize the **whole icon**, never the stroke. Common sizes: 18, 20, 24, 28.

## The set

**Brand & domain (16):** `hp-workflow`, `hp-automate`, `hp-voice-agent`,
`hp-phone-agent`, `hp-chat-ai`, `hp-time-saved`, `hp-audit`, `hp-integration`,
`hp-reporting`, `hp-growth`, `hp-booking`, `hp-review`, `hp-email`, `hp-team`,
`hp-launch`, `hp-trust`.

**UI & utility (8):** `hp-arrow-right`, `hp-check`, `hp-close`, `hp-menu`,
`hp-chevron-right`, `hp-search`, `hp-external-link`, `hp-play`.

## How to use

Inline the SVG (best, so `currentColor` and CSS work):

```html
<span class="icon" aria-hidden="true"><!-- paste hp-workflow.svg contents --></span>
```

Or reference the file and control color via CSS mask:

```css
.icon-workflow{
  width:24px;height:24px;background:currentColor;
  -webkit-mask:url(assets/icons/hp-workflow.svg) center/contain no-repeat;
          mask:url(assets/icons/hp-workflow.svg) center/contain no-repeat;
}
```

## Rules

1. **currentColor, not hardcoded.** Let the icon take the text color.
2. **Line, not fill.** Outline only. A single icon may take the brand gradient for
   one hero moment (like the logo bubble), never as the default.
3. **Pair icons with a label.** They support words, they do not replace them.
   Never use color alone to carry meaning.
4. **One weight.** Do not mix stroke widths. If an icon looks heavy next to text,
   size it down, do not thin the stroke.
5. **Add new brand icons to match.** New concepts get drawn on the 24px / 2px grid
   and dropped into `assets/icons/` with the `hp-` prefix.
