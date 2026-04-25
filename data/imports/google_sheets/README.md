# US Government Sites — Google Sheets Import

This directory holds the raw CSV export from the
[Web Almanac 2025](https://almanac.httparchive.org/) that is used as the seed
data source for all dot-gov scans.

## Files

| File | Description |
|---|---|
| `Web_Almanac_2025_United_States__USA__data - Web_Almanac_2025_United_States__USA__data.csv.csv` | Full US government crawl export — 65,680 page rows across 22,775 domains |

## CSV schema

| Column | Description |
|---|---|
| `country` | Always `United States (USA)` |
| `subnational` | State or territory name; empty for federal/national sites |
| `gov_domain` | Bare hostname of the domain (e.g. `example.tx.gov`) |
| `page` | Full page URL |
| `is_root_page` | `TRUE` / `FALSE` — whether this is the root page of the domain |
| `performance_score` | Lighthouse Performance score (0–1) |
| `accessibility_score` | Lighthouse Accessibility score (0–1) |
| `best_practices_score` | Lighthouse Best Practices score (0–1) |
| `seo_score` | Lighthouse SEO score (0–1) |

## Relationship to toon seed files

The CSV is the canonical source for the toon seeds in `data/toon-seeds/`.  The
script `scripts/split_usa_csv_to_toons.py` reads this CSV and writes one
`.toon` file per jurisdiction (state/territory + one `federal.toon` for rows
with an empty `subnational`).

To update the seeds after replacing this CSV with a newer export:

```bash
python3 scripts/split_usa_csv_to_toons.py
```

## Updating the source data

1. Export a fresh CSV from the shared Google Sheet (or the Web Almanac BigQuery
   dataset).
2. Replace the CSV file in this directory, keeping the same filename.
3. Run `scripts/split_usa_csv_to_toons.py` to rebuild the toon seeds.
4. Commit both the updated CSV and the regenerated `.toon` files together.
