# FEATURES

This file is the behavior index for dot-gov-scans.

It defines the stable, human-readable product behaviors we commit to over time.
Executable BDD specs live under `features/` and are organized by behavior pillar.

## Behavior Pillars

1. **Seed management**
   - Keep jurisdiction seed handling predictable and traceable.
2. **URL validation lifecycle**
   - Apply consistent validation, redirects, and removal policy.
3. **Reporting**
   - Generate reproducible, understandable reports from scan outputs.
4. **Workflow reliability**
   - Keep scheduled and manual workflows deterministic and safe.

## Feature Inventory (Source of Truth)

| Feature ID | Pillar | User outcome | Gherkin spec | Current implementation/tests |
|---|---|---|---|---|
| FTR-SEED-001 | Seed management | Operator can target a single jurisdiction seed consistently | `features/seed-management/seed-selection.feature` | `src/lib/jurisdiction_utils.py`, `tests/unit/test_jurisdiction_utils.py` |
| FTR-SEED-002 | Seed management | Operator can split import data into per-jurisdiction TOON seeds | `features/seed-management/seed-selection.feature` | `scripts/split_usa_csv_to_toons.py`, `tests/unit/test_source_ingest.py` |
| FTR-VAL-001 | URL validation lifecycle | Validator records redirects and final URLs deterministically | `features/url-validation/url-validation-lifecycle.feature` | `src/services/url_validator.py`, `tests/unit/test_url_validator.py` |
| FTR-VAL-002 | URL validation lifecycle | URL is removed after two consecutive failures | `features/url-validation/url-validation-lifecycle.feature` | `src/services/url_validator.py`, `tests/integration/test_url_validation_scanner.py` |
| FTR-REP-001 | Reporting | Operator can generate markdown validation report from metadata | `features/reporting/report-generation.feature` | `src/cli/generate_validation_report.py`, `tests/unit/test_generate_validation_report.py` |
| FTR-REP-002 | Reporting | Operator can generate scan progress outputs consistently | `features/reporting/report-generation.feature` | `src/cli/generate_scan_progress.py`, `tests/unit/test_generate_scan_progress.py` |
| FTR-WF-001 | Workflow reliability | Batch validation workflows can be resumed/cancelled safely | `features/workflow-reliability/workflow-safety.feature` | `.github/workflows/validate-urls-batch.yml`, `tests/unit/test_monitor_workflows_workflow.py` |
| FTR-WF-002 | Workflow reliability | Generated site accessibility checks run as predictable CI gate | `features/workflow-reliability/workflow-safety.feature` | `scripts/run-axe-site-check.mjs`, `.github/workflows/axe-site-accessibility.yml`, `package.json` |

## Test-Layer Split

- **Business/process behavior (fast):** keep using Python tests (`pytest`) for service and workflow logic.
- **Generated site/UI behavior:** use Playwright-based scenarios.
- **BDD expression:** keep behavior definitions in Gherkin (`.feature`) files and map them to test code.

For direct alignment with Playwright in E2E behavior, use **Cucumber.js + Playwright** for `@site` scenarios once introduced; this repository currently keeps executable coverage in `pytest` and Playwright-based axe checks.

## Tags and Scope

Use these tags to keep CI predictable:

- `@smoke` — smallest critical path
- `@regression` — full behavior coverage
- `@workflow` — GitHub Actions orchestration behavior
- `@site` — generated site behavior

## Governance Rules

1. Every behavior change PR updates all three when applicable:
   - User story in `FEATURES.md`
   - Matching `.feature` scenario(s)
   - Matching automated test implementation
2. Feature IDs are stable and must be referenced in related test code, PR descriptions, or test names.
3. New behavior is added to an existing pillar unless a truly new stable pillar is required.
4. Implementation details must stay out of user-facing scenario text.

## Lightweight Review Checklist

- [ ] Scenario wording is clear and user-outcome focused.
- [ ] Data assumptions are deterministic.
- [ ] Steps do not leak implementation details.
- [ ] Feature ID traceability is maintained from `FEATURES.md` to `.feature` to test code.
- [ ] Tagging reflects expected CI scope (`@smoke`, `@regression`, `@workflow`, `@site`).

## Adoption Path

Start with the high-value stories in `features/` (this commit), then expand only where behavior drift risk is highest.
