"""Unit tests for src.lib.toon_utils."""

from __future__ import annotations

import pytest

from src.lib.toon_utils import extract_urls_from_toon


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _toon(domains: list[dict]) -> dict:
    return {"version": "0.1-seed", "country": "United States (USA)", "domains": domains}


def _domain(canonical: str, pages: list[str], candidate_paths: list[str] | None = None) -> dict:
    entry: dict = {
        "canonical_domain": canonical,
        "pages": [{"url": u} for u in pages],
    }
    if candidate_paths is not None:
        entry["candidate_paths"] = candidate_paths
    return entry


# ---------------------------------------------------------------------------
# Basic page extraction
# ---------------------------------------------------------------------------


def test_extracts_pages_without_candidate_paths():
    toon = _toon([_domain("example.gov", ["https://example.gov/", "https://example.gov/about"])])
    assert extract_urls_from_toon(toon) == [
        "https://example.gov/",
        "https://example.gov/about",
    ]


def test_returns_empty_list_for_no_domains():
    assert extract_urls_from_toon({"domains": []}) == []


def test_returns_empty_list_for_missing_domains_key():
    assert extract_urls_from_toon({}) == []


def test_skips_pages_without_url():
    toon = _toon(
        [
            {
                "canonical_domain": "example.gov",
                "pages": [{"url": "https://example.gov/"}, {"not_a_url": "ignored"}],
            }
        ]
    )
    assert extract_urls_from_toon(toon) == ["https://example.gov/"]


# ---------------------------------------------------------------------------
# candidate_paths expansion
# ---------------------------------------------------------------------------


def test_candidate_paths_are_appended_after_pages():
    toon = _toon(
        [
            _domain(
                "example.gov",
                ["https://example.gov/"],
                candidate_paths=["/accessibility", "/ada-notice"],
            )
        ]
    )
    urls = extract_urls_from_toon(toon)
    assert urls == [
        "https://example.gov/",
        "https://example.gov/accessibility",
        "https://example.gov/ada-notice",
    ]


def test_candidate_paths_without_leading_slash():
    toon = _toon(
        [_domain("example.gov", ["https://example.gov/"], candidate_paths=["accessibility"])]
    )
    urls = extract_urls_from_toon(toon)
    assert "https://example.gov/accessibility" in urls


def test_candidate_paths_duplicate_of_existing_page_skipped():
    """A candidate_path that duplicates an existing page URL must not be added twice."""
    toon = _toon(
        [
            _domain(
                "example.gov",
                ["https://example.gov/", "https://example.gov/accessibility"],
                candidate_paths=["/accessibility", "/ada-notice"],
            )
        ]
    )
    urls = extract_urls_from_toon(toon)
    assert urls.count("https://example.gov/accessibility") == 1
    assert "https://example.gov/ada-notice" in urls


def test_candidate_paths_duplicate_within_candidate_paths_skipped():
    """Duplicate entries within candidate_paths should only produce one URL."""
    toon = _toon(
        [
            _domain(
                "example.gov",
                ["https://example.gov/"],
                candidate_paths=["/accessibility", "/accessibility"],
            )
        ]
    )
    urls = extract_urls_from_toon(toon)
    assert urls.count("https://example.gov/accessibility") == 1


def test_candidate_paths_ignored_when_no_canonical_domain():
    """Domains without a canonical_domain cannot generate candidate path URLs."""
    toon = _toon(
        [
            {
                "pages": [{"url": "https://example.gov/"}],
                "candidate_paths": ["/accessibility"],
            }
        ]
    )
    urls = extract_urls_from_toon(toon)
    # Only the explicit page URL should appear; no candidate URL can be built.
    assert urls == ["https://example.gov/"]


def test_candidate_paths_empty_list_adds_no_urls():
    toon = _toon([_domain("example.gov", ["https://example.gov/"], candidate_paths=[])])
    assert extract_urls_from_toon(toon) == ["https://example.gov/"]


def test_multiple_domains_each_expanded_independently():
    toon = _toon(
        [
            _domain("alpha.gov", ["https://alpha.gov/"], candidate_paths=["/accessibility"]),
            _domain("beta.gov", ["https://beta.gov/"], candidate_paths=["/ada"]),
        ]
    )
    urls = extract_urls_from_toon(toon)
    assert urls == [
        "https://alpha.gov/",
        "https://alpha.gov/accessibility",
        "https://beta.gov/",
        "https://beta.gov/ada",
    ]


def test_domain_without_candidate_paths_key_unchanged():
    """Domains that have no candidate_paths key at all are unaffected."""
    toon = _toon([_domain("example.gov", ["https://example.gov/"])])
    assert extract_urls_from_toon(toon) == ["https://example.gov/"]
