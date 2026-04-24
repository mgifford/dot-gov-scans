# AGENTS.md - Instructions for AI Coding Agents

This file follows the agents.md convention and provides guidance for AI coding
agents working in this repository.

## Project Overview

dot-gov-scans discovers and catalogues accessibility-statement URLs published by
United States government websites. It:

- Maintains TOON seed files per US state plus a federal seed
- Validates URLs asynchronously with rate-limiting and redirect tracking
- Tracks validation state in a lightweight SQLite/PostgreSQL-compatible metadata database
- Runs automated batch-validation cycles via GitHub Actions
- Generates markdown validation and scan reports

## Repository Layout

- `.github/workflows/` GitHub Actions CI/CD and cron workflows
- `data/imports/` raw CSV imports from Google Sheets
- `data/toon-seeds/` TOON seed files and index
- `docs/` user-facing documentation
- `src/` API, CLI, jobs, services, storage, and shared utilities
- `tests/` unit, integration, and contract tests

## Development Setup

```bash
pip install -r requirements.txt
python3 -m pytest tests/ -v
python3 -m src.cli.validate_urls --country TEXAS --rate-limit 2
python3 -m src.cli.validate_urls_batch --batch-mode --batch-size 2
python3 -m src.cli.generate_validation_report --output validation-report.md
```

## Conventions and Constraints

### Jurisdiction Codes and Filenames

- Primary grouping is US jurisdiction (state or federal)
- Filenames are lowercase-hyphenated (for example `new-york.toon`, `federal.toon`)
- Use conversion helpers in `src/lib/country_utils.py` until a dedicated jurisdiction utility is introduced

### URL Validation

- A URL is removed after 2 consecutive failures
- No retry within the same scan session
- Redirects are followed and final URLs are recorded
- `httpx` event hooks must be async

### Storage

- Validation metadata lives in `data/metadata.db` (not committed)
- Batch state is tracked in `validation_batch_state`
- Schema is defined in `src/storage/schema.py`

### Artifacts

- Seed files (`*.toon`) are version-controlled
- Validated output files (`*_validated.toon`) are git-ignored

## What AI Agents Should Do

- Follow existing style and patterns
- Keep changes focused and minimal
- Run tests for touched functionality
- Update docs when behavior changes
- Preserve URL failure policy and scan reliability

## What AI Agents Should Not Do

- Commit `data/metadata.db` or `*_validated.toon` files
- Push changes unless explicitly requested by a human
- Introduce breaking TOON format changes without updating parsers/tests
