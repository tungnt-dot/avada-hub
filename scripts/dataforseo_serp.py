"""
DataForSEO SERP Research
Pulls keyword rankings, search volume, difficulty, and SERP features for auditing.

Usage:
    python3 scripts/dataforseo_serp.py --keyword "shopify pricing plans"
    python3 scripts/dataforseo_serp.py --keyword "shopify pricing plans" --url https://avada.io/blog/shopify-pricing-plans/
    python3 scripts/dataforseo_serp.py --keyword "shopify pricing plans" --top 20
"""

import argparse
import json
import os
import http.client
import base64
from urllib.parse import urlparse

# ── Config ────────────────────────────────────────────────────────────────────
CREDENTIALS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../avada-commerce/dataforseo-credentials.json",
)
LOCATION_CODE = 2840   # United States
LANGUAGE_CODE = "en"
# ─────────────────────────────────────────────────────────────────────────────


def get_credentials():
    with open(CREDENTIALS_PATH) as f:
        creds = json.load(f)
    token = base64.b64encode(f"{creds['login']}:{creds['password']}".encode()).decode()
    return token


def api_post(endpoint: str, payload: list) -> dict:
    token = get_credentials()
    conn = http.client.HTTPSConnection("api.dataforseo.com")
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
    }
    conn.request("POST", endpoint, json.dumps(payload), headers)
    response = conn.getresponse()
    return json.loads(response.read().decode())


def get_serp_results(keyword: str, top: int = 10) -> list:
    """Get top SERP results for a keyword (US, English)."""
    payload = [{
        "keyword": keyword,
        "location_code": LOCATION_CODE,
        "language_code": LANGUAGE_CODE,
        "device": "desktop",
        "os": "windows",
        "depth": max(top, 10),
    }]
    result = api_post("/v3/serp/google/organic/live/advanced", payload)
    items = []
    try:
        tasks = result["tasks"][0]["result"][0]["items"]
        for item in tasks:
            if item.get("type") == "organic":
                items.append({
                    "rank": item.get("rank_absolute"),
                    "url": item.get("url"),
                    "title": item.get("title"),
                    "description": item.get("description", "")[:120],
                    "domain": item.get("domain"),
                })
                if len(items) >= top:
                    break
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing SERP results: {e}")
    return items


def get_keyword_data(keyword: str) -> dict:
    """Get search volume, competition, and keyword difficulty."""
    payload = [{
        "keywords": [keyword],
        "location_code": LOCATION_CODE,
        "language_code": LANGUAGE_CODE,
    }]
    result = api_post("/v3/keywords_data/google_ads/search_volume/live", payload)
    try:
        item = result["tasks"][0]["result"][0]
        return {
            "keyword": item.get("keyword"),
            "search_volume": item.get("search_volume"),
            "competition": item.get("competition"),
            "competition_index": item.get("competition_index"),
            "cpc": item.get("cpc"),
            "monthly_searches": item.get("monthly_searches", []),
        }
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing keyword data: {e}")
        return {}


def get_serp_features(keyword: str) -> list:
    """Get SERP features showing for this keyword (featured snippet, PAA, etc.)."""
    payload = [{
        "keyword": keyword,
        "location_code": LOCATION_CODE,
        "language_code": LANGUAGE_CODE,
        "device": "desktop",
        "os": "windows",
        "depth": 10,
    }]
    result = api_post("/v3/serp/google/organic/live/advanced", payload)
    features = []
    try:
        items = result["tasks"][0]["result"][0]["items"]
        feature_types = set()
        for item in items:
            t = item.get("type", "")
            if t != "organic" and t not in feature_types:
                feature_types.add(t)
                features.append(t)
    except (KeyError, IndexError, TypeError):
        pass
    return features


def find_url_rank(serp_items: list, target_url: str) -> dict:
    """Check if a specific URL appears in the SERP results."""
    target_domain = urlparse(target_url).netloc.replace("www.", "")
    for item in serp_items:
        item_domain = (item.get("domain") or "").replace("www.", "")
        if target_domain in item_domain or item.get("url", "") == target_url:
            return item
    return {}


def fmt_volume(n) -> str:
    if n is None:
        return "N/A"
    if n >= 1000:
        return f"{n/1000:.1f}K"
    return str(n)


def main():
    parser = argparse.ArgumentParser(description="DataForSEO SERP research")
    parser.add_argument("--keyword", required=True, help="Keyword to research")
    parser.add_argument("--url", default=None, help="Check if this URL ranks")
    parser.add_argument("--top", type=int, default=10, help="Number of top results to show (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    print(f"\nResearching: \"{args.keyword}\" (US, English)")
    print("─" * 60)

    # Run keyword data and SERP in parallel-ish
    print("Fetching keyword data...")
    kw_data = get_keyword_data(args.keyword)

    print("Fetching SERP results...")
    serp_items = get_serp_results(args.keyword, top=args.top)

    print("Fetching SERP features...")
    features = get_serp_features(args.keyword)

    if args.json:
        output = {
            "keyword": args.keyword,
            "keyword_data": kw_data,
            "serp_features": features,
            "serp_results": serp_items,
        }
        if args.url:
            output["url_rank"] = find_url_rank(serp_items, args.url)
        print(json.dumps(output, indent=2))
        return

    # ── Keyword Overview ──────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  KEYWORD OVERVIEW")
    print(f"{'='*60}")
    if kw_data:
        print(f"  Keyword:          {kw_data.get('keyword', args.keyword)}")
        print(f"  Monthly Volume:   {fmt_volume(kw_data.get('search_volume'))}")
        print(f"  CPC:              ${kw_data.get('cpc', 'N/A')}")
        comp = kw_data.get('competition', '')
        comp_idx = kw_data.get('competition_index', '')
        print(f"  Competition:      {comp} ({comp_idx}/100)")
    else:
        print("  No keyword data returned.")

    # ── SERP Features ─────────────────────────────────────────────────────────
    print(f"\n── SERP FEATURES ────────────────────────────────────")
    if features:
        for f in features:
            label = f.replace("_", " ").title()
            print(f"  • {label}")
    else:
        print("  Standard blue links only (no special features)")

    # ── URL Rank Check ────────────────────────────────────────────────────────
    if args.url:
        print(f"\n── AVADA RANKING CHECK ──────────────────────────────")
        rank_item = find_url_rank(serp_items, args.url)
        if rank_item:
            print(f"  ✅ Found at position #{rank_item['rank']}")
            print(f"  URL:   {rank_item['url']}")
            print(f"  Title: {rank_item['title']}")
        else:
            print(f"  ❌ Not found in top {args.top} results")
            print(f"  URL checked: {args.url}")

    # ── Top SERP Results ──────────────────────────────────────────────────────
    print(f"\n── TOP {args.top} ORGANIC RESULTS ─────────────────────────")
    print(f"  {'#':>3}  {'Domain':<35}  Title")
    print(f"  {'─'*3}  {'─'*35}  {'─'*30}")
    for item in serp_items:
        domain = (item.get("domain") or "")[:35]
        title = (item.get("title") or "")[:50]
        print(f"  {item['rank']:>3}  {domain:<35}  {title}")

    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()
