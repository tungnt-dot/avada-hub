# Skill: Improve Blog Post for Avada Commerce

## Usage
Trigger: `/improve-blog`
Input: A live page URL + the audit report for that article (either pasted or from saved file in `Content-SEO Plan/auditing/`)
Action type: **Light Edit** or **Major Update**

---

## Instructions

This skill takes an existing Avada blog article and improves it in-place based on audit findings. It preserves the article's structure and voice where they are working, and surgically fixes what the audit flagged. It does NOT rewrite from scratch — use `/rewrite-blog` for that.

---

### Step 1: Load Inputs

1. **Fetch the live article** using WebFetch on the provided URL. Extract the full article content.
2. **Load the audit report** — either from the pasted report in the conversation, or from the saved file at `Content-SEO Plan/auditing/[month]/[slug]-audit.md`.
3. Confirm the **audit action** (Light Edit or Major Update). If the audit report says Full Rewrite, stop and tell the user to use `/rewrite-blog` instead.

---

### Step 2: Plan the Improvements

Before writing, list the changes you will make based on the audit's Priority Action List. Group them into:

**SEO Fixes**
- Title (if over 60 chars or missing keyword)
- Meta description (if failing guidelines)
- Heading tweaks (if needed)

**Content Quality Fixes**
- Remove all em-dashes — rewrite affected sentences
- Remove banned vocabulary — replace with plain alternatives
- Fix paragraphs over 4 sentences — split them
- Fix conclusion if too thin — expand to summarize key takeaways
- Fix introduction if it doesn't follow Hook → Problem → Preview
- Fix brand voice issues (too casual, too corporate, etc.)

**Freshness Fixes**
- Update all wrong pricing figures with correct USD values from the audit report
- Replace outdated statistics (pre-2024) with current data — use WebSearch if needed to find updated stats
- Fix any incorrect plan names, feature descriptions, or tool references

**Content Gap Additions** (Major Update only)
For each high or medium priority gap from the competitor analysis, add a new section:
- Write the new section following the article's existing tone and structure
- Insert it in the most logical position in the article flow
- Keep new sections consistent with the brand voice (`avada-commerce/brand-voice.md`)
- Add Avada product mentions naturally where relevant to new sections

---

### Step 3: Apply the Improvements

Work through each fix in order. For each change:
- Show the **original text** (or heading/section)
- Show the **revised text**
- Note which audit issue it addresses

Format each change as:

```
### Change: [Brief label — e.g. "Fix meta description"]
**Audit issue:** [e.g. "Meta description fails guidelines — too long, conversational"]

**Before:**
[original text]

**After:**
[revised text]
```

For new sections added (content gap fills), output the full section:

```
### New Section: [Section heading]
**Gap addressed:** [e.g. "Break-even upgrade analysis — missing vs. competitors"]
**Insert after:** [existing H2 heading it should follow]

[Full new section content in markdown]
```

---

### Step 4: Output the Full Revised Article

After all individual changes, output the complete revised article in the standard blog output format:

```
**Title:** [revised title, max 60 chars]
**Meta Description:** [145-155 chars, descriptive]
**Main Keyword:** [keyword]
**Blog Type:** [template used]

---

[Full revised article in markdown]
```

---

### Step 5: Self-Check

Before finalizing, verify:
- [ ] Title ≤ 60 characters, includes main keyword
- [ ] Meta description 145–155 characters, purely descriptive, no CTAs
- [ ] No em-dashes anywhere in the article
- [ ] No banned vocabulary (Leverage, Delve, Seamless, Ensure, Enable, etc.)
- [ ] All paragraphs ≤ 4 sentences
- [ ] All Shopify pricing figures match the audit's verified USD prices
- [ ] All statistics are 2024 or later, or flagged with source year
- [ ] Introduction follows Hook → Problem/Gap → Preview
- [ ] Conclusion summarizes key takeaways (no CTAs, no promo links)
- [ ] New sections match the article's tone and structure
- [ ] Avada products mentioned naturally where relevant
- [ ] Reading level approximately grade 7–8

---

### Step 6: Ask to Save

After outputting the revised article, ask:
> "Would you like me to save the revised article to the workspace?"

If yes: save as `content/blogs/[keyword-slug]/[keyword-slug].md`

---

## Notes
- If a pricing figure needs updating but the audit report didn't include the verified current price, use WebFetch on `https://www.shopify.com/pricing` to get the current USD price before making the change
- If a new section requires a statistic you don't have, use WebSearch to find a current (2024+) source before writing
- Do not add Avada product mentions to sections where they feel forced — only where genuinely relevant
- Preserve the author's personal examples and anecdotes (e.g. "I paid X for Shopify") — flag them for human review rather than deleting them, since they are brand voice assets
