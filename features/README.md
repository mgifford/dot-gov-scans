# Behavior Specs

Gherkin feature files are organized by stable behavior pillar:

- `features/seed-management/`
- `features/url-validation/`
- `features/reporting/`
- `features/workflow-reliability/`

Each scenario should map back to a feature ID in `/FEATURES.md`.

## Conventions

- Prefer user-outcome wording.
- Keep scenarios deterministic.
- Tag for CI scope (`@smoke`, `@regression`, `@workflow`, `@site`).
- Keep one source of truth for behavior intent in `/FEATURES.md`.
