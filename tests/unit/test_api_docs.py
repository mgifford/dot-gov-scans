"""Tests for Data API documentation wiring."""

from pathlib import Path


def test_api_doc_exists_and_lists_technology_index() -> None:
    """Data API doc should exist and include the technology index endpoint."""
    api_doc = Path("docs/api.md")
    content = api_doc.read_text(encoding="utf-8")
    assert "title: Data API" in content
    assert "technology-index.json" in content
    assert "scan-progress-data.json" in content


def test_docs_navigation_includes_api_page() -> None:
    """Site navigation and docs index should link to api.md."""
    config_content = Path("docs/_config.yml").read_text(encoding="utf-8")
    index_content = Path("docs/index.md").read_text(encoding="utf-8")
    assert "- api.md" in config_content
    assert "`api.md`" in index_content
