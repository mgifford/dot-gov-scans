# SBOM (Software Bill of Materials)

This file tracks the primary software used by this repository, including version
pins and licensing signals to support legal and security review.

## Scope

- Direct Python dependencies from `requirements.txt`
- Direct Node.js dependencies from `package.json`
- Primary toolchain components used in local and CI workflows

## Python Dependencies (Direct)

| Component | Version | Purpose | License |
| --- | --- | --- | --- |
| setuptools | >=68.0,<81.0 | Packaging/runtime compatibility | MIT |
| fastapi | 0.115.6 | API framework | MIT |
| httpx | 0.28.1 | Async HTTP client | BSD-3-Clause |
| pydantic | 2.10.5 | Data models and validation | MIT |
| pydantic-settings | 2.7.1 | Settings management | MIT |
| apscheduler | 3.10.4 | Scheduled jobs | MIT |
| tldextract | 5.1.3 | Domain parsing | BSD-3-Clause |
| beautifulsoup4 | 4.12.3 | HTML parsing | MIT |
| tenacity | 9.0.0 | Retry logic | Apache-2.0 |
| webtech | 1.3.4 | Technology detection | GPL-3.0 |
| pytest | 9.0.3 | Test runner | MIT |
| pytest-asyncio | 1.3.0 | Async test support | Apache-2.0 |
| pytest-mock | 3.14.0 | Mocking utilities for tests | MIT |
| ruff | 0.9.10 | Linting | MIT |

## Node.js Dependencies (Direct)

| Component | Version | Purpose | License |
| --- | --- | --- | --- |
| @axe-core/playwright | ^4.10.2 | Accessibility test integration | MPL-2.0 |
| playwright | ^1.54.2 | Browser automation for accessibility checks | Apache-2.0 |

## Toolchain and Platform Components

| Component | Version Source | Purpose | Tracking Method |
| --- | --- | --- | --- |
| Python | `.github/workflows/*.yml` (setup-python) | Runtime for scanner and CLI | Pin and review in workflows |
| Node.js | `.github/workflows/*.yml` (setup-node) | Runtime for site accessibility checks | Pin and review in workflows |
| uv | AGENTS/README setup docs | Python dependency and environment manager | Pin installer/action version in CI when added |

## Update Workflow

1. Update dependency versions in `requirements.txt` and/or `package.json`.
2. Run tests and linters after every dependency change.
3. Update this SBOM with version and license changes in the same pull request.
4. Review dependency changes for vulnerability and license risk before merge.
