# Skill: Full Blog Audit for Avada Commerce

## Usage
Trigger: `/audit-blog`
Input: A live page URL from avada.io/blog or avada.io/tools

---

## Instructions

### Step 1: Confirm Input
Ask the user for the URL if not already provided. Confirm the main keyword (infer from URL slug if not given).

### Step 2: Fetch the Page Once
Use WebFetch on the provided URL. Extract everything needed for all audits in a single fetch:
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

### Step 3b: SERP & Keyword Data (DataForSEO)
Run the DataForSEO script to get keyword data and check Avada's current ranking:

```bash
python3 scripts/dataforseo_serp.py --keyword "<main keyword>" --url <URL> --top 50
```

Extract and note:
- **Monthly search volume:** How much traffic potential does this keyword have?
- **CPC & competition:** Signals commercial intent and difficulty
- **Avada's current rank:** In top 10? Top 50? Not ranking? — critical urgency signal
- **SERP features present:** AI Overview, Featured Snippet, PAA, Video — affects click-through rates and content format needed
- **Top-ranking competitors:** Use the top 3–5 organic results (excluding Shopify.com itself) as competitors for gap analysis in Step 3c

If Avada is not ranking in the top 20, default to Major Update or Full Rewrite regardless of content score.

### Step 3c: GA4 Performance Data
Run the GA4 insights script for the page being audited (last 90 days + compare to previous period):

```bash
python3 scripts/ga4_page_insights.py --url <URL> --days 90 --compare
```

Extract and note:
- **Sessions & trend:** Is traffic growing, stable, or declining?
- **Engagement rate & bounce rate:** Are users reading the content or leaving?
- **Avg session duration:** Proxy for content depth satisfaction
- **Scroll depth:** % reaching 90% (if tracked) — flags if users are dropping off early
- **Top traffic channel:** Organic vs Direct vs Referral — signals SEO health
- **Period delta:** % change vs prior 90 days — flags urgency of update

Use this data to inform action classification in Step 5. A page with >50% traffic decline or bounce rate >65% should default to Major Update or Full Rewrite regardless of content score alone.

### Step 3d: Competitor Content Gap Analysis
Use the top 3–5 organic URLs from the DataForSEO SERP results (Step 3b) as competitors. Fetch each with WebFetch and extract headings, unique topics, word count, and any data points not in the Avada article. Compare coverage and flag gaps. Reference `avada-commerce/competitors.md` for additional known content competitors.

---

### Step 4: Run All Three Audits

---

#### AUDIT 1: SEO (score out of 40)

##### Title
- [ ] Is it 60 characters or under?
- [ ] Does it include the main keyword?
- [ ] Is it clear, specific, and compelling?
- [ ] Does it avoid clickbait or vague phrasing?

##### Meta Description
- [ ] Is it 145–155 characters?
- [ ] Does it accurately describe what the article covers?
- [ ] Is it free of CTAs like "Learn more" or "Find out how"?
- [ ] Does it include the main keyword naturally?

##### Keyword Placement
- [ ] Is the main keyword in the H1?
- [ ] Is the main keyword in at least one H2?
- [ ] Does the main keyword appear in the first 100 words?
- [ ] Are secondary keywords used naturally throughout headings?

##### Heading Structure
- [ ] Is there exactly one H1?
- [ ] Do H2s cover the main topic angles clearly?
- [ ] Are H3s used to break down H2 sections (not used randomly)?
- [ ] Does the heading flow make logical sense top to bottom?
- [ ] Are headings descriptive (not generic like "Introduction" or "Conclusion")?
- [ ] Are there enough H2/H3 sections to make the article scannable?

---

#### AUDIT 2: Content Quality (score out of 50)

Reference `avada-commerce/AI writing style/AI Writing Style Guide.md` for full examples of each check below.

##### Brand Voice (reference `avada-commerce/brand-voice.md`)
- [ ] Is the tone professional but accessible? (Not corporate, not casual)
- [ ] Is it informative and educational? (Not promotional or exaggerated)
- [ ] Is it practical and actionable? (Real store examples, not abstract)
- [ ] Is it confident but neutral? (Not overselling Avada products)
- [ ] Are explanations direct? (Answers "what is" questions without analogies or counter-questions)
- [ ] Does the article acknowledge both strengths AND weaknesses where relevant? (Balanced, not one-sided)
- [ ] Are claims backed by specific data, sources, or examples? (Not vague generalities)

##### Writing Style
- [ ] Is plain English used throughout? (No unnecessary jargon)
- [ ] Are paragraphs max 3–4 sentences?
- [ ] Are sentences short and varied in length?
- [ ] Does each paragraph front-load its main idea? (Topic sentence first)
- [ ] Is there use of conjunctions and transitional phrases between paragraphs?
- [ ] Does the article lead with the verdict or key takeaway early? (Not buried at the end)
- [ ] Are contractions used naturally? (e.g., "you're", "it's", "doesn't")
- [ ] Is punctuation limited and clean? (No em-dashes or hyphens)
- [ ] Are numbers under ten spelled out? ("five", not "5") [CRITICAL]
- [ ] Is "okay" used, not "ok"? [CRITICAL]
- [ ] Is "email" used, not "e-mail"? [CRITICAL]
- [ ] Are italics used for subtle emphasis rather than bold?
- [ ] Do major sections end with a short one-sentence impact paragraph?
- [ ] Are specific tools and platforms referenced by name? (Not "various platforms")

##### Banned Vocabulary Check
Flag any use of these words or phrases:

**Corporate buzzwords:** Leverage (as verb), Utilize, Synergize, Streamlined, Seamless, Robust, Paradigm, Game-changing, Game-changer, Best-in-class, World-class, Cutting-edge, Disruptive, Next-level, Mission-critical

**AI clichés:** Delve, Meticulous, Elevate, Revolutionize, Holistic, Empower, Realm, Enhance, Reinvent, Embark, Reimagined, Enable, Redefine, Unprecedented, Embrace, Harness the power, Dive into, Emerge, Deep dive, Unleash, Ever-evolving, Unveil, Unlock, Paradigm shift, Tailored, Fast-paced, Navigate, Ensure

**Throat-clearing phrases:** "In conclusion...", "It's important to note that...", "At the end of the day...", "When all is said and done..."

**Cliché openings:** "In today's fast-paced world...", "As we move into the digital age...", "In an increasingly competitive landscape...", "Now more than ever...", "It's no secret that..."

##### Content Structure
- [ ] Does the introduction follow: Hook → Problem/Gap → Preview?
- [ ] After each H2 that has H3 subheadings, is there a 1–2 sentence transition before the first H3?
- [ ] Does the conclusion summarize key takeaways without CTAs or promotional links?
- [ ] Is the content scannable? (lists, bold text, clear headings used throughout)

##### Formatting
- [ ] Are lists used where appropriate?
- [ ] Is bold text used to highlight key points (not overused)?
- [ ] Does the article avoid the "[Keyword]: [Short Explanation]" stiff structure?
- [ ] Is the reading level approximately grade 7–8?

##### Avada Product Mentions (reference `avada-commerce/products.md`)
- [ ] Are Avada products mentioned naturally, not forced?
- [ ] Are mentions relevant to the article topic?
- [ ] Are related Avada blog posts cross-linked where appropriate?
- Products to check: Avada SEO Image Optimizer, SEO On apps, Chatty, AOV apps, Joy Loyalty, Joy Subscription, Air Reviews, SEA Survey, AG Order Printer, SEA Accessibility, Avada GDPR

##### Proposed New Outline (if needed)
If the Content Quality total is **below 40/50**, or Content Structure score is **below 7/10**, produce a proposed new outline:
- Fix structural problems (missing intro pattern, weak conclusion, missing transitions)
- Preserve sections that are working well
- Reorder sections where the flow is illogical
- Add missing sections flagged in the audit
- Include guidance notes for each section (keep / rewrite / new)

---

#### AUDIT 3: Freshness & Accuracy (score out of 40)

##### Statistics & Data
- [ ] Are all statistics from 2024 or later?
- [ ] Are statistics cited with a source link?
- [ ] Are any statistics from 2023 or earlier still accurate? (Flag with year)
- [ ] Are any statistics from 2022 or earlier present? (Flag as outdated — must update or remove)

##### Shopify Pricing Accuracy (USD only)
Compare article pricing vs. current Shopify pricing page in USD:
- [ ] Are plan names correct? (Starter, Basic, Grow, Advanced, Plus — note: "Shopify" plan is now "Grow")
- [ ] Are monthly USD prices correct?
- [ ] Are annual USD prices correct?
- [ ] Are annual discount percentages correct?
- [ ] Are transaction fees correct per plan?
- [ ] Is the trial offer / promotional price accurate?
- [ ] Are any discontinued plans or old pricing still referenced?

##### Shopify Feature Accuracy
- [ ] Are any features described that have changed or been removed?
- [ ] Are plan feature limits (staff accounts, inventory locations) still accurate?
- [ ] Are any new Shopify features missing that would strengthen the article?

##### Third-Party Tools & Apps
- [ ] Are any third-party tools mentioned that have changed, been acquired, or shut down?
- [ ] Are app pricing or feature claims still accurate?

##### Avada Product Accuracy
- [ ] Are Avada product names correct? (Reference `avada-commerce/products.md`)
- [ ] Are any discontinued Avada products mentioned?
- [ ] Are there new Avada products that could be added naturally?

---

### Step 5: Determine Audit Action

Based on combined scores and GA4 data, classify the article:

| Action | Criteria |
|--------|----------|
| **Light Edit** | Total score 90–120 AND traffic stable or growing. Minor fixes only. Estimated effort: < 1 hour. |
| **Major Update** | Total score 60–89 OR traffic declined >30% vs prior period OR bounce rate >65%. Multiple sections need updating. Estimated effort: 2–4 hours. |
| **Full Rewrite** | Total score below 60 OR traffic declined >50% with low engagement. Article is structurally weak, heavily outdated, or fundamentally off-brand. Estimated effort: full new article. |

---

### Step 6: Output Unified Report

```
## Full Blog Audit Report
**URL:** [url]
**Main Keyword:** [keyword]
**Audit Date:** [today's date]
**Article Last Updated:** [date or "Not visible"]

---

### SERP & Keyword Data
| Metric | Value |
|---|---|
| Monthly Search Volume | X,XXX |
| CPC | $X.XX |
| Competition | LOW / MEDIUM / HIGH (X/100) |
| Avada Current Rank | #X or Not in top 50 |
| SERP Features | [AI Overview / Featured Snippet / PAA / Video / etc.] |

**Top 5 Organic Competitors:**
1. [domain] — #X
2. [domain] — #X
3. [domain] — #X

---

### GA4 Performance Snapshot (Last 90 Days)
| Metric                  | Current Period | vs Prior 90 Days |
|------------------------|---------------|-----------------|
| Sessions               | X             | +/-X%            |
| Active Users           | X             | +/-X%            |
| Avg Session Duration   | Xm Xs         | —                |
| Engagement Rate        | X%            | —                |
| Bounce Rate            | X%            | —                |
| Scroll to 90%          | X% of users   | —                |
| Top Channel            | [Organic/Direct/etc.] | —        |

**Traffic Signal:** 🔴 Declining / 🟡 Stable / 🟢 Growing

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

1. 🔴 [Critical issue]
2. 🔴 [Critical issue]
3. 🟡 [Important issue]
4. 🟡 [Important issue]
5. 🟢 [Nice to fix]

---

### SEO Audit Details
| Category          | Score | Key Issues |
|------------------|-------|------------|
| Title             | X/10  | [note]     |
| Meta Description  | X/10  | [note]     |
| Keyword Placement | X/10  | [note]     |
| Heading Structure | X/10  | [note]     |

[Full findings per checklist item]

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

[Full findings per checklist item]

[Proposed New Outline if triggered]

---

### Freshness & Accuracy Details
| Category                  | Score | Key Issues |
|--------------------------|-------|------------|
| Statistics & Data         | X/10  | [note]     |
| Shopify Pricing Accuracy  | X/10  | [note]     |
| Shopify Feature Accuracy  | X/10  | [note]     |
| Third-Party Tools         | X/10  | [note]     |

**Shopify Pricing Discrepancies:**
| Plan | Billing | Article Says | Current (USD) | Status |
|------|---------|-------------|---------------|--------|
| [plan] | Monthly | $X | $X | ✅/❌ |

**Update Urgency:** 🔴 Critical / 🟡 Moderate / 🟢 Fresh

---

### Competitor Content Gap Analysis
**Competitors Checked:**
1. [URL] — ~X,XXX words
2. [URL] — ~X,XXX words
3. [URL] — ~X,XXX words

**Sections Avada article is MISSING:**
| Missing Topic | Found In | Priority |
|--------------|----------|----------|
| [topic]      | [competitor] | High/Medium/Low |

**Word count comparison:**
| Article | Word Count |
|---------|------------|
| Avada   | ~X,XXX     |
| Competitor 1 | ~X,XXX |
| Competitor 2 | ~X,XXX |
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
