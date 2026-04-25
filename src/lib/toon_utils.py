"""Shared utilities for working with TOON seed data structures."""

from __future__ import annotations

from typing import List


def extract_urls_from_toon(toon_data: dict) -> List[str]:
    """Extract all page URLs from a TOON data structure.

    In addition to the explicit ``pages`` entries, any ``candidate_paths``
    listed on a domain entry are expanded into full URLs using the domain's
    ``canonical_domain``.  These extra probe URLs are appended after the
    regular page URLs for each domain so that scanners can discover
    accessibility statements and other resources that are not yet in the
    seed ``pages`` list.

    Duplicate URLs are silently skipped — if a candidate path resolves to a
    URL that is already present in ``pages``, it will not be added a second
    time.

    Args:
        toon_data: Parsed TOON JSON dict with a ``domains`` list.

    Returns:
        Ordered list of URL strings (pages first, then candidate paths per
        domain).
    """
    urls: List[str] = []
    for domain_entry in toon_data.get("domains", []):
        page_urls: set[str] = set()

        for page in domain_entry.get("pages", []):
            url = page.get("url")
            if url:
                urls.append(url)
                page_urls.add(url)

        # Expand candidate_paths into full URLs using the canonical domain.
        canonical = domain_entry.get("canonical_domain", "")
        candidate_paths = domain_entry.get("candidate_paths", [])
        if canonical and candidate_paths:
            for path in candidate_paths:
                # Ensure the path starts with a forward slash.
                if not path.startswith("/"):
                    path = "/" + path
                candidate_url = f"https://{canonical}{path}"
                if candidate_url not in page_urls:
                    urls.append(candidate_url)
                    page_urls.add(candidate_url)

    return urls
