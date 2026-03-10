# Skill: /ga4-insights

Fetch comprehensive GA4 behavioral and traffic data for a specific blog post URL. Use for content auditing, pre-improvement research, and performance tracking.

---

## Trigger

User runs `/ga4-insights` with a URL or blog post path.

---

## Inputs

- **URL** (required): Full URL or path, e.g. `https://avada.io/blog/shopify-pricing-plans/` or `/blog/shopify-pricing-plans/`
- **Days** (optional): Lookback period in days. Default: 90. Options: 30, 60, 90, 180, 365
- **Compare** (optional): If user says "compare" or "vs previous", run comparison against prior period

---

## Steps

### Step 1 — Run the GA4 script

Run the Python script with the provided URL:

```bash
python3 scripts/ga4_page_insights.py --url <URL> --days <DAYS>
```

If comparison requested, add `--compare`:

```bash
python3 scripts/ga4_page_insights.py --url <URL> --days <DAYS> --compare
```

### Step 2 — Present the report

Display the full output from the script, which includes:

**Traffic**
- Sessions, Active Users, New Users, Pageviews

**User Behavior**
- Avg session duration
- Engagement rate
- Bounce rate

**Scroll Behavior**
- % of users who reached 90% scroll depth (GA4 default scroll event)
- Note: if scroll data is missing, flag that scroll tracking may not be active

**Outbound Clicks**
- Top clicked links from the page (if click tracking is active)

**Traffic by Channel**
- Organic, Direct, Referral, Social, Email, etc.

**Monthly Trend**
- Session trend over the selected period

**Period Comparison** (if --compare used)
- Side-by-side delta for sessions, users, pageviews, bounce rate, engagement rate

### Step 3 — Interpret and flag for content action

After the raw data, add a brief interpretation section:

```
## Insights for Content Action

**Engagement:** [Good/Needs attention] — [1-2 sentence interpretation of avg duration + engagement rate]
**Scroll depth:** [X% reading to 90%] — [flag if low, suggest content improvements]
**Traffic trend:** [Growing/Declining/Stable] — [note if organic is underperforming]
**Bounce rate:** [X%] — [flag if >60%, suggest intro/CTA improvements]
**Top clicked links:** [What users are clicking on — signals intent or navigation gaps]
```

### Step 4 — Recommend next action

Based on the data, recommend one of:
- **Audit this post** → run `/audit-blog <URL>`
- **Improve engagement** → specific suggestions (better intro, stronger CTA, add visuals)
- **No action needed** → explain why metrics look healthy

---

## Data Notes

- Scroll depth uses GA4's default `scroll` event (triggers at 90% page depth)
- Click tracking requires GA4 enhanced measurement "Outbound clicks" to be enabled
- If either shows no data, note this in the report and suggest verifying in GA4 → Admin → Data Streams → Enhanced Measurement
- **Search clicks/impressions** (Google organic CTR) are NOT available via GA4 — those require Google Search Console API (future addition)
- All data is filtered to the exact page path provided

---

## Example Usage

```
/ga4-insights https://avada.io/blog/shopify-pricing-plans/
/ga4-insights /blog/cheapest-online-shopping-sites-in-usa/ --days 30
/ga4-insights https://avada.io/blog/shopify-pricing-plans/ compare last 60 days
```
