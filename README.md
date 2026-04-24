# dot-gov-scans

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Deploy GitHub Pages](https://github.com/mgifford/dot-gov-scans/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/mgifford/dot-gov-scans/actions/workflows/deploy-pages.yml)
[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://mgifford.github.io/dot-gov-scans/)

Scans and seed datasets for finding accessibility statements on United States government websites.

## Overview

## Accessibility Standard: WCAG 2.1 AA (ADA Title II)

All government website scans in this project are evaluated against **WCAG 2.1 AA** — the
conformance level mandated by the US Department of Justice's final rule under
**Title II of the Americans with Disabilities Act (ADA)** for state and local government
websites and mobile apps.

**Why WCAG 2.1 AA, not WCAG 2.2 AA?**

- The DOJ rule explicitly cites WCAG 2.1 AA as the required standard.
- WCAG 2.2 adds useful criteria but is not yet legally required for US government sites.
- This project's own documentation and UI targets WCAG 2.2 AA as an internal quality bar,
	but government sites are measured only against what the law requires.

**Compliance timeline this project tracks:**

| Entity size | Original deadline | DOJ extended deadline |
|---|---|---|
| State/local governments (pop. > 50,000) | April 24, 2026 | Varies — see [DOJ update](https://www.deque.com/blog/ada-title-ii-update-the-key-takeaway-from-the-april-20-compliance-date-extension-from-the-doj/) |
| Smaller entities | April 26, 2027 | Varies |
| Federal agencies | Ongoing (Section 508 / WCAG 2.1 AA) | — |

Scans are designed to produce a **longitudinal record** — repeated snapshots per state and
federal scope — so progress toward WCAG 2.1 AA conformance can be tracked over time.

**Scan tool configuration:**

- **axe** (`scripts/run-axe-site-check.mjs`): runs tags `wcag2a`, `wcag2aa`, `wcag21a`,
	`wcag21aa` only. `wcag22a` / `wcag22aa` tags are explicitly excluded.
- **Google Lighthouse**: the `accessibility` category is used as an indicator score.
	Lighthouse does not expose a WCAG-version filter natively, but its audit set broadly
	covers WCAG 2.1 AA criteria. PWA audits are skipped for government sites.

## Overview

This repository uses a United States dataset model:

- One primary import CSV in `data/imports/google_sheets/`
- TOON seed files split by US state and federal scope in `data/toon-seeds/states/`
- A top-level TOON index at `data/toon-seeds/index.json`
- Automated scanning workflows and reports under `docs/`

## Data Model

Each TOON seed file is scoped to one jurisdiction:

- US states (for example `california.toon`, `texas.toon`)
- Federal (`federal.toon`)

Current TOON records include:

- `country`: `United States (USA)`
- `state`: State name or `Federal`
- `domains[]`: canonical government domains
- `pages[]`: source URLs with scan scores where available

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
python3 -m pytest tests/ -v

# Validate one jurisdiction (legacy CLI flag still uses --country)
python3 -m src.cli.validate_urls --country TEXAS --rate-limit 2

# Run a batch validation cycle
python3 -m src.cli.validate_urls_batch --batch-mode --batch-size 2

# Generate a validation report
python3 -m src.cli.generate_validation_report --output validation-report.md
```

## Regenerate State TOON Seeds

Use the splitter script to rebuild per-state and federal TOON files from the master CSV:

```bash
python3 scripts/split_usa_csv_to_toons.py
```

## Repository Structure

- `data/imports/` source CSV imports
- `data/toon-seeds/states/` state/federal TOON seeds
- `src/cli/` scan and report CLI entry points
- `src/services/` scanner and orchestration logic
- `src/storage/` metadata schema and DB helpers
- `docs/` public reports and methodology pages

## Notes

- `data/metadata.db` is local runtime state and should not be committed.
- Validated output TOON files are excluded from git.

## AI Disclosure

This repository allows AI-assisted development during implementation and maintenance.
When AI tools are used, contributors should keep this section updated with:

- Model/tool name
- Scope of use (code, tests, docs, refactoring)
- Whether AI is used only at build-time or also at runtime
