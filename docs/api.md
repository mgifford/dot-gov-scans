---
title: Data API
layout: page
---

Machine-readable scan datasets are published as static JSON (and CSV for
Lighthouse) under this site.

## Base URL

`https://mgifford.github.io/dot-gov-scans/`

## Endpoints

| Endpoint | Availability | Description |
|---|---|---|
| [`technology-index.json`](technology-index.json) | committed | Compact technology cross-reference index (`by_technology`, `by_category`). |
| [`technology-data.json`](technology-data.json) | committed + workflow artifact | Full technology dataset with drilldowns. |
| [`third-party-tools-data.json`](third-party-tools-data.json) | committed + workflow artifact | Third-party JS summary and drilldowns. |
| [`social-media-data.json`](social-media-data.json) | committed + workflow artifact | Social media summary and page evidence. |
| [`accessibility-data.json`](accessibility-data.json) | committed + workflow artifact | Accessibility statement summary and page evidence. |
| [`lighthouse-data.json`](lighthouse-data.json) | committed + workflow artifact | Lighthouse summary and per-URL results. |
| [`scan-progress-data.json`](scan-progress-data.json) | committed + workflow artifact | Cross-scan progress summaries and drilldowns. |
| [`scan-coverage-history.json`](scan-coverage-history.json) | committed | Historical coverage snapshots used by reports. |
| [`lighthouse-data.csv`](lighthouse-data.csv) | workflow artifact | Flat Lighthouse export for spreadsheets. |

## technology-index.json schema

```json
{
  "generated_at": "2026-05-21 22:00 UTC",
  "base_url": "https://mgifford.github.io/dot-gov-scans/",
  "note": "...",
  "by_technology": {
    "Drupal": {
      "pages": 123,
      "categories": ["CMS"],
      "by_country": {
        "FEDERAL": 100,
        "TEXAS": 23
      }
    }
  },
  "by_category": {
    "CMS": {
      "pages": 456,
      "technologies": ["Drupal", "WordPress"]
    }
  }
}
```

## Usage examples

Top jurisdictions for one technology:

```bash
curl -s https://mgifford.github.io/dot-gov-scans/technology-index.json | python3 -c "
import json,sys
data=json.load(sys.stdin)
wp=data['by_technology'].get('WordPress',{})
print('pages:', wp.get('pages', 0))
for cc,count in sorted(wp.get('by_country',{}).items(), key=lambda x: -x[1])[:10]:
    print(cc, count)
"
```

List technologies in a category:

```bash
curl -s https://mgifford.github.io/dot-gov-scans/technology-index.json | python3 -c "
import json,sys
data=json.load(sys.stdin)
print(data['by_category'].get('CMS',{}).get('technologies',[]))
"
```

## Artifact access

Each `Generate Scan Progress Report` workflow run uploads a
`scan-progress-report-*` artifact containing generated data files, including
JSON and CSV outputs referenced above.

