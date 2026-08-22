# Hello People, daily social automation system

The engine that turns one topic a week into a full week of on-brand posts across
Instagram (feed + story), Facebook, LinkedIn, and X, aimed at engagement,
followers, and leads. Say hello to less busywork, including our own.

## Where things live (two repos, kept separate)

- **This repo (design system)** holds the MACHINE: the generator (`social/`), the
  brand and voice rules, and this plan. Stable, rarely changes.
- **dpatel15/hellopeople-social** holds the OUTPUT: one folder per week
  (`weeks/<date>/` with content.csv, reel-scripts.md, images/). The weekly Routine
  writes there, never here, so the design system stays clean.

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

---

# Growth system (v2): what a full week now produces

Each weekly cycle the brain generates, for one chosen topic:

1. **7 daily post sets**, copy tailored to Instagram (feed + story), Facebook,
   LinkedIn, and X.
2. **7 daily branded images / carousels** from the design system (`social/`).
3. **7 daily Reel scripts** (see `social/reel-scripts-*.md`), mixed for reach and
   leads: about 4 educational, 2 lead-focused, 1 pure-reach per week.
4. **Alt text** for every image.
5. **Tracking links** (UTM) for anything pointing at the site.

You approve the week in the sheet; Metricool publishes daily at 8am; you (or a
teammate) film the Reels from the scripts.

## Content pillars (so weeks never repeat and always sell)

Every topic maps to one of four pillars, and a good week uses all four:

1. **Teach** (educational): how AI works in a real business day. Builds authority,
   earns saves and shares.
2. **Prove** (before/after, cases, numbers): real outcomes. Builds trust.
3. **Bust** (myths and objections): "AI won't replace your team." Removes fear.
4. **Invite** (offers and lead magnets): "comment AUDIT." Converts attention.

Rough mix per week: 40% Teach, 25% Prove, 20% Bust, 15% Invite.

### Topic bank (starter, rotate and add)

AI receptionist / missed calls, invoice chasing, lead follow-up speed, no-show
reminders, review requests, onboarding paperwork, inbox triage, quote and
estimate generation, appointment booking, data entry between apps, FAQ answering,
after-hours coverage, seasonal rush handling, "what to automate first," cost of
busywork, AI myths, human vs machine work, small-team productivity.

## The seven growth initiatives (execution plan)

Priority order, most leads first:

| # | Initiative | What it is | Tool | Status |
|---|---|---|---|---|
| 1 | **Auto-DM** | Comment "AUDIT" triggers an instant DM with the lead magnet | ManyChat (free) | to set up |
| 2 | **Lead magnet** | One-page "5 tasks to automate first" checklist (on brand) | Design system | to build |
| 3 | **Daily Reels** | 7 scripts a week, filmed and posted | Scripts done weekly | scripts ready |
| 4 | **Tracking links** | UTM / short links so we tie posts to booked audits | Bitly or /go links | to set up |
| 5 | **First-comment link** | Auto-post the link as the first comment on IG | Metricool / ManyChat | to set up |
| 6 | **Pillars + topic bank** | Funnel-balanced topics, no repeats | This doc | done |
| 7 | **Alt text** | Accessibility + small reach bump, on every image | Engine | to add to engine |

### Phased rollout

- **Phase 1 (this week):** build the lead magnet (#2), set up the auto-DM keyword
  flow (#1), and wire the weekly Routine + Metricool. This gets a review-gated,
  lead-capturing system live.
- **Phase 2:** add tracking links (#4) and first-comment automation (#5), start
  filming the daily Reels from the scripts (#3).
- **Phase 3:** add alt text to the engine (#7), and let Friday reporting steer the
  pillar mix. Pillars and topic bank (#6) are already in place.

## Reel script format (what the brain writes each week)

Reel scripts are written to be spoken authentically, not read off a teleprompter.
They are founder-led talking points, first person, helping one real person, so
they sound like you and not like an ad. For each day: what you genuinely believe
about the topic, a real 2 second hook, the shooting format (talking head / screen
recording / text-on-screen), loose talking points in your own words, an honest
CTA tied to the lead mechanic (offered as a gift, not a pitch), the post caption,
and hashtags. See `social/reel-scripts-week-ai-in-real-life.md` for the worked
example week and the delivery notes.

## The lead loop (how a view becomes a booked audit)

Reel or post (hook) -> "comment AUDIT" -> **auto-DM sends the checklist** ->
checklist ends with "book your free audit" (tracked link) -> booked audit. Every
piece of content feeds this one loop, so the whole week compounds into leads, not
just likes.
