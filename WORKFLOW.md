# Avada Commerce — Content Operations Workflow

This document describes how to use the AI-assisted content workflow for auditing, improving, and creating blog content at Avada.io.

---

## How It Works

The workflow is built on **Claude Code** (this AI tool) combined with live data sources:

| Data Source | What It Provides |
|-------------|-----------------|
| **Google Analytics 4** | Real traffic, user behavior, bounce rate, scroll depth, channel breakdown |
| **DataForSEO** | Live SERP rankings, keyword search volume, CPC, competitor URLs |
| **Shopify pricing page** | Current plan names, prices, transaction fees (USD) |
| **Competitor articles** | Content coverage, headings, word count, topics Avada is missing |

All of this feeds into a set of **skills** — slash commands you run in Claude Code to trigger predefined workflows.

---

## Skills Reference

| Skill | Command | When to Use |
|-------|---------|-------------|
| Prioritize content | `/prioritize-content` | Start of any content sprint — find which articles need attention most |
| Full blog audit | `/audit-blog` | Before touching any article — diagnoses all issues |
| Improve article | `/improve-blog` | When audit says Light Edit or Major Update |
| Rewrite article | `/rewrite-blog` | When audit says Full Rewrite |
| GA4 insights | `/ga4-insights` | Quick traffic check on a single URL |
| Write new blog | `/write-blog` | Creating a net-new article from scratch |

---

## The Standard Workflow

### Step 1 — Find What to Work On

Run `/prioritize-content` to get a priority-ranked list of all blog pages.

```
You: /prioritize-content
```

Claude runs `scripts/ga4_blog_traffic.py --days 90 --compare` and outputs:

- **🔴 High priority** — significant traffic decline, high bounce, or low engagement. Audit these first.
- **🟡 Medium priority** — some decline or engagement issues. Queue for next sprint.
- **🟢 Healthy** — stable or growing. Monitor only.

Each article gets a **priority score (0–100)**. Lower = more urgent.

> Pick the top 🔴 article and move to Step 2.

---

### Step 2 — Run a Full Audit

```
You: /audit-blog https://avada.io/blog/[article-slug]/
```

Claude runs four data checks automatically:

1. **GA4 performance** — sessions, bounce, scroll depth, trend vs prior 90 days
2. **DataForSEO SERP** — where Avada ranks for the main keyword, top competitors
3. **Shopify pricing** — fetches live USD pricing to verify accuracy in the article
4. **Competitor content gap** — fetches top 3–5 competitor articles, extracts headings and topics Avada is missing

Then runs three audits:

| Audit | Max Score | What It Checks |
|-------|-----------|----------------|
| SEO | 40 pts | Title, meta description, keyword placement, heading structure |
| Content Quality | 50 pts | Brand voice, writing style, banned vocabulary, structure, Avada product mentions |
| Freshness & Accuracy | 40 pts | Stats age, Shopify pricing accuracy, third-party tool accuracy |

**Total: 130 points.** The score maps to an action:

| Score | Traffic Signal | Action |
|-------|---------------|--------|
| 90–130 | Stable/growing | **Light Edit** — minor fixes, < 1 hour |
| 60–89 | Declining >30% | **Major Update** — multiple sections need updating, 2–4 hours |
| Below 60 | Declining >50% | **Full Rewrite** — structurally weak or fundamentally outdated |

> If Avada is not ranking in the top 20 for the main keyword, default to Major Update or Full Rewrite regardless of content score.

---

### Step 3 — Fix or Rewrite

**Light Edit or Major Update:**
```
You: /improve-blog
```
Claude makes surgical in-place edits: fixes pricing, updates stats, rewrites weak sections, fills content gaps from competitors, fixes SEO and style violations.

**Full Rewrite:**
```
You: /rewrite-blog
```
Claude writes the article from scratch using the audit findings as constraints and competitor gaps as the content brief. The rewrite follows the full writing framework from `skills/write-blog.md`.

Output is saved to `content/blogs/[keyword-slug]/[keyword-slug].md`.

---

## Quick Reference — One-Off Commands

**Check traffic for a single article:**
```
You: /ga4-insights https://avada.io/blog/[article-slug]/
```
Returns: sessions, bounce rate, scroll depth, outbound clicks, channel breakdown, monthly trend.

**Write a new article:**
```
You: /write-blog [topic or keyword]
```
Claude follows the full writing workflow: keyword research → outline → draft → review checklist.

---

## Files and Folder Structure

```
Avada Hub/
├── CLAUDE.md                    ← Workspace config (loaded every session)
├── WORKFLOW.md                  ← This file
│
├── avada-commerce/              ← Brand context loaded into every task
│   ├── company.md
│   ├── products.md
│   ├── audience.md
│   ├── competitors.md
│   ├── brand-voice.md
│   ├── visual-identity.md
│   ├── AI writing style/
│   │   └── AI Writing Style Guide.md
│   ├── GA4 json/                ← Service account credentials (gitignored)
│   └── dataforseo-credentials.json  ← DataForSEO credentials (gitignored)
│
├── skills/                      ← Skill definitions (slash commands)
│   ├── write-blog.md            ← /write-blog
│   ├── audit-blog.md            ← /audit-blog
│   ├── improve-blog.md          ← /improve-blog
│   ├── rewrite-blog.md          ← /rewrite-blog
│   ├── ga4-insights.md          ← /ga4-insights
│   └── prioritize-content.md   ← /prioritize-content
│
├── scripts/                     ← Python scripts used by skills
│   ├── ga4_blog_traffic.py      ← All blog pages traffic + priority scoring
│   ├── ga4_page_insights.py     ← Per-URL behavioral data
│   └── dataforseo_serp.py       ← SERP rankings, keyword volume, competitors
│
├── content/
│   └── blogs/
│       └── [keyword-slug]/
│           └── [keyword-slug].md  ← Published article drafts
│
└── Content-SEO Plan/
    ├── auditing/
    │   └── [month]/
    │       └── [keyword-slug]-audit.md  ← Saved audit reports
    └── ga4-exports/
        └── blog_traffic_*.csv   ← CSV exports from priority script
```

---

## Context Always Loaded

Every session, Claude automatically loads:

- **Brand voice** (`brand-voice.md`) — tone, what to avoid, good/bad examples
- **Products** (`products.md`) — Avada product names and descriptions for accurate mentions
- **AI Writing Style Guide** — personal quirks, banned phrases, structure patterns, scoring rubric
- **Competitors** (`competitors.md`) — known content competitors for gap analysis

This means you never need to re-explain the brand or style. Claude already knows.

---

## Credentials Setup

Two credential files are required. Both are gitignored and must be present locally:

**GA4 Service Account:**
- Path: `avada-commerce/GA4 json/tonal-asset-489802-h0-0e812b83f650.json`
- GA4 Property ID: `358883563`
- Required for: `/prioritize-content`, `/ga4-insights`, `/audit-blog`

**DataForSEO:**
- Path: `avada-commerce/dataforseo-credentials.json`
- Format: `{ "login": "...", "password": "..." }`
- Required for: `/audit-blog` (SERP + competitor data)

---

## Typical Sprint Example

```
Sprint goal: improve the 3 worst-performing blog articles this month

1. /prioritize-content
   → Shows 5 🔴 articles. Top 3 are the targets.

2. /audit-blog https://avada.io/blog/shopify-pricing-plans/
   → Score: 58/130. Action: Full Rewrite.

3. /rewrite-blog
   → New article saved to content/blogs/shopify-pricing-plans/

4. /audit-blog https://avada.io/blog/shopify-apps-for-dropshipping/
   → Score: 74/130. Action: Major Update.

5. /improve-blog
   → Updated in place.

6. /audit-blog https://avada.io/blog/email-marketing-for-shopify/
   → Score: 95/130. Action: Light Edit.

7. /improve-blog
   → Minor fixes applied.
```

Three articles fully addressed in one session.
