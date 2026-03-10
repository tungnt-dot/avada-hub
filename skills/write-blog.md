# Skill: Write Blog Post for Avada Commerce

## Usage
Trigger: `/write-blog`

## Instructions
When the user asks you to write a blog post, follow these steps:

### Step 1: Gather Input
Ask the user for:
1. **Main keyword** (required)
2. **Topic/angle** (required)
3. **Anything else?** (optional): secondary keywords, word count, specific Avada products to mention, or other notes

Then suggest a **blog type** based on the keyword and topic (How to, What is, List, Comparison, Pillar, Beginner's Guide, Tutorial, Problem-Solution, Trends, FAQ, Data-Driven, or Evergreen). Briefly explain why this type fits. Wait for user confirmation before writing.

### Step 2: Write the Article
- Select the matching template from the Blog Templates section below and follow its structure
- Follow ALL rules from the Writing Guidelines section below
- Follow tone and voice from `avada-commerce/brand-voice.md`
- Follow the AI Writing Style Guide at `avada-commerce/AI writing style/AI Writing Style Guide.md` for voice, quirks, and structure patterns
- Reference `avada-commerce/` files for accurate product names, target audience, and competitive context
- Match writing patterns from the Sample Blog Patterns section below
- Mention Avada products naturally where relevant (don't force it)

### Step 3: Output Format
```
**Title:** [max 60 chars, includes main keyword]
**Meta Description:** [145-155 chars, descriptive]
**Main Keyword:** [keyword]
**Blog Type:** [template used]

---

[Full blog content in markdown]
```

### Step 4: Self-Check
After writing, verify:
- [ ] Title under 60 characters, includes main keyword
- [ ] Meta description 145-155 characters, purely descriptive
- [ ] Keyword in title, headings, and first 100 words
- [ ] Structure matches the selected blog template
- [ ] Introduction follows the hook → problem/gap → preview pattern
- [ ] Key verdict or answer delivered early (not buried at the end)
- [ ] No banned vocabulary (see audit-content.md full list)
- [ ] No em-dashes or hyphens
- [ ] No cliché openings ("In today's fast-paced world...", "It's no secret...", etc.)
- [ ] No throat-clearing phrases ("In conclusion...", "It's important to note...")
- [ ] Numbers under ten spelled out ("five", not "5")
- [ ] "okay" not "ok" — "email" not "e-mail"
- [ ] Italics used for subtle emphasis, not bold overuse
- [ ] Specific tools/platforms named (not "various platforms")
- [ ] Claims backed by specific data or sources (not vague generalities)
- [ ] Major sections end with a short one-sentence impact paragraph
- [ ] Reading level around grade 7-8
- [ ] Paragraphs max 3-4 sentences, front-loaded with main idea
- [ ] Content scannable (lists, bolds, clear headings)
- [ ] Sources cited where needed
- [ ] Statistics from 2024 onward

---

## Writing Guidelines

### Blog Title
- Maximum 60 characters.
- Must include the main keyword.
- The keyword can be front-loaded or placed naturally depending on readability.
- Make the title clear, specific, and compelling.

### Meta Description
- 145–155 characters.
- Summarize what the blog covers. Be purely descriptive.
- Do not include CTAs like "Learn more" or "Find out how".

### Content Structure
- Follow the inverted pyramid: most important information first, extra details later.
- Make sure keywords appear in the title, headings, and the first 100 words.
- Headings and sections addressing the same thing should be grouped together.
- Each paragraph should contain a maximum of 3-4 sentences.
- Include conjunction and transitional phrases in each paragraph.
- Make content scannable. Use lists whenever possible.
- Use bolds and underlines to highlight key points.
- After each H2 heading that contains H3 subheadings, add a transition sentence (1-2 sentences) before the first H3. This bridges the section topic to its subtopics and keeps the reading flow smooth.

### SEO Rules
- Don't stuff keywords. Use them in a natural way.
- When writing about an 'entity', try telling Google some of its 'attributes' or how it's related to other 'entities' (for example, what 'attributes' do they share? Do they fall under the same category? Etc.)
- Cite/link to authoritative sources when mentioning statistics, quotes, or references.
- Use recent data (2024 onward). Avoid outdated statistics. If no recent data is available, clearly state the year of the source.
- For fact-based articles, don't give your opinion.

### Tone and Voice
- Use plain English and simple words.
- Use first person.
- Get straight to the point.
- Answer questions in a direct way, especially for "what is" questions. Don't make complex analogies or counter-questions.
- Use personal experience, anecdotes and opinions.
- Keep the grade reading level around 7-8.

### Sentence and Paragraph Rules
- Sentences should be as short as possible and as long as necessary. Short sentences are better.
- Simple sentence structure is better.
- Vary sentence length.
- Use conjunctions and complex sentences from time to time.
- Ask a question or two.
- Limit punctuation.
- Avoid use em-dash or hyphen.

### Formatting
- Use lists where appropriate.
- **Avoid the structure "[Keyword/Concept]: [Short Explanation]"** (like POS: Connecting Your Physical Store) because it can feel stiff, generic, or AI-like.
- Avoid complex industry jargon as much as possible, but use them as much as necessary (e.g. when talking about definitions, linking terms, or covering different content angles).

### Banned Vocabulary
Avoid these words too much:
Leverage, Delve, Meticulous, Elevate, Revolutionize, Holistic, Empower, Realm, Seamless, Enhance, Reinvent, Fast-paced, Embark, Reimagined, Game-changer, Enable, Redefine, Unprecedented, Embrace, Harness the power, Next-level, Ensure, Navigate, Best-in-class, Dive into, Disruptive, Emerge, Deep dive, Unleash, Synergy, Ever-evolving, Unveil, Mission-critical, Unlock, Paradigm shift, Tailored.

### Final Check
- Always check for typos after finishing writing.

---

## Blog Templates

Choose the template that matches the article type.

### 1. "How to" Post
Best for: Shopify tutorials, setup guides, step-by-step processes.

**Structure:**
- **Introduction** (100-200 words): Hook with current context/stats, state the problem, preview what the post covers.
- **What is [Term] and Why Does It Matter?** Define the concept briefly if needed.
- **How to [Task]**: Break into numbered steps, each with its own subheading. Be precise and actionable.
- **Tips and Reminders** (optional): 3-5 practical tips or common pitfalls.
- **Conclusion**: Summarize key takeaways.

### 2. "What Is" Post
Best for: Explaining ecommerce concepts (retention, AOV, SEO, upselling, etc.).

**Structure:**
- **Introduction** (100-200 words): Hook with context, explain why the topic matters now.
- **What is [Term]?** Direct definition in 50-60 words (featured snippet target), then expand with more context.
- **Why is [Term] Important?** Practical impact on ecommerce business. Include stats if available.
- **Examples of [Term]** (optional): 3-5 real-world examples.
- **Tips for [Term]** (optional): 3-5 actionable tips.
- **Conclusion**: Summarize the key takeaway.

### 3. List Post
Best for: Tips, tools, examples, strategies, statistics roundups.

**Structure:**
- **Introduction** (100-200 words): Hook with context, state who this list is for, preview the count.
- **Why is [Term] Important?** (optional): Brief context if the topic needs it.
- **[# Items] for [Term]**: Each item gets its own subheading with 2-3 sentences (long lists) or 2-3 paragraphs (short lists).
- **Conclusion**: Highlight the common thread or suggest next steps.

### 4. Comparison Post
Best for: App comparisons, tool evaluations, X vs Y articles.

**Structure:**
- **Introduction** (100-200 words): Hook with why this comparison matters, preview what will be compared.
- **Overview of [X and Y]**: What they are, who they are for, primary value.
- **Key Features and Benefits**: Use table or bullet list for side-by-side comparison.
- **Pros and Cons**: Strengths and weaknesses of each option.
- **When to Choose [X] vs [Y]**: Scenario-based recommendations.
- **Conclusion**: Clear summary with recommendation if appropriate.

### 5. Pillar Post
Best for: Comprehensive guides for topical authority SEO (2000-5000 words).

**Structure:**
- **Introduction** (100-200 words): Explain topic significance, preview the full scope.
- **What is [Term] and Why Does It Matter?**
- **Terms to Know** (optional): Key vocabulary.
- **How to [Task/Term]**: Step-by-step core content.
- **Examples of [Term]**: Real-world applications.
- **Tips and Best Practices**
- **Resources for [Term]** (optional): Additional tools, blogs, references.
- **Conclusion**: Summarize and encourage further exploration.

Note: Link to supporting cluster posts throughout. Each section should be substantial enough to stand alone.

### 6. Beginner's Guide Post
Best for: New Shopify merchants, ecommerce beginners learning a concept.

**Structure:**
- **Introduction** (100-200 words): Hook with why this matters for beginners, preview the guide.
- **What is [Term]?** Simple, beginner-friendly definition with example.
- **Why [Term] Matters**: Relevance to their store or business growth.
- **How to Get Started with [Term]**: Clear steps with subheadings (Step 1, Step 2...).
- **Common Mistakes to Avoid** (optional): 3-5 beginner pitfalls.
- **Conclusion**: Encourage first steps, reinforce that it is achievable.

### 7. Tutorial Post
Best for: Detailed technical walkthroughs, product setup guides.

**Structure:**
- **Introduction** (100-200 words): What this tutorial teaches and who it is for.
- **What You'll Need** (optional): Tools, prerequisites, access requirements.
- **Step-by-Step Guide to [Task]**: Numbered steps, each with subheading. Include screenshots/visuals references where helpful.
- **Tips and Best Practices** (optional): Extra advice for better results.
- **Troubleshooting** (optional): Common issues and solutions.
- **Conclusion**: Summarize the process and encourage applying what they learned.

### 8. Problem-Solution Post
Best for: Addressing merchant pain points (low traffic, cart abandonment, low retention).

**Structure:**
- **Introduction** (100-200 words): Hook with the problem's impact, use stats if available.
- **The Problem: What's Going Wrong?** Describe in relatable terms with data.
- **The Solution: How to Fix It**: Step-by-step actionable guide.
- **Tools and Resources to Help** (optional): Relevant tools including Avada products where natural.
- **Common Mistakes to Avoid** (optional): Pitfalls when addressing this problem.
- **Conclusion**: Reinforce the importance of solving this and encourage action.

### 9. Trends Post
Best for: Yearly ecommerce trends, industry shift analysis.

**Structure:**
- **Introduction** (100-200 words): Why staying ahead of trends matters, who this is for.
- **What's Driving These Trends?** Market forces, tech changes, consumer behavior shifts.
- **Key Trends for [Year/Topic]**: Each trend gets a subheading with explanation, data, and impact.
- **How to Adapt to These Trends**: Actionable advice for merchants.
- **Conclusion**: Encourage proactive action.

### 10. FAQ Post
Best for: Common merchant questions about a topic, product category, or concept.

**Structure:**
- **Introduction** (100-200 words): What questions this post answers and why.
- **FAQs About [Topic]**: Q&A format. Each question as a subheading, answer in concise paragraphs.
- **Conclusion**: Summary of key answers, invite further questions.

### 11. Data-Driven Post
Best for: Statistics roundups, research summaries, evidence-based analysis.

**Structure:**
- **Introduction** (100-200 words): Why this data matters, source overview.
- **The Data**: Key data points with subheadings, include chart/graph references.
- **What This Means for [Audience]**: Interpret data into actionable insights.
- **How to Act on This Data**: Specific steps or strategies based on findings.
- **Conclusion**: Summarize key findings and implications.

### 12. Evergreen Post
Best for: Foundational ecommerce content that stays relevant long-term.

**Structure:**
- **Introduction** (100-200 words): Why this topic is timeless and important.
- **What is [Term/Topic]?** Clear definition with examples.
- **Why [Topic] Matters**: Long-term relevance to ecommerce.
- **How to [Achieve/Do/Understand Topic]**: Actionable steps with subheadings.
- **Common Mistakes to Avoid** (optional): Universal pitfalls.
- **Conclusion**: Reinforce long-term value, encourage action.

### Introduction Pattern (All Templates)

Every blog post introduction should follow this pattern:
1. **Hook with current context**: Start with a real-world situation, trend, or statistic related to the topic. Make it feel timely and relevant.
2. **State the problem or gap**: Point out what merchants are doing wrong or overlooking.
3. **Preview the content**: Briefly state what the article covers.

Statistics in the introduction are encouraged but optional. The introduction should be flexible in length but typically 100-200 words.

### Conclusion Pattern (All Templates)

Keep the conclusion short. Summarize the key takeaways from the article. No CTAs, no promotional links, no questions. Just a clear recap of what the reader learned.

---

## Sample Blog Patterns

Based on 9 published articles from avada.io/blog. Use these patterns as reference when writing new content.

### Articles Analyzed

| # | Article | Type | Word Count |
|---|---------|------|------------|
| 1 | 450+ Food Business Name Ideas | List | ~3,500 |
| 2 | 500+ Pet Store Names | List | ~3,000 |
| 3 | 20+ Cheapest Online Shopping Sites in USA | List | ~2,500 |
| 4 | 500+ Ecommerce Business Name Ideas | List | ~3,500 |
| 5 | Top 5 Online Selling Platforms in India Without GST | List | ~2,100 |
| 6 | 300+ Beauty Business Name Ideas | List | ~3,300 |
| 7 | 500+ T-Shirt Brand Names | List | ~2,600 |
| 8 | 500 Clothing Brand Name Ideas | List | ~2,000 |
| 9 | 400+ Flower Shop Names | List | ~2,800 |

### Title Patterns
- Numbers front-loaded: "450+", "500+", "300+", "20+"
- Action or benefit words: "to Stand Out", "to Shine", "to Inspire You", "for Every Style"
- Year included when relevant: "in 2026"
- Format: **[Number]+ [Adjective] [Topic] [Benefit Phrase] [Year]**

### Content Structure (List Posts)
Consistent structure across all naming articles:
1. Introduction
2. Why [Topic] Matters / Importance section
3. Main list organized by categories (style, niche, audience, model)
4. Tips for choosing / How to choose
5. Case studies (2-3 real brand examples)
6. Tools and techniques
7. FAQ section
8. Conclusion

### Writing Style Observations
- **Tone**: Conversational, encouraging, authoritative but accessible
- **Person**: First person ("I", "my experience", "Trust me")
- **Reader address**: Direct ("you", "your brand", "your store")
- **Sentence length**: Short and varied
- **Paragraphs**: 2-4 sentences max
- **Bold text** for key concepts and emphasis
- **Lists** used extensively for scannability

### FAQ Section Pattern
- 3-5 questions per article
- Q&A format with question as subheading
- Concise answers (2-4 sentences each)
- Targets featured snippet opportunities

### Avada Product Mentions
- Natural integration, not forced
- Products mentioned only when genuinely relevant to the topic
- Related Avada blog posts cross-linked

### Note
All 9 samples are List Posts. Other blog types (How-to, What Is, Comparison, Tutorial, Problem-Solution) should follow the templates above while maintaining the tone and style patterns documented here.
