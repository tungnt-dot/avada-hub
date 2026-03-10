"""
GA4 Blog Traffic Exporter
Pulls traffic data for all /blog/ pages from GA4 and exports to CSV.

Usage:
    python3 scripts/ga4_blog_traffic.py
    python3 scripts/ga4_blog_traffic.py --days 90
    python3 scripts/ga4_blog_traffic.py --days 90 --compare
    python3 scripts/ga4_blog_traffic.py --days 30 --output my_report.csv
"""

import argparse
import csv
import os
from datetime import date, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    FilterExpression,
    Filter,
    RunReportRequest,
    OrderBy,
)
from google.oauth2 import service_account

# ── Config ────────────────────────────────────────────────────────────────────
PROPERTY_ID = "358883563"
CREDENTIALS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../avada-commerce/GA4 json/tonal-asset-489802-h0-0e812b83f650.json",
)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../Content-SEO Plan/ga4-exports")
# ─────────────────────────────────────────────────────────────────────────────


def get_client():
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/analytics.readonly"],
    )
    return BetaAnalyticsDataClient(credentials=credentials)


def run_report(client, start_date: str, end_date: str):
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[
            Dimension(name="pagePath"),
            Dimension(name="pageTitle"),
        ],
        metrics=[
            Metric(name="sessions"),
            Metric(name="activeUsers"),
            Metric(name="screenPageViews"),
            Metric(name="averageSessionDuration"),
            Metric(name="bounceRate"),
            Metric(name="engagementRate"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="pagePath",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.BEGINS_WITH,
                    value="/blog/",
                ),
            )
        ),
        order_bys=[
            OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)
        ],
        limit=500,
    )
    return client.run_report(request)


def parse_response(response) -> dict:
    """Parse GA4 response into a dict keyed by pagePath."""
    rows = {}
    for row in response.rows:
        page_path = row.dimension_values[0].value
        rows[page_path] = {
            "page_title": row.dimension_values[1].value,
            "sessions": int(row.metric_values[0].value),
            "users": int(row.metric_values[1].value),
            "pageviews": int(row.metric_values[2].value),
            "avg_session_duration_sec": round(float(row.metric_values[3].value), 1),
            "bounce_rate_pct": round(float(row.metric_values[4].value) * 100, 1),
            "engagement_rate_pct": round(float(row.metric_values[5].value) * 100, 1),
        }
    return rows


def pct_change(current, prior) -> str:
    if prior == 0:
        return "N/A"
    delta = ((current - prior) / prior) * 100
    sign = "+" if delta >= 0 else ""
    return f"{sign}{delta:.1f}%"


def priority_score(sessions, sessions_delta_pct, bounce_rate, engagement_rate) -> int:
    """
    Lower score = higher priority to fix.
    Combines traffic decline, bounce rate, and engagement into a 0–100 score.
    """
    score = 50

    # Traffic trend: heavy weight
    if sessions_delta_pct is not None:
        if sessions_delta_pct <= -50:
            score -= 30
        elif sessions_delta_pct <= -30:
            score -= 20
        elif sessions_delta_pct <= -10:
            score -= 10
        elif sessions_delta_pct >= 20:
            score += 15

    # Bounce rate: high bounce = needs work
    if bounce_rate >= 70:
        score -= 15
    elif bounce_rate >= 55:
        score -= 8
    elif bounce_rate <= 35:
        score += 10

    # Engagement rate: low = needs work
    if engagement_rate <= 30:
        score -= 10
    elif engagement_rate >= 60:
        score += 8

    # Volume: tiny pages are lower priority
    if sessions < 50:
        score -= 5
    elif sessions >= 500:
        score += 5

    return max(0, min(100, score))


def parse_args():
    parser = argparse.ArgumentParser(description="Export GA4 blog traffic to CSV")
    parser.add_argument(
        "--days", type=int, default=90, help="Number of days to look back (default: 90)"
    )
    parser.add_argument(
        "--compare", action="store_true", help="Compare against prior period"
    )
    parser.add_argument("--output", type=str, default=None, help="Output CSV filename")
    return parser.parse_args()


def main():
    args = parse_args()

    end = date.today()
    start = end - timedelta(days=args.days)
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")

    prior_end = start - timedelta(days=1)
    prior_start = prior_end - timedelta(days=args.days)
    prior_start_str = prior_start.strftime("%Y-%m-%d")
    prior_end_str = prior_end.strftime("%Y-%m-%d")

    print(f"Fetching GA4 data: {start_str} → {end_str} (last {args.days} days)")
    if args.compare:
        print(f"Prior period:      {prior_start_str} → {prior_end_str}")
    print(f"Property ID: {PROPERTY_ID}")

    client = get_client()
    current_data = parse_response(run_report(client, start_str, end_str))

    prior_data = {}
    if args.compare:
        print("Fetching prior period...")
        prior_data = parse_response(run_report(client, prior_start_str, prior_end_str))

    # Build merged rows
    rows = []
    for page_path, curr in current_data.items():
        prior = prior_data.get(page_path, {})
        prior_sessions = prior.get("sessions", 0)
        curr_sessions = curr["sessions"]

        delta_pct_str = pct_change(curr_sessions, prior_sessions) if args.compare else "—"
        delta_pct_val = None
        if args.compare and prior_sessions > 0:
            delta_pct_val = ((curr_sessions - prior_sessions) / prior_sessions) * 100

        pscore = priority_score(
            curr_sessions,
            delta_pct_val,
            curr["bounce_rate_pct"],
            curr["engagement_rate_pct"],
        )

        rows.append({
            "priority_score": pscore,
            "page_path": page_path,
            "page_title": curr["page_title"],
            "sessions": curr_sessions,
            "prior_sessions": prior_sessions if args.compare else "",
            "sessions_delta": delta_pct_str,
            "users": curr["users"],
            "pageviews": curr["pageviews"],
            "avg_session_duration_sec": curr["avg_session_duration_sec"],
            "bounce_rate_pct": curr["bounce_rate_pct"],
            "engagement_rate_pct": curr["engagement_rate_pct"],
            "date_range": f"{start_str} to {end_str}",
        })

    # Sort by priority (lowest score = highest urgency)
    rows.sort(key=lambda r: r["priority_score"])

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = args.output or f"blog_traffic_{start_str}_to_{end_str}.csv"
    output_path = os.path.join(OUTPUT_DIR, filename)

    fieldnames = [
        "priority_score", "page_path", "page_title", "sessions", "prior_sessions",
        "sessions_delta", "users", "pageviews", "avg_session_duration_sec",
        "bounce_rate_pct", "engagement_rate_pct", "date_range",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✓ {len(rows)} blog pages exported to:")
    print(f"  {output_path}")

    # ── Priority table ─────────────────────────────────────────────────────────
    print(f"\n{'='*80}")
    print(f"  CONTENT PRIORITY QUEUE  (sorted by urgency — fix these first)")
    print(f"{'='*80}")
    print(f"  {'#':>3}  {'Score':>5}  {'Sessions':>8}  {'Delta':>7}  {'Bounce':>6}  {'Engage':>6}  Path")
    print(f"  {'─'*3}  {'─'*5}  {'─'*8}  {'─'*7}  {'─'*6}  {'─'*6}  {'─'*35}")

    for i, r in enumerate(rows[:20], 1):
        urgency = "🔴" if r["priority_score"] < 35 else ("🟡" if r["priority_score"] < 55 else "🟢")
        delta = r["sessions_delta"] if args.compare else "—"
        print(
            f"  {i:>3}  {urgency} {r['priority_score']:>2}  "
            f"{r['sessions']:>8}  {delta:>7}  "
            f"{r['bounce_rate_pct']:>5}%  {r['engagement_rate_pct']:>5}%  "
            f"{r['page_path'][:50]}"
        )

    print(f"\n  🔴 = High urgency (score < 35) | 🟡 = Medium (35–54) | 🟢 = Healthy (55+)")
    print(f"  Use /audit-blog on 🔴 pages first.\n")


if __name__ == "__main__":
    main()
