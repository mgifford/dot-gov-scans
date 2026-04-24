# GitHub Copilot Instructions

Start with AGENTS.md at the repository root before making changes.

## Key References

- `AGENTS.md` - canonical repository guidance
- `ACCESSIBILITY.md` - accessibility commitments and standards
- `README.md` - project introduction and contributor workflow
- `docs/` - user-facing scan and report documentation

## Quick Start

```bash
pip install -r requirements.txt
python3 -m pytest tests/ -v
python3 -m src.cli.validate_urls --country TEXAS --rate-limit 2
python3 -m src.cli.validate_urls_batch --batch-mode --batch-size 2
python3 -m src.cli.generate_validation_report --output validation-report.md
```

## Critical Conventions

- TOON seeds are organized by US state and federal scope
- Validation removes URLs after 2 consecutive failures
- `httpx` event hooks must remain async
- Validation metadata is local in `data/metadata.db` and is not committed
- Seed TOON files are version-controlled; validated outputs are excluded by gitignore

## Do Not

- Commit `data/metadata.db` or `*_validated.toon`
- Bypass the two-failure URL-removal policy
- Hardcode jurisdiction conversions when helper utilities exist
- Push changes unless explicitly requested
