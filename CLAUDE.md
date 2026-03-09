# Avada Commerce - Claude Code Configuration

## Context Files

### Company (`avada-commerce/`)
- `company.md` - Overview, mission, strategy, reputation
- `products.md` - Full product ecosystem (SEO, Sales, Retention, Operations)
- `audience.md` - Target audience and business size
- `competitors.md` - Competitive landscape
- `brand-voice.md` - Tone, voice characteristics, good/bad examples
- `visual-identity.md` - Brand colors, typography, logo, visual system

## Skills
- `skills/write-blog.md` - Blog writing skill (`/write-blog`): workflow, writing guidelines, 12 blog templates, sample blog patterns
- `skills/audit-blog.md` - Full blog audit skill (`/audit-blog`): fetches live URL + Shopify pricing, runs all 3 audits, outputs unified report with action classification
- `skills/audit-seo.md` - SEO audit skill (`/audit-seo`): title, meta description, keyword placement, heading structure
- `skills/audit-content.md` - Content quality audit skill (`/audit-content`): brand voice, writing style, banned vocabulary, structure, Avada product mentions — automatically generates a proposed new outline if content structure score is below 7/10
- `skills/audit-freshness.md` - Freshness audit skill (`/audit-freshness`): compares article data vs live Shopify pricing page (USD only), flags outdated stats, runs competitor content gap analysis via WebSearch + WebFetch
- `skills/improve-blog.md` - Improvement skill (`/improve-blog`): surgical in-place fixes for Light Edit and Major Update articles — fixes SEO, style violations, pricing, and adds missing sections from competitor gap analysis
- `skills/rewrite-blog.md` - Rewrite skill (`/rewrite-blog`): full rewrite from scratch for Full Rewrite articles — uses audit findings as constraints, competitor gaps as brief, and write-blog.md as writing framework
