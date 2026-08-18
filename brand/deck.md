# Hello People Deck

The presentation system: a library of on-brand slide types with a real narrative
flow. Template: `web/deck.html`. Overview: `assets/deck/_overview.png`.

Every slide shares the same type scale, spacing, footer, and color, so a client
feels **one consistent brand** from cover to close. Swap the copy and numbers per
deck, then **print to PDF** (16:9, 1280 x 720) to send.

## Slide types (24)

**Openers**
1. Cover (dark, gradient accent)
2. Agenda / contents
3. / 10. / 18. Section dividers (dark and gradient)

**Narrative**
4. Bullets
5. Big statement (one bold line, highlighter)
16. Quote / testimonial
17. Full-bleed statement (dark, soft gradient glow)

**Data**
6. Data table
7. Bar chart (magnitude, single blue hue)
8. Big stat (one hero number)
9. Stats row (3 KPIs)
14. Line chart (change over time, area fill, emphasized endpoint)
15. Donut / progress
13. Before / after

**The offer**
11. Feature cards
12. Two-column + illustration (workflow graphic)
19. Scope (steps)
20. Timeline (steps)
21. Investment (pricing)

**Proof & close**
22. Team / about
23. Trusted by (logo strip)
24. Close CTA (gradient)

## Chart rules (kept simple and on-brand)

- **Magnitude uses one hue** (brand blue). No rainbow, no dual axes.
- Thin marks, rounded bar ends, a recessive grid, and **values in ink** (never in
  the series color). One accent (the gradient) only where it earns attention.
- Charts are plain inline SVG: edit the numbers directly in `web/deck.html`
  (bar heights, the line `points`, the donut `stroke-dasharray`). Each chart has a
  short comment or obvious values to change.
- Need more than one category with color? Use the fixed order blue, magenta,
  violet, and stop at four; beyond that, facet or group into "Other".

## Flow guidance

Open, frame the problem, prove it with the audit and data, show the plan and the
impact, make working together concrete (scope / timeline / investment), build
trust (quote / team / logos), then ask for the yes. Use a **section divider**
between the major acts so the client always knows where they are.

## Placeholders to swap

`[Client Name]`, `[Company]`, `[Date]`, `[Name]`, the `$[X,XXX]` / `$[XXX]`
prices, and the chart numbers. Everything else is brand-locked.
