"""
GA4 Page Insights
Pulls comprehensive behavioral + traffic data for a specific page URL.

Usage:
    python3 scripts/ga4_page_insights.py --url /blog/shopify-pricing-plans/
    python3 scripts/ga4_page_insights.py --url /blog/shopify-pricing-plans/ --days 90
    python3 scripts/ga4_page_insights.py --url /blog/shopify-pricing-plans/ --compare
"""

import argparse
import json
import os
from datetime import date, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    FilterExpression,
    FilterExpressionList,
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
# ─────────────────────────────────────────────────────────────────────────────


def get_client():
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/analytics.readonly"],
    )
    return BetaAnalyticsDataClient(credentials=credentials)


def normalize_path(url: str) -> str:
    """Strip domain to get just the path, e.g. /blog/shopify-pricing-plans/"""
    url = url.strip()
    for prefix in ["https://avada.io", "http://avada.io", "https://www.avada.io"]:
        if url.startswith(prefix):
            url = url[len(prefix):]
    if not url.startswith("/"):
        url = "/" + url
    return url


def page_filter(page_path: str) -> FilterExpression:
    return FilterExpression(
        filter=Filter(
            field_name="pagePath",
            string_filter=Filter.StringFilter(
                match_type=Filter.StringFilter.MatchType.EXACT,
                value=page_path,
            ),
        )
    )


def get_traffic_metrics(client, page_path: str, start_date: str, end_date: str) -> dict:
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="pagePath"), Dimension(name="pageTitle")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="activeUsers"),
            Metric(name="newUsers"),
            Metric(name="screenPageViews"),
            Metric(name="averageSessionDuration"),
            Metric(name="bounceRate"),
            Metric(name="engagementRate"),
            Metric(name="userEngagementDuration"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=page_filter(page_path),
    )
    response = client.run_report(request)
    if not response.rows:
        return {}
    row = response.rows[0]
    return {
        "page_path": row.dimension_values[0].value,
        "page_title": row.dimension_values[1].value,
        "sessions": int(row.metric_values[0].value),
        "active_users": int(row.metric_values[1].value),
        "new_users": int(row.metric_values[2].value),
        "pageviews": int(row.metric_values[3].value),
        "avg_session_duration_sec": round(float(row.metric_values[4].value), 1),
        "bounce_rate_pct": round(float(row.metric_values[5].value) * 100, 1),
        "engagement_rate_pct": round(float(row.metric_values[6].value) * 100, 1),
        "total_engagement_duration_sec": round(float(row.metric_values[7].value), 1),
    }


def get_scroll_data(client, page_path: str, start_date: str, end_date: str) -> dict:
    """GA4 fires a 'scroll' event when user reaches 90% of the page."""
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="pagePath"), Dimension(name="eventName")],
        metrics=[Metric(name="eventCount"), Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=FilterExpression(
            and_group=FilterExpressionList(
                expressions=[
                    page_filter(page_path),
                    FilterExpression(
                        filter=Filter(
                            field_name="eventName",
                            string_filter=Filter.StringFilter(
                                match_type=Filter.StringFilter.MatchType.EXACT,
                                value="scroll",
                            ),
                        )
                    ),
                ]
            )
        ),
    )
    response = client.run_report(request)
    if not response.rows:
        return {"scroll_events": 0, "scroll_users": 0}
    row = response.rows[0]
    return {
        "scroll_events": int(row.metric_values[0].value),
        "scroll_users": int(row.metric_values[1].value),
    }


def get_click_events(client, page_path: str, start_date: str, end_date: str) -> list:
    """Get outbound click events from the page."""
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[
            Dimension(name="pagePath"),
            Dimension(name="eventName"),
            Dimension(name="linkUrl"),
        ],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=FilterExpression(
            and_group=FilterExpressionList(
                expressions=[
                    page_filter(page_path),
                    FilterExpression(
                        filter=Filter(
                            field_name="eventName",
                            string_filter=Filter.StringFilter(
                                match_type=Filter.StringFilter.MatchType.EXACT,
                                value="click",
                            ),
                        )
                    ),
                ]
            )
        ),
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="eventCount"), desc=True)],
        limit=10,
    )
    response = client.run_report(request)
    results = []
    for row in response.rows:
        results.append({
            "link_url": row.dimension_values[2].value,
            "click_count": int(row.metric_values[0].value),
        })
    return results


def get_traffic_by_channel(client, page_path: str, start_date: str, end_date: str) -> list:
    """Sessions broken down by traffic source/channel."""
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[
            Dimension(name="pagePath"),
            Dimension(name="sessionDefaultChannelGroup"),
        ],
        metrics=[Metric(name="sessions"), Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=page_filter(page_path),
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    )
    response = client.run_report(request)
    return [
        {
            "channel": row.dimension_values[1].value,
            "sessions": int(row.metric_values[0].value),
            "users": int(row.metric_values[1].value),
        }
        for row in response.rows
    ]


def get_traffic_over_time(client, page_path: str, start_date: str, end_date: str) -> list:
    """Monthly sessions trend."""
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="pagePath"), Dimension(name="yearMonth")],
        metrics=[Metric(name="sessions"), Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimension_filter=page_filter(page_path),
        order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="yearMonth"))],
    )
    response = client.run_report(request)
    return [
        {
            "month": row.dimension_values[1].value,
            "sessions": int(row.metric_values[0].value),
            "pageviews": int(row.metric_values[1].value),
        }
        for row in response.rows
    ]


def fmt_duration(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m}m {s}s"


def print_report(data: dict, period_label: str):
    traffic = data.get("traffic", {})
    scroll = data.get("scroll", {})
    clicks = data.get("clicks", [])
    channels = data.get("channels", [])
    trend = data.get("trend", [])

    print(f"\n{'='*60}")
    print(f"  GA4 INSIGHTS — {period_label}")
    print(f"{'='*60}")

    if not traffic:
        print("  No data found for this page in the selected period.")
        return

    print(f"\n  Page:  {traffic.get('page_title', 'N/A')}")
    print(f"  Path:  {traffic.get('page_path', 'N/A')}")

    print(f"\n── TRAFFIC ──────────────────────────────────────────")
    print(f"  Sessions:       {traffic['sessions']:,}")
    print(f"  Active Users:   {traffic['active_users']:,}")
    print(f"  New Users:      {traffic['new_users']:,}  ({round(traffic['new_users']/max(traffic['active_users'],1)*100)}% of users)")
    print(f"  Pageviews:      {traffic['pageviews']:,}")

    print(f"\n── USER BEHAVIOR ────────────────────────────────────")
    print(f"  Avg Session Duration:  {fmt_duration(traffic['avg_session_duration_sec'])}")
    print(f"  Engagement Rate:       {traffic['engagement_rate_pct']}%")
    print(f"  Bounce Rate:           {traffic['bounce_rate_pct']}%")

    # Scroll depth (GA4 default = 90% scroll)
    if scroll["scroll_users"] > 0 and traffic["active_users"] > 0:
        scroll_pct = round(scroll["scroll_users"] / traffic["active_users"] * 100, 1)
        print(f"\n── SCROLL BEHAVIOR ──────────────────────────────────")
        print(f"  Users reaching 90% scroll depth: {scroll['scroll_users']:,} ({scroll_pct}% of users)")
        print(f"  Scroll events fired:              {scroll['scroll_events']:,}")
    else:
        print(f"\n── SCROLL BEHAVIOR ──────────────────────────────────")
        print(f"  No scroll event data found (may not be tracked or no 90% scroll events)")

    # Click events
    if clicks:
        print(f"\n── TOP OUTBOUND CLICKS ──────────────────────────────")
        for c in clicks:
            print(f"  {c['click_count']:>4}x  {c['link_url']}")
    else:
        print(f"\n── TOP OUTBOUND CLICKS ──────────────────────────────")
        print(f"  No click event data found")

    # Traffic channels
    if channels:
        print(f"\n── TRAFFIC BY CHANNEL ───────────────────────────────")
        for ch in channels:
            print(f"  {ch['sessions']:>6} sessions  {ch['channel']}")

    # Monthly trend
    if trend:
        print(f"\n── MONTHLY TREND ────────────────────────────────────")
        for t in trend:
            month = f"{t['month'][:4]}-{t['month'][4:]}"
            bar = "█" * min(int(t["sessions"] / max(1, max(x["sessions"] for x in trend)) * 30), 30)
            print(f"  {month}  {bar} {t['sessions']:,}")

    print(f"\n{'='*60}\n")


def fetch_all(client, page_path: str, start_date: str, end_date: str) -> dict:
    return {
        "traffic": get_traffic_metrics(client, page_path, start_date, end_date),
        "scroll": get_scroll_data(client, page_path, start_date, end_date),
        "clicks": get_click_events(client, page_path, start_date, end_date),
        "channels": get_traffic_by_channel(client, page_path, start_date, end_date),
        "trend": get_traffic_over_time(client, page_path, start_date, end_date),
    }


def parse_args():
    parser = argparse.ArgumentParser(description="GA4 insights for a specific page")
    parser.add_argument("--url", required=True, help="Page URL or path (e.g. /blog/shopify-pricing-plans/ or full URL)")
    parser.add_argument("--days", type=int, default=90, help="Days to look back (default: 90)")
    parser.add_argument("--compare", action="store_true", help="Compare current period vs previous period")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of formatted report")
    return parser.parse_args()


def main():
    args = parse_args()
    page_path = normalize_path(args.url)

    end = date.today()
    start = end - timedelta(days=args.days)
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")

    client = get_client()

    print(f"Fetching GA4 insights for: {page_path}")
    print(f"Period: {start_str} → {end_str} (last {args.days} days)")

    current_data = fetch_all(client, page_path, start_str, end_str)

    if args.json:
        result = {"current": {"start": start_str, "end": end_str, "data": current_data}}
        if args.compare:
            prev_end = start - timedelta(days=1)
            prev_start = prev_end - timedelta(days=args.days)
            prev_data = fetch_all(client, page_path, prev_start.strftime("%Y-%m-%d"), prev_end.strftime("%Y-%m-%d"))
            result["previous"] = {"start": prev_start.strftime("%Y-%m-%d"), "end": prev_end.strftime("%Y-%m-%d"), "data": prev_data}
        print(json.dumps(result, indent=2))
        return

    print_report(current_data, f"Last {args.days} days ({start_str} to {end_str})")

    if args.compare:
        prev_end = start - timedelta(days=1)
        prev_start = prev_end - timedelta(days=args.days)
        prev_data = fetch_all(client, page_path, prev_start.strftime("%Y-%m-%d"), prev_end.strftime("%Y-%m-%d"))
        print_report(prev_data, f"Previous {args.days} days ({prev_start.strftime('%Y-%m-%d')} to {prev_end.strftime('%Y-%m-%d')})")

        # Delta summary
        ct = current_data.get("traffic", {})
        pt = prev_data.get("traffic", {})
        if ct and pt:
            def delta(curr, prev):
                if prev == 0:
                    return "N/A"
                change = ((curr - prev) / prev) * 100
                sign = "+" if change >= 0 else ""
                return f"{sign}{change:.1f}%"

            print(f"── PERIOD COMPARISON ────────────────────────────────")
            print(f"  Sessions:        {pt['sessions']:,} → {ct['sessions']:,}  ({delta(ct['sessions'], pt['sessions'])})")
            print(f"  Users:           {pt['active_users']:,} → {ct['active_users']:,}  ({delta(ct['active_users'], pt['active_users'])})")
            print(f"  Pageviews:       {pt['pageviews']:,} → {ct['pageviews']:,}  ({delta(ct['pageviews'], pt['pageviews'])})")
            print(f"  Bounce Rate:     {pt['bounce_rate_pct']}% → {ct['bounce_rate_pct']}%")
            print(f"  Engagement Rate: {pt['engagement_rate_pct']}% → {ct['engagement_rate_pct']}%")
            print()


if __name__ == "__main__":
    main()
