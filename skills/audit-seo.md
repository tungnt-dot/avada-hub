# Skill: SEO Audit for Avada Commerce Blog

## Usage
Trigger: `/audit-seo`
Input: A live page URL from avada.io/blog or avada.io/tools

---

## Instructions

### Step 1: Fetch the Page
Use WebFetch on the provided URL. Extract:
- Page title (text shown in browser tab / `<title>` tag)
- Meta description
- H1 tag
- All H2 and H3 headings (in order)
- First 100 words of the introduction
- Main keyword (infer from URL slug and H1 if not provided by user)

### Step 2: Run SEO Checks

#### Title
- [ ] Is it 60 characters or under?
- [ ] Does it include the main keyword?
- [ ] Is it clear, specific, and compelling?
- [ ] Does it avoid clickbait or vague phrasing?

#### Meta Description
- [ ] Is it 145–155 characters?
- [ ] Does it accurately describe what the article covers?
- [ ] Is it free of CTAs like "Learn more" or "Find out how"?
- [ ] Does it include the main keyword naturally?

#### Keyword Placement
- [ ] Is the main keyword in the H1?
- [ ] Is the main keyword in at least one H2?
- [ ] Does the main keyword appear in the first 100 words?
- [ ] Are secondary keywords used naturally throughout headings?

#### Heading Structure
- [ ] Is there exactly one H1?
- [ ] Do H2s cover the main topic angles clearly?
- [ ] Are H3s used to break down H2 sections (not used randomly)?
- [ ] Does the heading flow make logical sense top to bottom?
- [ ] Are headings descriptive (not generic like "Introduction" or "Conclusion")?

#### Content Scannability (inferred from headings)
- [ ] Are there enough H2/H3 sections to make the article scannable?
- [ ] Do headings suggest use of lists, tables, or step-by-step content?

### Step 3: Score and Output

Score each category out of 10. Output the following format:

```
## SEO Audit: [URL]
**Main Keyword:** [keyword]

### Scores
| Category         | Score |
|-----------------|-------|
| Title            | X/10  |
| Meta Description | X/10  |
| Keyword Placement| X/10  |
| Heading Structure| X/10  |
| **Total**        | X/40  |

### Findings

#### Title
[Pass/Fail each checklist item with brief note]

#### Meta Description
[Pass/Fail each checklist item with brief note]

#### Keyword Placement
[Pass/Fail each checklist item with brief note]

#### Heading Structure
[Pass/Fail each checklist item with brief note]

### Priority SEO Fixes
1. [Most critical fix]
2. [Second fix]
3. [Third fix]
```

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 9-10 | Excellent — no action needed |
| 7-8  | Good — minor improvements possible |
| 5-6  | Fair — several issues to fix |
| 3-4  | Poor — significant rework needed |
| 1-2  | Critical — major SEO problems |
