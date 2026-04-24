"""Unit tests for jurisdiction utility functions."""

from src.lib.jurisdiction_utils import (
    jurisdiction_code_to_display_name,
    jurisdiction_code_to_filename,
    jurisdiction_filename_to_code,
)


def test_jurisdiction_filename_to_code():
    """Test converting filename to jurisdiction code."""
    assert jurisdiction_filename_to_code("texas") == "TEXAS"
    assert jurisdiction_filename_to_code("new-york") == "NEW_YORK"
    assert jurisdiction_filename_to_code("new-mexico") == "NEW_MEXICO"


def test_jurisdiction_code_to_filename():
    """Test converting jurisdiction code to filename."""
    assert jurisdiction_code_to_filename("TEXAS") == "texas"
    assert jurisdiction_code_to_filename("NEW_YORK") == "new-york"
    assert jurisdiction_code_to_filename("NEW_MEXICO") == "new-mexico"


def test_roundtrip_conversion():
    """Test that conversions are reversible."""
    filenames = ["texas", "new-york", "federal", "us-virgin-islands"]

    for filename in filenames:
        code = jurisdiction_filename_to_code(filename)
        result = jurisdiction_code_to_filename(code)
        assert result == filename


def test_roundtrip_conversion_from_code():
    """Test that conversions are reversible from code."""
    codes = ["TEXAS", "NEW_YORK", "FEDERAL", "US_VIRGIN_ISLANDS"]

    for code in codes:
        filename = jurisdiction_code_to_filename(code)
        result = jurisdiction_filename_to_code(filename)
        assert result == code


def test_jurisdiction_code_to_display_name():
    """Test converting jurisdiction codes to human-friendly display names."""
    assert jurisdiction_code_to_display_name("TEXAS") == "Texas"
    assert jurisdiction_code_to_display_name("NEW_YORK") == "New York"
    assert jurisdiction_code_to_display_name("FEDERAL") == "Federal"
    assert jurisdiction_code_to_display_name("DC") == "DC"
    assert jurisdiction_code_to_display_name("US_VIRGIN_ISLANDS") == "US Virgin Islands"
