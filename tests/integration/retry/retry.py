# tests/test_retry.py
import pytest
from mpesakit.retry.retry import retryable_request
import random

# A dummy function to simulate failure
@retryable_request(stop_attempts=5, wait_min=0, wait_max=0, exception_type=ValueError)
def sometimes_fails():
    """Fails randomly to test retry logic."""
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

def test_retryable_request():
    result = sometimes_fails()
    assert result == "Success"
