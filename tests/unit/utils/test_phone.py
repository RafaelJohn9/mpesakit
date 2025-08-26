"""Unit tests for the normalize_phone_number function in mpesakit.utils.phone."""

import pytest
from mpesakit.utils.phone import normalize_phone_number


@pytest.mark.parametrize(
    "input_phone,expected",
    [
        # Valid formats
        ("0712345678", "254712345678"),
        ("+254712345678", "254712345678"),
        ("254712345678", "254712345678"),
        # With whitespace (should be valid if spaces are present)
        (" 0712345678 ", "254712345678"),
        ("\t+254712345678\n", "254712345678"),
        (" 254712345678", "254712345678"),
        # Valid numbers with spaces inside
        ("+254 712345678", "254712345678"),
        ("0 712345678", "254712345678"),
        ("07 12345678", "254712345678"),
        ("254 712345678", "254712345678"),
        ("+2547 12345678", "254712345678"),
        ("0 712 345678", "254712345678"),
        # Invalid formats
        ("712345678", None),  # Missing leading 0 or 254
        ("+25471234567", None),  # Too short
        ("+2547123456789", None),  # Too long
        ("071234567", None),  # Too short
        ("07123456789", None),  # Too long
        ("25471234567", None),  # Too short
        ("2547123456789", None),  # Too long
        ("1234567890", None),  # Invalid prefix
        ("", None),  # Empty string
        (None, None),  # None input
        (1234567890, None),  # Non-string input
        ([], None),  # Non-string input
        # Invalid if contains non-digit (except + at start)
        ("+2547a2345678", None),  # Contains letter
    ],
)
def test_normalize_phone_number(input_phone, expected):
    """Test the normalize_phone_number function with various inputs."""
    assert normalize_phone_number(input_phone) == expected
