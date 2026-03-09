# Skill: Content Quality Audit for Avada Commerce Blog

## Usage
Trigger: `/audit-content`
Input: A live page URL from avada.io/blog or avada.io/tools

---

## Instructions

### Step 1: Fetch the Page
Use WebFetch on the provided URL. Extract:
- Full article body text (as much as possible)
- Introduction (first 150–200 words)
- Conclusion (last 100–150 words)
- All headings
- Any lists, tables, or bold text usage
- Any Avada product mentions

### Step 2: Run Content Quality Checks

#### Brand Voice (reference `avada-commerce/brand-voice.md`)
- [ ] Is the tone professional but accessible? (Not corporate, not casual)
- [ ] Is it informative and educational? (Not promotional or exaggerated)
- [ ] Is it practical and actionable? (Real store examples, not abstract)
- [ ] Is it confident but neutral? (Not overselling Avada products)
- [ ] Is it written in first person where appropriate?
- [ ] Are explanations direct? (Answers "what is" questions without analogies or counter-questions)

#### Writing Style
- [ ] Is plain English used throughout? (No unnecessary jargon)
- [ ] Are paragraphs max 3–4 sentences?
- [ ] Are sentences short and varied in length?
- [ ] Is there use of conjunctions and transitional phrases between paragraphs?
- [ ] Does the article ask a question or two to engage the reader?
- [ ] Is punctuation limited and clean? (No em-dashes or hyphens)

#### Banned Vocabulary Check
Flag any use of these words:
Leverage, Delve, Meticulous, Elevate, Revolutionize, Holistic, Empower, Realm, Seamless, Enhance, Reinvent, Fast-paced, Embark, Reimagined, Game-changer, Enable, Redefine, Unprecedented, Embrace, Harness the power, Next-level, Ensure, Navigate, Best-in-class, Dive into, Disruptive, Emerge, Deep dive, Unleash, Synergy, Ever-evolving, Unveil, Mission-critical, Unlock, Paradigm shift, Tailored.

#### Content Structure
- [ ] Does the introduction follow: Hook → Problem/Gap → Preview?
- [ ] Does the article follow one of the 12 Avada blog templates? (reference `skills/write-blog.md`)
- [ ] After each H2 that has H3 subheadings, is there a 1–2 sentence transition before the first H3?
- [ ] Does the conclusion summarize key takeaways without CTAs or promotional links?
- [ ] Is the content scannable? (lists, bold text, clear headings used throughout)

#### Formatting
- [ ] Are lists used where appropriate?
- [ ] Is bold text used to highlight key points (not overused)?
- [ ] Does the article avoid the "[Keyword]: [Short Explanation]" stiff structure?
- [ ] Is the reading level approximately grade 7–8? (Simple, accessible language)

#### Avada Product Mentions
- [ ] Are Avada products mentioned naturally, not forced?
- [ ] Are mentions relevant to the article topic?
- [ ] Are related Avada blog posts cross-linked where appropriate?
- Products to check: Avada SEO Image Optimizer, SEO On apps, Chatty, AOV apps, Joy Loyalty, Joy Subscription, Air Reviews, SEA Survey, AG Order Printer, SEA Accessibility, Avada GDPR

### Step 3: Score and Output

Score each category out of 10. Output the following format:

```
## Content Quality Audit: [URL]

### Scores
| Category            | Score |
|--------------------|-------|
| Brand Voice         | X/10  |
| Writing Style       | X/10  |
| Content Structure   | X/10  |
| Formatting          | X/10  |
| Avada Integration   | X/10  |
| **Total**           | X/50  |

### Findings

#### Brand Voice
[Pass/Fail each checklist item with brief note or example from the article]

#### Writing Style
[Pass/Fail each checklist item with brief note]

#### Banned Vocabulary Found
[List any flagged words with the sentence they appear in]

#### Content Structure
[Pass/Fail each checklist item with brief note]

#### Formatting
[Pass/Fail each checklist item with brief note]

#### Avada Product Mentions
[List mentions found, assess if natural or forced. Flag missed opportunities.]

### Priority Content Fixes
1. [Most critical fix]
2. [Second fix]
3. [Third fix]
```

---

### Step 4: Proposed New Outline (if needed)

If the total score is **below 40/50**, or if the Content Structure score is **below 7/10**, produce a revised article outline.

The outline should:
- Fix structural problems identified in the audit (missing intro pattern, weak conclusion, missing transitions, wrong template)
- Preserve sections that are working well (keep H2s and H3s that passed)
- Reorder sections where the flow is illogical
- Add missing sections flagged in the audit (e.g. missing Hook, missing FAQ, missing conclusion)
- Follow the correct blog template from `skills/write-blog.md`
- Include guidance notes for each section (what to write, what to avoid, what to preserve from the original)

Output format:

```
## Proposed New Outline: [URL]

**Blog Type:** [selected template from write-blog.md]
**Why this template:** [1 sentence reason]
**Sections preserved from original:** [list]
**Sections removed:** [list with reason]
**Sections added:** [list with reason]

---

### Outline

**Title:** [proposed title, ≤ 60 chars]
**Meta Description:** [145–155 chars]

---

**Introduction** (100–200 words)
- Hook: [what to open with — stat, scenario, or question]
- Problem/Gap: [what merchants get wrong or overlook]
- Preview: [what the article covers]

**H2: [Section heading]**
> Note: [Keep as-is / Rewrite / New section — brief instruction]
  - H3: [Subsection]
    > Note: [instruction]
  - H3: [Subsection]
    > Note: [instruction]

**H2: [Section heading]**
> Note: [Keep as-is / Rewrite / New section — brief instruction]

[... continue for all sections ...]

**Conclusion** (5–8 sentences)
> Note: Summarize [X, Y, Z key takeaways]. No CTAs. No promotional links.
```

If the score is 40/50 or above and structure is solid, skip this step and state:
> "Content structure is strong — no new outline needed."

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 9-10 | Excellent — no action needed |
| 7-8  | Good — minor improvements possible |
| 5-6  | Fair — several issues to fix |
| 3-4  | Poor — significant rework needed |
| 1-2  | Critical — major quality problems |
