# Hello People, social slide system

Generates on-brand social visuals (feed posts, stories, carousels, data cards)
straight from the design system, so every post looks like us with no manual
design work. Pairs with the copy engine in `../social-automation.md`.

## Run it

```bash
cd social
python3 generate.py      # writes the slide HTML
node render.cjs          # renders each to PNG at native size (2x)
```

Assets are pulled from the canonical design system (no copies):
fonts (`../assets/fonts/hello-people-fonts-social.css`), the warped-grid
background (`../assets/social/backgrounds/hello-people-bg-grid-ribbons.svg`), and
the logo (`../assets/logo/`). Example output lives in
`../assets/social/examples/`.

## Formats

| Slide | Size |
|---|---|
| Instagram feed post | 1080 x 1080 |
| Instagram story | 1080 x 1920 (safe zone: keep content clear of top/bottom ~300px) |
| Carousel (cover, content, CTA) | 1080 x 1350 |
| Before / after data card | 1080 x 1080 |

## Locked visual rules (the standard, do not drift)

1. **Warped grid background** with a soft center wash for legible text.
2. **Poppins 800 headline**, key words in a solid-blue highlight block (`.hl`);
   white highlight on the blue CTA slide. Body in Inter.
3. **Contextual line illustration** to fill an empty band, one per slide, matching
   that slide's message. Skip it where the slide is already full.
   - **stroke width: 0.3px** (fine hairline)
   - **opacity: 15%**, the same on light and dark slides
   - drawn in the brand icon language (24px grid, rounded), brand blue on light,
     white on blue.
4. **95 / 5 color:** solid blue does the work; the gradient stays a cover-only
   treat. Every slide signs off with the logo and `@hellopeople_agency`.
5. **Copy** follows `../brand/voice-and-tone.md`: plain, human, **no em or en
   dashes**, one idea per slide, a lead-focused CTA.

## Adding a new illustration

Add a path to the `P{}` dictionary in `generate.py`, keyed by topic (a Lucide-style
24px line icon works perfectly), then reference it with `illo("name", "...position")`.
It automatically inherits the 0.3px / 15% treatment.
