"""Split the Web Almanac USA CSV into per-state (and federal) TOON seed files.

Usage:
    python3 scripts/split_usa_csv_to_toons.py

Output:
    data/toon-seeds/<state-slug>.toon  — one file per state + federal.toon
    data/toon-seeds/index.json                — updated index listing all states
"""

from __future__ import annotations

import csv
import json
import pathlib
import re
import sys
from collections import defaultdict
from typing import Any

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = (
    REPO_ROOT
    / "data/imports/google_sheets"
    / "Web_Almanac_2025_United_States__USA__data - Web_Almanac_2025_United_States__USA__data.csv.csv"
)
OUTPUT_DIR = REPO_ROOT / "data/toon-seeds"
INDEX_PATH = REPO_ROOT / "data/toon-seeds/index.json"

TOON_VERSION = "0.1-seed"
COUNTRY = "United States (USA)"


def slugify(name: str) -> str:
    """Convert a state name to a lowercase-hyphenated filename slug.

    Examples:
        'New York'        -> 'new-york'
        'DC'              -> 'dc'
        'US Virgin Islands' -> 'us-virgin-islands'
        ''                -> 'federal'
    """
    if not name:
        return "federal"
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def build_toons(csv_path: pathlib.Path) -> dict[str, dict[str, Any]]:
    """Read the CSV and group rows into per-state TOON structures.

    Returns a mapping of state slug -> TOON dict (without counts, filled later).
    """
    # state_slug -> domain -> list[page dicts]
    state_domains: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    state_display: dict[str, str] = {}  # slug -> display name

    with csv_path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            state_name = row["subnational"].strip()
            slug = slugify(state_name)
            display = state_name if state_name else "Federal"
            state_display[slug] = display

            domain = row["gov_domain"].strip()
            page: dict[str, Any] = {"url": row["page"].strip()}

            is_root_raw = row.get("is_root_page", "").strip().upper()
            page["is_root_page"] = is_root_raw == "TRUE"

            for score_field in (
                "performance_score",
                "accessibility_score",
                "best_practices_score",
                "seo_score",
            ):
                val = row.get(score_field, "").strip()
                if val:
                    page[score_field] = val

            state_domains[slug][domain].append(page)

    toons: dict[str, dict[str, Any]] = {}
    for slug, domains in state_domains.items():
        domain_list = []
        for canonical_domain, pages in sorted(domains.items()):
            domain_list.append(
                {
                    "canonical_domain": canonical_domain,
                    "subnational": state_display[slug],
                    "pages": pages,
                }
            )

        toons[slug] = {
            "version": TOON_VERSION,
            "country": COUNTRY,
            "state": state_display[slug],
            "domain_count": len(domain_list),
            "page_count": sum(len(d["pages"]) for d in domain_list),
            "domains": domain_list,
        }

    return toons


def write_toons(toons: dict[str, dict[str, Any]], output_dir: pathlib.Path) -> None:
    """Write each TOON dict to <output_dir>/<slug>.toon."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for slug, toon in sorted(toons.items()):
        out_path = output_dir / f"{slug}.toon"
        with out_path.open("w", encoding="utf-8") as fh:
            json.dump(toon, fh, indent=2, ensure_ascii=False)
        print(f"  wrote {out_path.relative_to(REPO_ROOT)}  "
              f"({toon['domain_count']} domains, {toon['page_count']} pages)")


def write_index(toons: dict[str, dict[str, Any]], index_path: pathlib.Path) -> None:
    """Write/overwrite data/toon-seeds/index.json with the new state listing."""
    entries = []
    for slug in sorted(toons):
        toon = toons[slug]
        entries.append(
            {
                "state": toon["state"],
                "file": f"data/toon-seeds/{slug}.toon",
                "domain_count": toon["domain_count"],
                "page_count": toon["page_count"],
            }
        )
    index = {"states": entries}
    with index_path.open("w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=2, ensure_ascii=False)
    print(f"\nWrote index: {index_path.relative_to(REPO_ROOT)}  ({len(entries)} entries)")


def main() -> int:
    """Entry point."""
    if not CSV_PATH.exists():
        print(f"ERROR: CSV not found at {CSV_PATH}", file=sys.stderr)
        return 1

    print(f"Reading {CSV_PATH.name} …")
    toons = build_toons(CSV_PATH)
    print(f"Found {len(toons)} states/groups\n")

    write_toons(toons, OUTPUT_DIR)
    write_index(toons, INDEX_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
