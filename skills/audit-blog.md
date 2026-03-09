# Skill: Full Blog Audit for Avada Commerce

## Usage
Trigger: `/audit-blog`
Input: A live page URL from avada.io/blog or avada.io/tools

---

## Instructions

This is the master audit skill. It runs all three specialized audits in sequence and produces a unified report with an overall score and prioritized action plan.

### Step 1: Confirm Input
Ask the user for the URL if not already provided. Confirm the main keyword (infer from URL slug if not given).

### Step 2: Fetch the Page Once
Use WebFetch on the provided URL. Extract everything needed for all three audits in a single fetch:
- Page title, meta description, H1
- All H2 and H3 headings (in order)
- Full article body (intro, body sections, conclusion)
- All statistics with years cited
- All Shopify pricing figures mentioned
- All Avada product mentions
- Article last updated date (if visible)
- Approximate word count

### Step 3: Fetch Shopify Pricing (USD only)
Use WebFetch on `https://www.shopify.com/pricing` to get current plan names, prices, fees, and trial offer.

**All pricing must be verified in USD. Do not use regional pricing from other country versions of the page.**

If the article covers Shopify features in depth, also fetch the relevant Shopify Help Center page.

### Step 3b: Competitor Content Gap Analysis
Use WebSearch to find the top 3 ranking competitor articles for the main keyword. Fetch each and extract headings, unique topics, word count, and any data points not in the Avada article. Compare coverage and flag gaps. Reference `avada-commerce/competitors.md` for known content competitors.

### Step 4: Run All Three Audits

Run each audit using the full checklist from each specialized skill file:

#### SEO Audit (reference `skills/audit-seo.md`)
- Title check
- Meta description check
- Keyword placement check
- Heading structure check

#### Content Quality Audit (reference `skills/audit-content.md`)
- Brand voice check (reference `avada-commerce/brand-voice.md`)
- Writing style check
- Banned vocabulary scan
- Content structure check
- Formatting check
- Avada product mentions check (reference `avada-commerce/products.md`)
- Proposed new outline (if content structure score is below 7/10 or total content score is below 40/50)

#### Freshness & Accuracy Audit (reference `skills/audit-freshness.md`)
- Statistics & data currency
- Shopify pricing accuracy in USD (compare vs fetched Shopify pricing page)
- Shopify feature accuracy
- Third-party tools accuracy
- Avada product accuracy
- Competitor content gap analysis (topics missing vs. top 3 ranking competitors)

### Step 5: Determine Audit Action

Based on the combined scores, classify the article into one of three actions:

| Action | Criteria |
|--------|----------|
| **Light Edit** | Total score 90–120. Minor fixes only. Estimated effort: < 1 hour. |
| **Major Update** | Total score 60–89. Multiple sections need rewriting or updating. Estimated effort: 2–4 hours. |
| **Full Rewrite** | Total score below 60. Article is structurally weak, heavily outdated, or fundamentally off-brand. Estimated effort: full new article. |

### Step 6: Output Unified Report

```
## Full Blog Audit Report
**URL:** [url]
**Main Keyword:** [keyword]
**Audit Date:** [today's date]
**Article Last Updated:** [date or "Not visible"]

---

### Overall Scores
| Audit Area              | Score  |
|------------------------|--------|
| SEO                    | X/40   |
| Content Quality        | X/50   |
| Freshness & Accuracy   | X/40   |
| Competitor Gap         | noted  |
| **Total**              | X/130  |

### Audit Action: [LIGHT EDIT / MAJOR UPDATE / FULL REWRITE]
[1–2 sentence summary of why this action is recommended]

---

### Priority Action List
Ranked by impact. Fix these first.

1. 🔴 [Critical issue — e.g. wrong Shopify pricing]
2. 🔴 [Critical issue]
3. 🟡 [Important issue — e.g. banned vocabulary, outdated stat]
4. 🟡 [Important issue]
5. 🟢 [Nice to fix — e.g. minor heading tweak]

---

### SEO Audit Details
| Category         | Score | Key Issues |
|-----------------|-------|------------|
| Title            | X/10  | [note]     |
| Meta Description | X/10  | [note]     |
| Keyword Placement| X/10  | [note]     |
| Heading Structure| X/10  | [note]     |

[Full SEO findings from audit-seo.md checklist]

---

### Content Quality Details
| Category            | Score | Key Issues |
|--------------------|-------|------------|
| Brand Voice         | X/10  | [note]     |
| Writing Style       | X/10  | [note]     |
| Content Structure   | X/10  | [note]     |
| Formatting          | X/10  | [note]     |
| Avada Integration   | X/10  | [note]     |

**Banned Vocabulary Found:** [list words + sentences, or "None found"]

[Full content quality findings from audit-content.md checklist]

---

### Freshness & Accuracy Details
| Category                  | Score | Key Issues |
|--------------------------|-------|------------|
| Statistics & Data         | X/10  | [note]     |
| Shopify Pricing Accuracy  | X/10  | [note]     |
| Shopify Feature Accuracy  | X/10  | [note]     |
| Third-Party Tools         | X/10  | [note]     |

**Shopify Pricing Discrepancies:**
| Item | Article Says | Current | Status |
|------|-------------|---------|--------|
| [plan/fee] | $X | $X | ✅/❌ |

**Update Urgency:** 🔴 Critical / 🟡 Moderate / 🟢 Fresh

[Full freshness findings from audit-freshness.md checklist]
```

### Step 7: Ask if User Wants to Proceed
After the report, ask:
> "Would you like me to make the edits now, or save this audit report to the workspace?"

If saving: write the report as a `.md` file to `Content-SEO Plan/auditing/[month]/[keyword-slug]-audit.md`.

---

## Notes
- Always fetch the live page fresh — do not use cached assumptions about content
- If WebFetch fails on the article URL, report the error and ask the user to paste the article content directly
- If the Shopify pricing page fetch fails, note it in the report and flag all pricing figures as "unverified"
- Scoring is a guide, not a hard rule — use judgment when a checklist item is partially met
