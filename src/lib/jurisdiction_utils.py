"""Utility functions for jurisdiction (US state and federal) handling."""

from __future__ import annotations


# Special-case display names for jurisdictions whose names cannot be derived
# mechanically from their code (e.g. title-casing would produce "Dc" or
# "Us Virgin Islands").
_JURISDICTION_DISPLAY_NAMES: dict[str, str] = {
    "DC": "DC",
    "US_VIRGIN_ISLANDS": "US Virgin Islands",
}


def jurisdiction_filename_to_code(filename: str) -> str:
    """
    Convert a jurisdiction filename to a jurisdiction code.

    Transforms lowercase hyphenated filenames to uppercase underscored codes.
    Example: "new-york" -> "NEW_YORK"

    Args:
        filename: Lowercase hyphenated jurisdiction name (without .toon extension)

    Returns:
        Uppercase underscored jurisdiction code
    """
    return filename.upper().replace("-", "_")


def jurisdiction_code_to_filename(jurisdiction_code: str) -> str:
    """
    Convert a jurisdiction code to a filename-safe format.

    Transforms uppercase underscored codes to lowercase hyphenated names.
    Example: "NEW_YORK" -> "new-york"

    Args:
        jurisdiction_code: Uppercase underscored jurisdiction code

    Returns:
        Lowercase hyphenated filename (without extension)
    """
    return jurisdiction_code.lower().replace("_", "-")


def jurisdiction_code_to_display_name(jurisdiction_code: str) -> str:
    """Return a human-friendly display label for a jurisdiction code."""
    if jurisdiction_code in _JURISDICTION_DISPLAY_NAMES:
        return _JURISDICTION_DISPLAY_NAMES[jurisdiction_code]
    return jurisdiction_code.replace("_", " ").title()
