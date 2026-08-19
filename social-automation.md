# Hello People, daily social automation system

The engine that turns one topic a week into a full week of on-brand posts across
Instagram (feed + story), Facebook, LinkedIn, and X, aimed at engagement,
followers, and leads. Say hello to less busywork, including our own.

## The model: one brain, one publisher

We split the system in two, because generating and publishing have very
different needs.

**The brain (Claude, on a weekly rhythm).** Researches current topics, proposes
options, and once you pick one, writes the whole week of posts (copy per platform
plus a branded image from the design system) into a Google Sheet.

**The publisher (Metricool, daily).** Reads the approved week and posts each day
at 8am to every platform, including Instagram Stories.

Direct posting to Instagram, Facebook, and X needs an approved app or a paid API,
so we never post from a script. A proper scheduler does that leg reliably. We own
the part that is hard to do well: the ideas, the copy, and the brand.

## The weekly rhythm

| When | Who | What |
|---|---|---|
| Sun, 8am MT | Brain | Scan trends, drop 6 topic ideas plus a note on last week's best post |
| Sun | You | Reply with the topic number (or your own topic + optional reference file) |
| Sun | Brain | Generate the 7 day plan into the Google Sheet + render the images |
| Sun/Mon | You | Skim the week, edit anything, mark rows Approved (about 5 minutes) |
| Daily, 8am MT | Publisher | Metricool posts the day's content to all 5 placements |
| Fri | Brain | Pull the week's numbers, learn what worked, feed it into next week |

Review then publish is deliberate. One off-brand auto-post costs more than a five
minute skim.

## The Google Sheet (single source of truth)

One row per post. Columns:

`Date | Day | Theme | Angle | Platform | Format | Post copy | Hashtags | CTA | Visual / design note | Status`

- **Status** drives everything: `Draft` -> `Approved` -> `Scheduled` -> `Posted`.
- Metricool only picks up `Approved` rows.
- Import `hp-content-calendar-template.csv` to start; see
  `hp-content-week-ai-in-real-life.csv` for a full worked example week.

## Publisher setup (Metricool, one time)

Chosen because it is the one tool that covers all five placements, including
Instagram Stories, with bulk upload and analytics, and has a free tier.

1. Create a Metricool account and connect Instagram (business), Facebook page,
   LinkedIn (page + personal), and X.
2. Set the posting time to 8am America/Edmonton (Calgary).
3. Bulk-import the approved rows (CSV upload or the planner), or connect the
   Google Sheet through Make.com if you want it hands-off.
4. Confirm the first day in the preview, then let it run.

Alternative: Publer (also supports Stories, cheaper paid tier). Same workflow.

## Content rules (what makes a post ours)

- **Voice:** plain and human, sell the outcome, never the tech. No buzzwords.
  **No em or en dashes**, ever. See `brand/voice-and-tone.md`.
- **One idea per post.** If it needs two headlines, it is two posts.
- **Design:** build images from the social kit (`brand/social.md`,
  `web/social-structured.html`, `web/social.html`). Solid blue does the work; the
  gradient is a cover-only treat. Always sign off with the logo and
  `@hellopeople_agency`.
- **Every post earns its keep:** a hook in the first line, one clear idea, and a
  CTA that moves toward a lead (book an audit, comment a keyword, DM us).
- **Platform fit:** LinkedIn longer and professional, X short and punchy, IG
  visual with a save-worthy hook, Stories interactive (poll or question), FB
  warm and plain.

## The weekly generation prompt (what the brain runs)

> You are the Hello People social engine. Theme world: AI in real life (practical,
> real-world AI for busy teams). Audience: small and mid business owners and ops
> leads. Topic for this week: [TOPIC]. Reference: [optional file].
>
> Produce a 7 day plan, one row per platform per day, for Instagram feed,
> Instagram story, Facebook, LinkedIn, and X. Each day is a distinct angle on the
> topic (educational, before/after, how-to, objection, proof/case, relatable,
> reflection). Follow the Hello People voice and the no-dash rule. Every post
> gets a hook, one idea, hashtags (more for IG, few for LinkedIn, one or two for
> X), a lead-focused CTA, and a design note referencing the social kit. Output as
> the Google Sheet columns and render one branded image per day.

## What we measure (so it actually drives leads)

- **Reach and saves/shares** (did it travel?)
- **Follower growth** (are we compounding?)
- **Profile clicks, link clicks, DMs, comment keywords** (intent)
- **Audits booked** (the only number that pays the bills)

Each Friday we keep what worked, cut what did not, and let next week's topics lean
toward the angles that pulled leads.
