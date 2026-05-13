# Definition of Done (Report)

Use this checklist to decide whether a report cycle is complete and ready to share.

## 1) Scope and Inputs

- [ ] The report scope is explicit (selected seed/jurisdiction or all seeds).
- [ ] Input data came from the current repository workflow/CLI outputs.
- [ ] No local-only runtime artifacts were committed (`data/metadata.db`, `*_validated.toon`).

## 2) Validation and Data Quality

- [ ] URL validation completed without blocking failures.
- [ ] The two-failure removal policy was preserved (no bypasses).
- [ ] Redirect handling was preserved and final URLs were recorded.
- [ ] Report totals are internally consistent (totals, valid/invalid/redirected/removed).

## 3) Report Content Quality

- [ ] The report includes summary statistics per seed/jurisdiction.
- [ ] The report includes actionable failure/error details.
- [ ] Terminology is consistent with project conventions:
  - Use “seed” in user-facing report text where appropriate.
  - Keep legacy `--country` wording only when referring to CLI flags.
- [ ] The report states assumptions, limitations, and any partial-run caveats.

## 4) Reproducibility and Verification

- [ ] Commands/workflows used to generate the report are documented or traceable.
- [ ] Results are reproducible from repository state and committed inputs.
- [ ] Any changed documentation reflects current behavior.

## 5) Publication Readiness

- [ ] Markdown renders correctly and is readable on GitHub.
- [ ] Links referenced in the report resolve.
- [ ] Artifacts needed by maintainers/reviewers are available (workflow artifacts or docs references).

## 6) Review and Handoff

- [ ] Changes are reviewed for accuracy and clarity.
- [ ] Open risks/follow-ups are listed explicitly.
- [ ] The report is ready for maintainers to act on without extra context.

---

A report is **Done** when every checklist item above is complete or any exceptions are explicitly documented.
