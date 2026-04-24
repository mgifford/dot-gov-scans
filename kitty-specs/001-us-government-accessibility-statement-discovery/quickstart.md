# Quickstart - US Government Accessibility Statement Discovery

## Prerequisites
- Python 3.12
- Network egress to public government domains
- Access to source domain lists (official and curated)

## 1) Prepare input sources
1. Build state/federal-scoped source list records with provenance URLs.
2. Ensure each record includes state or federal code and candidate hostnames.
3. Load or update the accessibility-term glossary used by this project.

## 2) Run a monthly jurisdiction scan
1. Trigger a scan for a specific state or federal scope and target month.
2. Wait for scan status to transition to `completed`.
3. Verify one jurisdiction TOON artifact was generated.

## 3) Validate output quality checks
- Every input hostname has a detection status (`found`, `not_found`, `uncertain`).
- Canonical hostname and redirect chain are populated when redirects occur.
- Confidence is one of `high`, `medium`, `low`.
- Up to 10 sampled URLs are present, with shortfall reason if fewer than 10.
- Provenance source URL is present on domain records.

## 4) Validate stale lifecycle
1. Simulate unreachable host with existing cached result.
2. Confirm host is retained and marked `stale=true` on first failed run.
3. Re-run next month (or forced second run) and confirm host is removed from active set if unreachable again.

## 5) Retrieve cached artifact
- Fetch latest jurisdiction artifact for operations dashboards.
- Fetch a specific monthly snapshot for audits and historical comparison.

## 6) Suggested implementation test passes
- Unit: detection scoring, glossary matching, canonicalization rules.
- Integration: end-to-end scan from source lists to TOON artifact.
- Contract: API request/response and schema conformance.
