# Avada Commerce - Claude Code Configuration

## Context Files

### Company (`avada-commerce/`)
- `company.md` - Overview, mission, strategy, reputation
- `products.md` - Full product ecosystem (SEO, Sales, Retention, Operations)
- `audience.md` - Target audience and business size
- `competitors.md` - Competitive landscape
- `brand-voice.md` - Tone, voice characteristics, good/bad examples
- `visual-identity.md` - Brand colors, typography, logo, visual system
- `AI writing style/AI Writing Style Guide.md` - Detailed writing voice, personal quirks, banned phrases, structure patterns, and section-by-section writing process
- `dataforseo-credentials.json` - DataForSEO API credentials (gitignored) — used by `scripts/dataforseo_serp.py` for SERP ranking, keyword volume, and competitor data

## Skills
- `skills/write-blog.md` - Blog writing skill (`/write-blog`): workflow, writing guidelines, 12 blog templates, sample blog patterns
- `skills/audit-blog.md` - Full blog audit skill (`/audit-blog`): fetches live URL + GA4 data + Shopify pricing + competitor gaps, runs SEO / content quality / freshness audits inline, outputs unified report with action classification
- `skills/improve-blog.md` - Improvement skill (`/improve-blog`): surgical in-place fixes for Light Edit and Major Update articles — fixes SEO, style violations, pricing, and adds missing sections from competitor gap analysis
- `skills/rewrite-blog.md` - Rewrite skill (`/rewrite-blog`): full rewrite from scratch for Full Rewrite articles — uses audit findings as constraints, competitor gaps as brief, and write-blog.md as writing framework
- `skills/ga4-insights.md` - GA4 insights skill (`/ga4-insights`): pulls traffic, user behavior, scroll depth, click events, channel breakdown, and monthly trend for a given URL — with optional period comparison
- `skills/prioritize-content.md` - Content priority skill (`/prioritize-content`): runs GA4 across all blog pages, scores each by traffic decline + bounce + engagement, outputs a priority queue of articles to audit next
