"""Unit tests for is_mpesa_ip_allowed in mpesa_sdk.utils.ip_whitelist."""

import pytest
from mpesa_sdk.utils.ip_whitelist import is_mpesa_ip_allowed


@pytest.mark.parametrize(
    "ip,expected",
    [
        # Valid M-Pesa IPs
        ("196.201.214.200", True),
        ("196.201.214.206", True),
        ("196.201.213.114", True),
        ("196.201.214.207", True),
        ("196.201.214.208", True),
        ("196.201.213.44", True),
        ("196.201.212.127", True),
        ("196.201.212.128", True),
        ("196.201.212.129", True),
        ("196.201.212.132", True),
        ("196.201.212.136", True),
        ("196.201.212.138", True),
        ("196.201.212.69", True),
        ("196.201.212.74", True),
        # Not in M-Pesa IPs
        ("192.168.1.1", False),
        ("8.8.8.8", False),
        ("127.0.0.1", False),
        ("255.255.255.255", False),
        # Invalid IPs
        ("not.an.ip", False),
        ("", False),
        (None, False),
        ("196.201.214.999", False),  # Out of range
    ],
)
def test_is_mpesa_ip_allowed_default(ip, expected):
    """Test is_mpesa_ip_allowed with default M-Pesa IPs."""
    assert is_mpesa_ip_allowed(ip) == expected


@pytest.mark.parametrize(
    "ip,allowed_ips,expected",
    [
        # Custom allowed IPs
        ("10.0.0.1", ["10.0.0.1", "10.0.0.2"], True),
        ("10.0.0.2", ["10.0.0.1", "10.0.0.2"], True),
        ("10.0.0.3", ["10.0.0.1", "10.0.0.2"], False),
        # Custom allowed IPs with M-Pesa IPs
        ("196.201.214.200", ["196.201.214.200"], True),
        ("196.201.214.200", ["196.201.214.201"], False),
        # Empty allowed_ips
        ("196.201.214.200", [], False),
        # Invalid IP in allowed_ips
        ("196.201.214.200", ["not.an.ip"], False),
        # allowed_ips is None (should use default)
        ("196.201.214.200", None, True),
    ],
)
def test_is_mpesa_ip_allowed_custom(ip, allowed_ips, expected):
    """Test is_mpesa_ip_allowed with custom allowed_ips."""
    assert is_mpesa_ip_allowed(ip, allowed_ips) == expected
