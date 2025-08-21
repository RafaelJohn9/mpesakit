"""Unit tests for MpesaError and MpesaApiException classes.

This module tests the error handling functionality of the Mpesa SDK using Pydantic for validation and serialization.
"""

from mpesa_sdk.errors import MpesaError, MpesaApiException


def test_mpesa_error_str_full_fields():
    """Test that MpesaError string representation includes all fields."""
    error = MpesaError(
        request_id="req-123",
        error_code="ERR001",
        error_message="Invalid request",
        status_code=400,
        raw_response={"foo": "bar"},
    )
    s = str(error)
    assert "Error Code: ERR001" in s
    assert "Message: Invalid request" in s
    assert "Request ID: req-123" in s


def test_mpesa_error_str_partial_fields():
    """Test that MpesaError string representation handles missing fields."""
    error = MpesaError(error_code="ERR002")
    s = str(error)
    assert "Error Code: ERR002" in s
    assert "Message:" not in s
    assert "Request ID:" not in s


def test_mpesa_error_str_no_fields():
    """Test that MpesaError string representation handles no fields."""
    error = MpesaError()
    s = str(error)
    assert s == "Unknown M-Pesa API error"


def test_mpesa_api_exception_message_and_properties():
    """Test that MpesaApiException initializes with MpesaError and exposes properties."""
    error = MpesaError(
        request_id="req-456", error_code="ERR003", error_message="Something went wrong"
    )
    exc = MpesaApiException(error)
    assert isinstance(exc, Exception)
    assert exc.error is error
    assert exc.error_code == "ERR003"
    assert exc.request_id == "req-456"
    assert str(exc) == str(error)


def test_mpesa_api_exception_with_minimal_error():
    """Test MpesaApiException with minimal MpesaError."""
    error = MpesaError()
    exc = MpesaApiException(error)
    assert exc.error_code is None
    assert exc.request_id is None
    assert str(exc) == "Unknown M-Pesa API error"


def test_mpesa_error_raw_response_field():
    """Test that MpesaError can store and retrieve raw response data."""
    raw = {"status": "failed", "reason": "timeout"}
    error = MpesaError(raw_response=raw)
    assert error.raw_response == raw


def test_mpesa_error_status_code_field():
    """Test that MpesaError can store and retrieve status code."""
    error = MpesaError(status_code=500)
    assert error.status_code == 500
