# Hello People, social slide system

Generates on-brand social visuals (feed posts, stories, carousels, data cards)
straight from the design system, so every post looks like us with no manual
design work. Pairs with the copy engine in `../social-automation.md`.

## Run it

```bash
cd social
python3 generate.py                          # writes the slide HTML
node render.cjs                              # renders each to PNG at 2x

# Build a self-contained review board for a weekly output folder:
python3 build_week_viewer.py <week-dir> <jszip.min.js>
# and a slim printable/emailable PDF:
python3 build_week_printable.py <week-dir>
```

Assets are pulled from the canonical design system (no copies):
fonts (`../assets/fonts/hello-people-fonts-social.css`), the warped-grid
background (`../assets/social/backgrounds/hello-people-bg-grid-ribbons.svg`), and
the logo (`../assets/logo/`). Example output lives in
`../assets/social/examples/`.

## Formats (IG-native only)

| Slide | Size |
|---|---|
| Instagram feed post | 1080 x 1080 |
| Instagram story | 1080 x 1920 (safe zone: keep content clear of top/bottom ~300px) |
| Carousel (cover, content, CTA) | 1080 x 1350 |
| Before / after data card | 1080 x 1080 |
| Reel cover (Instagram thumbnail) | 1080 x 1920, centered layout: eyebrow tag centered on top, big Poppins hook centered under it, big photo cutout of founder in the middle, subheading centered below, logo + handle centered at the bottom. One hero photo used across a whole week for recognition. |

## Locked visual rules (the standard, do not drift)

1. **Warped grid background** with a soft center wash for legible text.
2. **Poppins 800 headline**, key words in a solid-blue highlight block (`.hl`);
   white highlight on the blue CTA slide. Body in Inter.
3. **Vertical alignment: center-then-expand.** Content sits vertically centered
   in the space between the top padding and the pinned bottom footer. Short
   content stays middle, longer content grows outward from the middle. Never
   top-anchor content just because there is empty room below. Covers keep the
   "Swipe" cue at the bottom-left so the hook signal stays.
4. **Logo on every slide; handle splits by role.** The Hello People logo mark
   appears at the bottom of every slide. The handle text splits:
   - **Regular slides** (cover, numbered content, code, story) sign off with
     `@dhairyapatel.official` (personal, where reach lives).
   - **CTA slides and lead-magnet PDF footer** sign off with `@hellopeople.ca`
     (company, where the lead lands).
   White logo variant on the blue CTA slide.
5. **Contextual line illustration** to fill an empty band, one per slide,
   matching that slide's message. On carousels, anchor it to the LOWER band
   (roughly `bottom: 180-190px`) so it never sits next to or behind the copy.
   Stories keep their own placement. Skip it where the slide is already full
   (e.g. the before/after data card).
   - **stroke width: 0.3px** (fine hairline)
   - **opacity: 15%**, the same on light and dark slides
   - drawn in the brand icon language (24px grid, rounded), brand blue on
     light, white on blue.
6. **95 / 5 color:** solid blue does the work; the gradient stays a
   cover-only treat.
7. **Grid rhythm: white, white, BLUE.** Instagram shows posts in a 3-column
   grid. To make the profile grid read as calm, calm, punch, every third
   carousel COVER is the solid brand-blue variant (the CTA-style look); the
   two before it are the standard warped-grid white with blue accents.
   Repeat down the grid. Stories do not participate. For a 7-day posting
   week, plan the day order so positions 3 and 6 hold content that earns the
   attention (Prove/case-study or Invite/lead-magnet days).
7. **Copy** follows `../brand/voice-and-tone.md`: plain, human, **no em or en
   dashes**, one idea per slide, a lead-focused CTA.

## Weekly output (downloadability)

The weekly viewer built by `build_week_viewer.py` embeds every full-resolution
image as a data URI. Every image is one-click downloadable, and a "Download all
images (ZIP)" button at the top of the page packages the whole week (JSZip
embedded inline, works offline in any browser).

`build_week_printable.py` produces a slim (~1-2 MB) printable/emailable PDF of
the same week: thumbnails + all copy + all reel scripts. Full-res images stay
in `weeks/<date>/images/` and are downloadable from `week.html`.

## Adding a new illustration

Add a path to the `P{}` dictionary in `generate.py`, keyed by topic (a
Lucide-style 24px line icon works perfectly), then reference it with
`illo("name", "...position")`. It automatically inherits the 0.3px / 15%
treatment.
