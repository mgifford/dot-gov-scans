# US Government Toon Seeds

This directory contains **TOON seed files** — one JSON file per US jurisdiction
(50 states + DC + 3 territories + 1 federal file) that list the government URLs
to be scanned.  They are the primary input for all scan and validation workflows.

## File format

Each `.toon` file is a JSON object with the following schema:

```json
{
  "version": "0.1-seed",
  "country": "United States (USA)",
  "state": "Texas",
  "domain_count": 283,
  "page_count": 562,
  "domains": [
    {
      "canonical_domain": "example.tx.gov",
      "subnational": "Texas",
      "pages": [
        {
          "url": "https://example.tx.gov/",
          "is_root_page": true,
          "performance_score": "0.95",
          "accessibility_score": "0.88",
          "best_practices_score": "1",
          "seo_score": "0.92"
        }
      ],
      "candidate_paths": [
        "/accessibility",
        "/ada-notice",
        "/accessibility-statement"
      ]
    }
  ]
}
```

| Field | Description |
|---|---|
| `version` | Schema version — currently `0.1-seed` for all seed files |
| `country` | Always `"United States (USA)"` |
| `state` | Jurisdiction display name (`"Federal"` for the federal seed) |
| `domain_count` | Number of distinct domains in this file |
| `page_count` | Total number of page URLs across all domains |
| `domains[].canonical_domain` | Bare hostname of the domain |
| `domains[].subnational` | State/territory name (mirrors `state`; `"Federal"` for federal) |
| `domains[].pages[].url` | Full page URL |
| `domains[].pages[].is_root_page` | `true` if this is the root/home page of the domain |
| `domains[].pages[].*_score` | Seeded Lighthouse scores from the Web Almanac 2025 crawl (absent if not yet collected) |
| `domains[].candidate_paths` | _(optional)_ List of additional URL paths to probe on this domain for deeper coverage (e.g. `["/accessibility", "/ada-notice"]`). Scanners expand these into full URLs using `https://{canonical_domain}{path}`. Paths that duplicate an existing `pages` entry are skipped automatically. |

## Index

`index.json` lists every seed file with its current `domain_count` and
`page_count`.  It is regenerated automatically when you run
`scripts/split_usa_csv_to_toons.py`.

## Candidate paths

The optional `candidate_paths` field on each domain entry tells scanners to
probe extra URL paths beyond those already listed in `pages`.  This is useful
for discovering accessibility statements and related resources that live at
predictable paths but were not captured during the original crawl.

**How it works:**  For each path in `candidate_paths`, the scanner constructs
`https://{canonical_domain}{path}` and adds it to the URL list for that scan
run.  Paths that duplicate an existing `pages` entry are skipped automatically
so no URL is scanned twice.

**Common patterns:**

```json
"candidate_paths": [
  "/accessibility",
  "/accessibility-statement",
  "/ada-notice",
  "/web-accessibility"
]
```

**When to add them:**
- For domains where accessibility statements are known to exist at non-root paths
- When you want broader coverage beyond what the Web Almanac crawl captured
- For high-priority domains where deeper investigation is warranted

**Adding candidate paths manually:**  Edit the `.toon` file directly (or the
source CSV for changes that should survive future regeneration) and add a
`candidate_paths` array to the relevant domain entry.  The field is optional —
omitting it has no effect on existing behaviour.

## Coverage

**55 seed files · 22,775 domains · 65,681 pages** (as of the 2025 Web Almanac import)

| Jurisdiction | File | Domains | Pages |
|---|---|---:|---:|
| Federal | `federal.toon` | 22,142 | 50,035 |
| Alabama | `alabama.toon` | 24 | 48 |
| Alaska | `alaska.toon` | 15 | 34 |
| American Samoa | `american-samoa.toon` | 3 | 7 |
| Arizona | `arizona.toon` | 141 | 337 |
| Arkansas | `arkansas.toon` | 12 | 29 |
| California | `california.toon` | 1,131 | 2,495 |
| Colorado | `colorado.toon` | 71 | 134 |
| Connecticut | `connecticut.toon` | 90 | 167 |
| DC | `dc.toon` | 211 | 486 |
| Delaware | `delaware.toon` | 7 | 17 |
| Florida | `florida.toon` | 78 | 140 |
| Georgia | `georgia.toon` | 119 | 217 |
| Hawaii | `hawaii.toon` | 3 | 8 |
| Idaho | `idaho.toon` | 44 | 103 |
| Illinois | `illinois.toon` | 41 | 91 |
| Indiana | `indiana.toon` | 272 | 598 |
| Iowa | `iowa.toon` | 12 | 21 |
| Kansas | `kansas.toon` | 89 | 194 |
| Kentucky | `kentucky.toon` | 313 | 738 |
| Louisiana | `louisiana.toon` | 136 | 266 |
| Maine | `maine.toon` | 1 | 1 |
| Maryland | `maryland.toon` | 52 | 89 |
| Massachusetts | `massachusetts.toon` | 77 | 153 |
| Michigan | `michigan.toon` | 71 | 122 |
| Minnesota | `minnesota.toon` | 397 | 785 |
| Mississippi | `mississippi.toon` | 218 | 486 |
| Missouri | `missouri.toon` | 154 | 336 |
| Montana | `montana.toon` | 127 | 264 |
| Nebraska | `nebraska.toon` | 99 | 205 |
| Nevada | `nevada.toon` | 159 | 358 |
| New Hampshire | `new-hampshire.toon` | 99 | 249 |
| New Jersey | `new-jersey.toon` | 129 | 203 |
| New Mexico | `new-mexico.toon` | 130 | 288 |
| New York | `new-york.toon` | 342 | 732 |
| North Carolina | `north-carolina.toon` | 140 | 292 |
| North Dakota | `north-dakota.toon` | 94 | 215 |
| Ohio | `ohio.toon` | 182 | 388 |
| Oklahoma | `oklahoma.toon` | 82 | 160 |
| Oregon | `oregon.toon` | 89 | 163 |
| Pennsylvania | `pennsylvania.toon` | 201 | 354 |
| Puerto Rico | `puerto-rico.toon` | 225 | 496 |
| Rhode Island | `rhode-island.toon` | 55 | 108 |
| South Carolina | `south-carolina.toon` | 198 | 481 |
| South Dakota | `south-dakota.toon` | 79 | 164 |
| Tennessee | `tennessee.toon` | 88 | 162 |
| Texas | `texas.toon` | 283 | 562 |
| US Virgin Islands | `us-virgin-islands.toon` | 26 | 64 |
| Utah | `utah.toon` | 3 | 9 |
| Vermont | `vermont.toon` | 9 | 15 |
| Virginia | `virginia.toon` | 40 | 79 |
| Washington | `washington.toon` | 326 | 713 |
| West Virginia | `west-virginia.toon` | 88 | 217 |
| Wisconsin | `wisconsin.toon` | 265 | 573 |
| Wyoming | `wyoming.toon` | 13 | 30 |

### Known coverage gaps

The following jurisdictions have notably low coverage in the underlying source
data and are candidates for enrichment in a future Web Almanac import or
manual addition:

| Jurisdiction | Domains | Pages | Notes |
|---|---:|---:|---|
| Maine | 1 | 1 | Only one small-town site (`lincolnville.me.us`); state agencies are missing |
| Hawaii | 3 | 8 | Major state — likely under-represented in the 2025 crawl |
| Utah | 3 | 9 | Major state — likely under-represented in the 2025 crawl |
| Vermont | 9 | 15 | Small state; plausible but worth verifying |
| Iowa | 12 | 21 | Medium state; low relative to comparable states |

The territories **Guam** and the **Northern Mariana Islands** are not yet
represented and have no corresponding seed files.

## Regenerating seed files from the CSV

The toon seed files are derived from the Web Almanac import CSV in
`data/imports/google_sheets/`.  To regenerate them after a new CSV is dropped
in:

```bash
python3 scripts/split_usa_csv_to_toons.py
```

This rewrites every `.toon` file and `index.json` in place.  Review the diff
before committing — the script is the authoritative source for seed structure.

## Adding or updating a single jurisdiction

1. Update (or add) the jurisdiction's rows in the source CSV.
2. Re-run `scripts/split_usa_csv_to_toons.py` to rebuild all seeds.
3. Commit the changed `.toon` files and updated `index.json`.

Do **not** edit `.toon` files by hand if the change should persist across future
CSV imports — make the change in the CSV instead so it survives regeneration.

## What NOT to commit

- `data/metadata.db` — runtime validation state, git-ignored
- `*_validated.toon` — output files produced by the validation workflow, git-ignored
