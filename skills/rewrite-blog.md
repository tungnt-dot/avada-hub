# Skill: Rewrite Blog Post for Avada Commerce

## Usage
Trigger: `/rewrite-blog`
Input: A live page URL + the audit report for that article (either pasted or from saved file in `Content-SEO Plan/auditing/`)
Action type: **Full Rewrite**

---

## Instructions

This skill fully rewrites an existing Avada blog article from scratch. It uses the audit findings as constraints (what went wrong), the competitor gap analysis as a content brief (what to include), and `write-blog.md` as the writing framework. The output is a brand-new article on the same keyword.

Use this only when the audit report classifies the article as **Full Rewrite** (score below 60/130). For Light Edit or Major Update articles, use `/improve-blog` instead.

---

### Step 1: Load Inputs

1. **Fetch the live article** using WebFetch on the provided URL. Extract:
   - Main keyword
   - All headings (to understand the original angle)
   - Any strong sections or personal examples worth preserving
   - Approximate word count (to set a target)

2. **Load the audit report** — from the pasted report or from `Content-SEO Plan/auditing/[month]/[slug]-audit.md`. Note:
   - What the article got wrong (all priority action items)
   - Competitor content gaps to fill
   - Verified USD pricing figures (if article covers pricing)
   - Missing statistics or outdated data

3. **Fetch current Shopify pricing** if the article involves pricing — WebFetch `https://www.shopify.com/pricing` for current USD figures.

---

### Step 2: Build the Content Brief

Before writing, produce a brief:

```
### Rewrite Brief: [keyword]

**Target keyword:** [main keyword]
**Secondary keywords:** [infer from original article and audit gaps]
**Target word count:** [match or beat top competitor, minimum 2,000 words]
**Blog type:** [select best-fit template from write-blog.md]

**Must fix from audit:**
- [issue 1]
- [issue 2]
- ...

**Must include (competitor gaps):**
- [topic/section 1]
- [topic/section 2]
- ...

**Verified pricing/data to use:**
- [e.g. Basic plan: $19/month annual, ~$25/month monthly]
- ...

**Preserve from original (if any):**
- [e.g. author's personal cost breakdown — flag for human review]
```

Wait for user confirmation before writing, unless they have already confirmed to proceed.

---

### Step 3: Write the Article

Follow ALL rules from `skills/write-blog.md`:

- Select the correct blog template and follow its structure exactly
- Follow brand voice from `avada-commerce/brand-voice.md`
- Reference `avada-commerce/products.md` for accurate Avada product names
- Reference `avada-commerce/audience.md` for accurate target audience framing
- Use `avada-commerce/competitors.md` for competitive context if relevant

**Additional rewrite-specific rules:**
- Do not carry over em-dashes, banned vocabulary, or style violations from the original
- All pricing must use verified USD figures from the audit report or freshly fetched Shopify pricing page
- All statistics must be 2024 or later with source links
- Fill every high and medium priority content gap identified in the competitor analysis
- Add Avada product mentions naturally — use `avada-commerce/products.md` for correct names
- Target word count should match or beat the top competitor article

---

### Step 4: Output Format

```
**Title:** [max 60 chars, includes main keyword]
**Meta Description:** [145-155 chars, purely descriptive, no CTAs]
**Main Keyword:** [keyword]
**Blog Type:** [template used]
**Word Count:** [approximate]

---

[Full rewritten article in markdown]
```

---

### Step 5: Self-Check

Before finalizing, verify every item:
- [ ] Title ≤ 60 characters, includes main keyword
- [ ] Meta description 145–155 characters, purely descriptive, no CTAs
- [ ] Keyword in title, all major H2s, and first 100 words
- [ ] Structure matches selected blog template from `write-blog.md`
- [ ] Introduction follows Hook → Problem/Gap → Preview (100–200 words)
- [ ] No em-dashes or hyphens used as punctuation
- [ ] No banned vocabulary
- [ ] Paragraphs ≤ 4 sentences
- [ ] Sentences short and varied
- [ ] All Shopify pricing figures are current USD (verified from audit or live Shopify page)
- [ ] All statistics 2024 or later with source citations
- [ ] All content gaps (High + Medium priority) from competitor analysis are filled
- [ ] Conclusion: summarizes key takeaways only — no CTAs, no promo links
- [ ] Avada products mentioned naturally where relevant
- [ ] Reading level approximately grade 7–8
- [ ] Transition sentence after each H2 that has H3 subheadings

---

### Step 6: Flag Preserved Content

If anything was preserved from the original article (e.g. personal anecdotes, original data, author's own experience), flag it:

```
### Preserved from Original — Human Review Required
- [Section/sentence] — kept because [reason]. Verify accuracy before publishing.
```

---

### Step 7: Ask to Save

After outputting the rewritten article, ask:
> "Would you like me to save this rewritten article to the workspace?"

If yes: save as `content/blogs/[keyword-slug]/[keyword-slug].md`

---

## Notes
- A full rewrite does not mean ignoring the original entirely — extract any genuinely strong content (data, examples, unique angles) and incorporate it into the new article
- The goal is to produce an article that would outrank the original and the top 3 competitors for the main keyword
- If the blog type is unclear, default to the template that best fits the keyword intent (informational → What Is or Beginner's Guide; transactional/comparison → Comparison; comprehensive → Pillar Post)
