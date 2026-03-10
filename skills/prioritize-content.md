# Skill: Content Priority Queue

## Usage
Trigger: `/prioritize-content`
Input: Optional — number of days to analyze (default: 90). User may also specify a topic filter (e.g., "only Shopify articles").

---

## Instructions

### Step 1: Run the Priority Script

```bash
python3 scripts/ga4_blog_traffic.py --days 90 --compare
```

This pulls all `/blog/` pages from GA4, compares current vs prior 90 days, and outputs a priority-sorted table with a score for each page.

**Priority score explained (0–100, lower = more urgent):**
- Traffic decline >50% → heavy penalty
- Bounce rate >70% → penalty
- Engagement rate <30% → penalty
- Small pages (<50 sessions) → slight downgrade (low impact)
- Growing traffic + healthy engagement → score increases

### Step 2: Read the Output

Parse the terminal table. Extract:
- All 🔴 pages (score < 35) — these need `/audit-blog` immediately
- All 🟡 pages (score 35–54) — queue for next sprint
- All 🟢 pages (score 55+) — healthy, monitor only

### Step 3: Output the Priority Queue

Present a clean table to the user:

```
## Content Priority Queue
**Period:** Last 90 days vs prior 90 days
**Run date:** [today]
**Total blog pages:** X

---

### 🔴 High Priority — Audit Now
| # | Path | Sessions | Change | Bounce | Engagement | Score |
|---|------|----------|--------|--------|------------|-------|
| 1 | /blog/... | XXX | -XX% | XX% | XX% | XX |

### 🟡 Medium Priority — Next Sprint
| # | Path | Sessions | Change | Bounce | Engagement | Score |
|---|------|----------|--------|--------|------------|-------|

### 🟢 Healthy — Monitor Only
| # | Path | Sessions | Change | Bounce | Engagement | Score |
|---|------|----------|--------|--------|------------|-------|
```

### Step 4: Recommend Next Action

After the table, add:

> **Recommended next step:** Run `/audit-blog` on the top 🔴 article: `[URL]`

If the user says "audit the top one" or "start with #1", proceed directly with `/audit-blog` on that URL without waiting for further confirmation.

### Step 5: Save (optional)

If the user wants to save the priority list:
- Save as `Content-SEO Plan/auditing/[month]/content-priority-[date].md`

---

## Notes
- The script CSV export also lands in `Content-SEO Plan/ga4-exports/` for reference
- If the GA4 script fails (missing credentials), report the error and ask the user to check `avada-commerce/GA4 json/`
- Score is a guide — use judgment. A high-traffic page with -30% decline may be more important than a low-traffic page with -80% decline
