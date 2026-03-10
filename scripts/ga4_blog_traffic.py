"""
GA4 Blog Traffic Exporter
Pulls traffic data for all /blog/ pages from GA4 and exports to CSV.

Usage:
    python3 scripts/ga4_blog_traffic.py
    python3 scripts/ga4_blog_traffic.py --days 90
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


def parse_args():
    parser = argparse.ArgumentParser(description="Export GA4 blog traffic to CSV")
    parser.add_argument(
        "--days", type=int, default=90, help="Number of days to look back (default: 90)"
    )
    parser.add_argument("--output", type=str, default=None, help="Output CSV filename")
    return parser.parse_args()


def main():
    args = parse_args()

    end = date.today()
    start = end - timedelta(days=args.days)
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")

    print(f"Fetching GA4 data: {start_str} → {end_str} (last {args.days} days)")
    print(f"Property ID: {PROPERTY_ID}")

    client = get_client()
    response = run_report(client, start_str, end_str)

    rows = []
    for row in response.rows:
        page_path = row.dimension_values[0].value
        page_title = row.dimension_values[1].value
        sessions = int(row.metric_values[0].value)
        users = int(row.metric_values[1].value)
        pageviews = int(row.metric_values[2].value)
        avg_session_duration = round(float(row.metric_values[3].value), 1)
        bounce_rate = round(float(row.metric_values[4].value) * 100, 1)
        engagement_rate = round(float(row.metric_values[5].value) * 100, 1)

        rows.append({
            "page_path": page_path,
            "page_title": page_title,
            "sessions": sessions,
            "users": users,
            "pageviews": pageviews,
            "avg_session_duration_sec": avg_session_duration,
            "bounce_rate_pct": bounce_rate,
            "engagement_rate_pct": engagement_rate,
            "date_range": f"{start_str} to {end_str}",
        })

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = args.output or f"blog_traffic_{start_str}_to_{end_str}.csv"
    output_path = os.path.join(OUTPUT_DIR, filename)

    fieldnames = [
        "page_path", "page_title", "sessions", "users", "pageviews",
        "avg_session_duration_sec", "bounce_rate_pct", "engagement_rate_pct", "date_range",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✓ {len(rows)} blog pages exported to:")
    print(f"  {output_path}")
    print(f"\nTop 10 pages by sessions:")
    print(f"  {'Sessions':>8}  {'Pageviews':>9}  {'Bounce%':>7}  Path")
    print(f"  {'-'*8}  {'-'*9}  {'-'*7}  {'-'*40}")
    for r in rows[:10]:
        print(f"  {r['sessions']:>8}  {r['pageviews']:>9}  {r['bounce_rate_pct']:>6}%  {r['page_path']}")


if __name__ == "__main__":
    main()
