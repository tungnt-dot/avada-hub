# Skill: Freshness, Accuracy & Competitor Gap Audit for Avada Commerce Blog

## Usage
Trigger: `/audit-freshness`
Input: A live page URL from avada.io/blog or avada.io/tools

---

## Instructions

### Step 1: Fetch the Article
Use WebFetch on the provided URL. Extract:
- All statistics and data points (note the year cited for each)
- All Shopify pricing figures mentioned (plan names, prices, transaction fees)
- All Shopify feature references (plan features, limits, capabilities)
- Any references to Shopify promotions or trial offers
- Any references to third-party tools, apps, or platforms
- The article's last updated date (if visible on the page)
- All H2 and H3 headings (to compare against competitors later)

### Step 2: Fetch Official Shopify Pricing Page (US)
Use WebFetch on: `https://www.shopify.com/pricing`

**Important: All pricing must be verified in USD (United States). Ignore regional pricing.**

Extract:
- Current plan names
- Current monthly prices in USD (billed monthly, no annual commitment)
- Current annual prices in USD (billed yearly, shown as monthly equivalent)
- Annual discount percentage per plan
- Current transaction fees per plan (third-party payment provider fees)
- Current trial offer (e.g. free trial duration, $1/month promotion)
- Key plan features or limits (staff accounts, inventory locations, etc.)

If the pricing page does not clearly show both monthly and annual USD prices, also fetch:
`https://help.shopify.com/en/manual/your-account/manage-billing/your-invoice/plans`

### Step 3: Fetch Shopify Help Center (if article covers features)
If the article covers Shopify features (e.g. shipping, payments, POS, analytics, checkout), fetch the relevant Shopify Help Center page:
- Shopify Help Center base: `https://help.shopify.com/en`
- Fetch the most relevant help doc based on the article topic to verify feature accuracy

### Step 4: Competitor Content Gap Analysis
Use WebSearch to find the top 3 ranking articles for the article's main keyword (infer keyword from URL slug and H1).

Search query format: `[main keyword] site:hostinger.com OR site:bigcommerce.com OR site:ecommerce-platforms.com OR site:pagefly.io OR site:shopify.com/blog`

For each competitor found, use WebFetch to extract:
- All H2 and H3 headings
- Any unique angles, topics, or sections not covered in the Avada article
- Any statistics or data points cited
- Word count (approximate)
- Structured data like tables, comparison charts, or FAQs

Then compare competitor coverage vs. the Avada article:
- [ ] Do competitors cover any major sub-topics that the Avada article is missing?
- [ ] Do competitors have a more useful structure (e.g. better comparison table, FAQs, calculator)?
- [ ] Are there new angles competitors use that would improve the Avada article?
- [ ] Do competitors cite any newer statistics or studies worth including?
- [ ] Is the Avada article longer or shorter than competitors? Is the gap significant?

### Step 5: Run Freshness Checks

#### Statistics & Data
- [ ] Are all statistics from 2024 or later?
- [ ] Are statistics cited with a source link?
- [ ] Are any statistics from 2023 or earlier still accurate and worth keeping? (If so, flag with year)
- [ ] Are any statistics from 2022 or earlier present? (Flag as outdated — must update or remove)

#### Shopify Pricing Accuracy (USD only)
Compare article pricing vs. current Shopify pricing page in USD:
- [ ] Are plan names correct? (Starter, Basic, Grow, Advanced, Plus — note: "Shopify" plan is now "Grow")
- [ ] Are monthly USD prices correct? (billed monthly, no commitment)
- [ ] Are annual USD prices correct? (billed yearly, shown as monthly equivalent)
- [ ] Are annual discount percentages correct?
- [ ] Are transaction fees correct per plan?
- [ ] Is the trial offer / promotional price accurate?
- [ ] Are any discontinued plans or old pricing still referenced?

#### Shopify Feature Accuracy
- [ ] Are any features described that have changed or been removed?
- [ ] Are plan feature limits (staff accounts, inventory locations) still accurate?
- [ ] Are any new Shopify features missing that would strengthen the article?

#### Third-Party Tools & Apps
- [ ] Are any third-party tools mentioned that have changed significantly, been acquired, or shut down?
- [ ] Are app pricing or feature claims still accurate?

#### Avada Product Accuracy
- [ ] Are Avada product names correct? (Reference `avada-commerce/products.md`)
- [ ] Are any discontinued Avada products mentioned?
- [ ] Are there new Avada products that could be added naturally?

### Step 6: Score and Output

Score each category out of 10. Output the following format:

```
## Freshness, Accuracy & Competitor Audit: [URL]
**Article Last Updated:** [date if found, or "Not visible"]
**Shopify Pricing Checked:** [today's date] (USD)

### Scores
| Category                      | Score |
|------------------------------|-------|
| Statistics & Data             | X/10  |
| Shopify Pricing Accuracy (USD)| X/10  |
| Shopify Feature Accuracy      | X/10  |
| Third-Party Tools             | X/10  |
| **Total**                     | X/40  |

### Findings

#### Statistics & Data
[List each stat found, year cited, and whether it passes or needs updating]

#### Shopify Pricing (USD): Article vs. Current
| Plan | Billing | Article Says | Current (USD) | Status |
|------|---------|-------------|---------------|--------|
| Basic | Monthly | $X | $X | ✅/❌ |
| Basic | Annual (per month) | $X | $X | ✅/❌ |
| Grow | Monthly | $X | $X | ✅/❌ |
| Grow | Annual (per month) | $X | $X | ✅/❌ |
| Advanced | Monthly | $X | $X | ✅/❌ |
| Advanced | Annual (per month) | $X | $X | ✅/❌ |
| Plus | Monthly | $X | $X | ✅/❌ |
| Starter | Monthly | $X | $X | ✅/❌ |
| Trial offer | — | [article] | [current] | ✅/❌ |
| Basic 3rd-party fee | — | X% | X% | ✅/❌ |
| Grow 3rd-party fee | — | X% | X% | ✅/❌ |
| Advanced 3rd-party fee | — | X% | X% | ✅/❌ |

#### Shopify Feature Accuracy
[List any features checked and whether they are still accurate]

#### Third-Party Tools
[Note any tools mentioned and flag any known changes]

#### Avada Products
[Note mentions found, check against products.md, flag any issues]

---

### Competitor Content Gap Analysis

**Keyword:** [main keyword]
**Competitors Checked:**
1. [Competitor 1 URL] — [word count approx]
2. [Competitor 2 URL] — [word count approx]
3. [Competitor 3 URL] — [word count approx]

**Sections Avada article is MISSING vs. competitors:**
| Missing Topic / Section | Found In | Priority |
|------------------------|----------|----------|
| [topic] | [competitor] | High/Medium/Low |

**New angles or improvements competitors use:**
- [e.g. "Competitor X includes a live pricing calculator widget"]
- [e.g. "Competitor Y has a detailed table comparing Shopify Payments availability by country"]

**Word count comparison:**
| Article | Word Count |
|---------|------------|
| Avada (this article) | ~X,XXX |
| Competitor 1 | ~X,XXX |
| Competitor 2 | ~X,XXX |

**Verdict:** [Is Avada's coverage comprehensive, or are there clear content gaps to fill?]

---

### Priority Freshness & Gap Fixes
1. [Most urgent — e.g. wrong USD price]
2. [Second fix]
3. [Third fix]
4. [Content gap to add]
5. [Content gap to add]

### Update Urgency
- 🔴 Critical — pricing or major facts are wrong, update immediately
- 🟡 Moderate — some stats outdated or content gaps found, update within 30 days
- 🟢 Fresh — all data current, no urgent action needed
```

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 9-10 | Fully fresh — all data current |
| 7-8  | Mostly fresh — 1-2 minor items to update |
| 5-6  | Partially stale — several facts need updating |
| 3-4  | Stale — pricing or key facts are wrong |
| 1-2  | Critical — major inaccuracies throughout |
