# Hello People project memory

## Writing rules (IMPORTANT, applies to all copy, code comments, commits, and chat)

- **Never use the em dash ", " or the en dash "-"** anywhere: website copy, docs,
  code comments, commit messages, or replies. The client finds them
  AI-generated. This is a hard rule.
- Instead, use a **comma, colon, period, or parentheses** to break a sentence,
  and write **"to"** for ranges (e.g. "Mon to Fri", "120 to 320ms"). A plain
  hyphen "-" in compound words (follow-ups, on-brand) is fine.
- Keep sentences plain and human. See `brand/voice-and-tone.md`.

## What this repo is

The Hello People design system: brand guidelines (`brand/`), design tokens
(`tokens/`), a component library (`components/components.css`), and pages built on
them (`web/`). Brand rule: solid `--hp-blue` does the work; the gradient is
reserved for the logo, one hero moment, and the closing CTA band (95/5).

## Build notes

- The pages in `web/` are self-contained (embedded fonts + logos). They are
  assembled from templates in the working scratchpad by injecting
  `fonts-embedded.css`, `tokens/tokens.css`, `components/components.css`, and the
  logo SVGs as data URIs. Edit the source token/component/brand files, then
  rebuild the pages so they stay in sync.
- Verify visual changes by rendering with the pre-installed Chromium (Playwright)
  before committing.
- Develop on branch `claude/hello-people-design-system-9vjla5`.
