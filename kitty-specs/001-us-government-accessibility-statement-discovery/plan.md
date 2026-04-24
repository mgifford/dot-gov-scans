# Implementation Plan: US Government Accessibility Statement Discovery
*Path: [templates/plan-template.md](templates/plan-template.md)*

**Branch**: `main` | **Date**: 2026-02-26 | **Spec**: [/workspaces/dot-gov-scans/kitty-specs/001-us-government-accessibility-statement-discovery/spec.md](/workspaces/dot-gov-scans/kitty-specs/001-us-government-accessibility-statement-discovery/spec.md)
**Input**: Feature specification from `/kitty-specs/001-us-government-accessibility-statement-discovery/spec.md`

## Summary

Build a scheduled server-side scanning service that runs monthly and produces state/federal-specific cached TOON outputs for government domains in scope of the US public-sector accessibility requirements. The service ingests authoritative country domain lists, normalizes hostnames with redirect tracing, detects accessibility statements across configured glossary languages using a glossary, assigns `high`/`medium`/`low` confidence, and preserves provenance and sampled navigation URLs for downstream accessibility analysis.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: FastAPI, HTTPX, Pydantic, APScheduler, tldextract, beautifulsoup4, tenacity  
**Storage**: File-based TOON cache artifacts per jurisdiction/month plus lightweight relational metadata store (SQLite local/dev, PostgreSQL-compatible schema for server deployment)  
**Testing**: pytest with unit, integration, and contract suites  
**Target Platform**: Linux server scheduled-job runtime  
**Project Type**: Single backend service  
**Performance Goals**: Complete one monthly jurisdiction run in <=30 minutes for up to 2,000 hostnames and generate 100% jurisdiction artifact availability for completed runs  
**Constraints**: Respect robots and polite crawl limits, at most one active run per jurisdiction, preserve prior stale results on first unreachable detection  
**Scale/Scope**: Initial scope is United States jurisdictions (states plus federal), monthly snapshots, one TOON artifact per jurisdiction per month

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- `.kittify/memory/constitution.md` is not present in this repository.
- Constitution gate is skipped for this plan run.
- Post-design constitution re-check: skipped (no constitution file present).

## Project Structure

### Documentation (this feature)

```
kitty-specs/001-us-government-accessibility-statement-discovery/
|- plan.md              # This file (/spec-kitty.plan output)
|- research.md          # Phase 0 output
|- data-model.md        # Phase 1 output
|- quickstart.md        # Phase 1 output
|- contracts/           # Phase 1 output
`- tasks.md             # Phase 2 output (/spec-kitty.tasks)
```

### Source Code (repository root)

```
src/
|- api/
|- jobs/
|- models/
|- services/
|- cli/
|- glossary/
`- storage/

tests/
|- contract/
|- integration/
`- unit/
```

**Structure Decision**: Use a single backend service layout in `src/` with modular boundaries for API, scheduler jobs, detection services, glossary handling, and artifact storage.

## Complexity Tracking

No constitution violations identified.

## Parallel Work Analysis

### Dependency Graph

```
Foundation (ingestion + canonical hostname model + glossary loading)
-> Wave 1 parallel (statement detection, scheduler stale lifecycle, TOON writer)
-> Wave 2 parallel (API read endpoints, contract tests, integration fixtures)
-> Integration (monthly orchestration + artifact validation)
```

### Work Distribution

- **Sequential work**: Data contracts and canonical hostname model must land first.
- **Parallel streams**: Detection logic, scheduler lifecycle, and API retrieval can proceed in parallel after model contracts stabilize.
- **Agent assignments**: Split by module boundary (`src/services/detection`, `src/jobs/scheduler`, `src/api`).

### Coordination Points

- **Sync schedule**: Merge after Foundation and after each wave.
- **Integration tests**: Validate end-to-end monthly run, stale retry-delete flow, and jurisdiction TOON output schema compliance.
