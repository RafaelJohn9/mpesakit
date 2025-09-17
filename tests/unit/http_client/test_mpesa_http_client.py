"""Unit tests for the MpesaHttpClient HTTP client.

This module tests the MpesaHttpClient class for correct base URL selection,
HTTP POST and GET request handling, and error handling for various scenarios.
"""

import requests
import pytest
from unittest.mock import Mock, patch
from mpesakit.http_client.mpesa_http_client import MpesaHttpClient
from mpesakit.errors import MpesaApiException


@pytest.fixture
def client():
    """Fixture to provide a MpesaHttpClient instance in sandbox environment."""
    client = MpesaHttpClient(env="sandbox")
    return client


def test_base_url_sandbox():
    """Test that the base URL is correct for the sandbox environment."""
    client = MpesaHttpClient(env="sandbox")
    assert client.base_url == "https://sandbox.safaricom.co.ke"


def test_base_url_production():
    """Test that the base URL is correct for the production environment."""
    client = MpesaHttpClient(env="production")
    assert client.base_url == "https://api.safaricom.co.ke"


def test_post_success(client):
    """Test successful POST request returns expected JSON."""
    with patch("mpesakit.http_client.mpesa_http_client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {"foo": "bar"}
        mock_post.return_value = mock_response

        result = client.post("/test", json={"a": 1}, headers={"h": "v"})
        assert result == {"foo": "bar"}
        mock_post.assert_called_once()


def test_post_http_error(client):
    """Test POST request returns MpesaApiException on HTTP error."""
    with patch("mpesakit.http_client.mpesa_http_client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.json.return_value = {"errorMessage": "Bad Request"}
        mock_post.return_value = mock_response

        with pytest.raises(MpesaApiException) as exc:
            client.post("/fail", json={}, headers={})
        assert exc.value.error.error_code == "HTTP_400"
        assert "Bad Request" in exc.value.error.error_message


def test_post_json_decode_error(client):
    """Test POST request handles JSON decode error gracefully."""
    with patch("mpesakit.http_client.mpesa_http_client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 500
        mock_response.json.side_effect = ValueError()
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        with pytest.raises(MpesaApiException) as exc:
            client.post("/fail", json={}, headers={})
        assert exc.value.error.error_code == "HTTP_500"
        assert "Internal Server Error" in exc.value.error.error_message


def test_post_request_exception(client):
    """Test POST request raises MpesaApiException on generic exception."""
    with patch(
        "mpesakit.http_client.mpesa_http_client.requests.post",
        side_effect=requests.RequestException("boom"),
    ):
        with pytest.raises(MpesaApiException) as exc:
            client.post("/fail", json={}, headers={})
        assert exc.value.error.error_code == "REQUEST_FAILED"


def test_post_timeout(client):
    """Test POST request raises MpesaApiException on timeout."""
    with patch(
        "mpesakit.http_client.mpesa_http_client.requests.post",
        side_effect=requests.Timeout,
    ):
        with pytest.raises(MpesaApiException) as exc:
            client.post("/timeout", json={}, headers={})
        assert exc.value.error.error_code == "REQUEST_TIMEOUT"


def test_post_connection_error(client):
    """Test POST request raises MpesaApiException on connection error."""
    with patch(
        "mpesakit.http_client.mpesa_http_client.requests.post",
        side_effect=requests.ConnectionError,
    ):
        with pytest.raises(MpesaApiException) as exc:
            client.post("/conn", json={}, headers={})
        assert exc.value.error.error_code == "CONNECTION_ERROR"


def test_get_success(client):
    """Test successful GET request returns expected JSON."""
    with patch("mpesakit.http_client.mpesa_http_client.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"foo": "bar"}
        mock_get.return_value = mock_response

        result = client.get("/test", params={"a": 1}, headers={"h": "v"})
        assert result == {"foo": "bar"}
        mock_get.assert_called_once()


def test_get_http_error(client):
    """Test GET request returns MpesaApiException on HTTP error."""
    with patch("mpesakit.http_client.mpesa_http_client.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_response.json.return_value = {"errorMessage": "Not Found"}
        mock_get.return_value = mock_response

        with pytest.raises(MpesaApiException) as exc:
            client.get("/fail")
        assert exc.value.error.error_code == "HTTP_404"
        assert "Not Found" in exc.value.error.error_message


def test_get_json_decode_error(client):
    """Test GET request handles JSON decode error gracefully."""
    with patch("mpesakit.http_client.mpesa_http_client.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 500
        mock_response.json.side_effect = ValueError()
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        with pytest.raises(MpesaApiException) as exc:
            client.get("/fail")
        assert exc.value.error.error_code == "HTTP_500"
        assert "Internal Server Error" in exc.value.error.error_message


def test_get_request_exception(client):
    """Test GET request raises MpesaApiException on generic exception."""
    with patch(
        "mpesakit.http_client.mpesa_http_client.requests.get",
        side_effect=requests.RequestException("boom"),
    ):
        with pytest.raises(MpesaApiException) as exc:
            client.get("/fail")
        assert exc.value.error.error_code == "REQUEST_FAILED"


def test_get_timeout(client):
    """Test GET request raises MpesaApiException on timeout."""
    with patch(
        "mpesakit.http_client.mpesa_http_client.requests.get",
        side_effect=requests.Timeout,
    ):
        with pytest.raises(MpesaApiException) as exc:
            client.get("/timeout")
        assert exc.value.error.error_code == "REQUEST_TIMEOUT"


def test_get_connection_error(client):
    """Test GET request raises MpesaApiException on connection error."""
    with patch(
        "mpesakit.http_client.mpesa_http_client.requests.get",
        side_effect=requests.ConnectionError,
    ):
        with pytest.raises(MpesaApiException) as exc:
            client.get("/conn")
        assert exc.value.error.error_code == "CONNECTION_ERROR"





# Test async POST success scenario.
@pytest.mark.asyncio
async def test_async_post_success(client):
    # Patch aiohttp ClientSession.post to mock async POST request.
    with patch("mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.post") as mock_post:
        mock_response = Mock()
        mock_response.status = 200  # Simulate HTTP 200 OK.
        mock_response.json = Mock(return_value={"foo": "bar"})  # Mock JSON response.
        mock_post.return_value.__aenter__.return_value = mock_response

        # Call async_post and assert the result.
        result = await client.async_post("/test", json={"a": 1}, headers={"h": "v"})
        assert result == {"foo": "bar"}
        mock_post.assert_called_once()


# Test async POST HTTP error scenario.
@pytest.mark.asyncio
async def test_async_post_http_error(client):
    # Patch aiohttp ClientSession.post to simulate HTTP 400 error.
    with patch("mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.post") as mock_post:
        mock_response = Mock()
        mock_response.status = 400  # Simulate HTTP 400 error.
        mock_response.json = Mock(return_value={"errorMessage": "Bad Request"})
        mock_post.return_value.__aenter__.return_value = mock_response

        # Assert MpesaApiException is raised with correct error code and message.
        with pytest.raises(MpesaApiException) as exc:
            await client.async_post("/fail", json={}, headers={})
        assert exc.value.error.error_code == "HTTP_400"
        assert "Bad Request" in exc.value.error.error_message


# Test async POST JSON decode error scenario.
@pytest.mark.asyncio
async def test_async_post_json_decode_error(client):
    # Patch aiohttp ClientSession.post to simulate JSON decode error.
    with patch("mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.post") as mock_post:
        mock_response = Mock()
        mock_response.status = 500  # Simulate HTTP 500 error.
        mock_response.json = Mock(side_effect=ValueError())  # Simulate JSON decode error.
        mock_response.text = "Internal Server Error"
        mock_post.return_value.__aenter__.return_value = mock_response

        # Assert MpesaApiException is raised with correct error code and message.
        with pytest.raises(MpesaApiException) as exc:
            await client.async_post("/fail", json={}, headers={})
        assert exc.value.error.error_code == "HTTP_500"
        assert "Internal Server Error" in exc.value.error.error_message


# Test async POST generic exception scenario.
@pytest.mark.asyncio
async def test_async_post_exception(client):
    # Patch aiohttp ClientSession.post to raise a generic exception.
    with patch(
        "mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.post",
        side_effect=Exception("boom"),
    ):
        # Assert MpesaApiException is raised with REQUEST_FAILED code.
        with pytest.raises(MpesaApiException) as exc:
            await client.async_post("/fail", json={}, headers={})
        assert exc.value.error.error_code == "REQUEST_FAILED"


# Test async GET success scenario.
@pytest.mark.asyncio
async def test_async_get_success(client):
    # Patch aiohttp ClientSession.get to mock async GET request.
    with patch("mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.get") as mock_get:
        mock_response = Mock()
        mock_response.status = 200  # Simulate HTTP 200 OK.
        mock_response.json = Mock(return_value={"foo": "bar"})  # Mock JSON response.
        mock_get.return_value.__aenter__.return_value = mock_response

        # Call async_get and assert the result.
        result = await client.async_get("/test", params={"a": 1}, headers={"h": "v"})
        assert result == {"foo": "bar"}
        mock_get.assert_called_once()


# Test async GET HTTP error scenario.
@pytest.mark.asyncio
async def test_async_get_http_error(client):
    # Patch aiohttp ClientSession.get to simulate HTTP 404 error.
    with patch("mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.get") as mock_get:
        mock_response = Mock()
        mock_response.status = 404  # Simulate HTTP 404 error.
        mock_response.json = Mock(return_value={"errorMessage": "Not Found"})
        mock_get.return_value.__aenter__.return_value = mock_response

        # Assert MpesaApiException is raised with correct error code and message.
        with pytest.raises(MpesaApiException) as exc:
            await client.async_get("/fail")
        assert exc.value.error.error_code == "HTTP_404"
        assert "Not Found" in exc.value.error.error_message


# Test async GET JSON decode error scenario.
@pytest.mark.asyncio
async def test_async_get_json_decode_error(client):
    # Patch aiohttp ClientSession.get to simulate JSON decode error.
    with patch("mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.get") as mock_get:
        mock_response = Mock()
        mock_response.status = 500  # Simulate HTTP 500 error.
        mock_response.json = Mock(side_effect=ValueError())  # Simulate JSON decode error.
        mock_response.text = "Internal Server Error"
        mock_get.return_value.__aenter__.return_value = mock_response

        # Assert MpesaApiException is raised with correct error code and message.
        with pytest.raises(MpesaApiException) as exc:
            await client.async_get("/fail")
        assert exc.value.error.error_code == "HTTP_500"
        assert "Internal Server Error" in exc.value.error.error_message


# Test async GET generic exception scenario.
@pytest.mark.asyncio
async def test_async_get_exception(client):
    # Patch aiohttp ClientSession.get to raise a generic exception.
    with patch(
        "mpesakit.http_client.mpesa_http_client.aiohttp.ClientSession.get",
        side_effect=Exception("boom"),
    ):
        # Assert MpesaApiException is raised with REQUEST_FAILED code.
        with pytest.raises(MpesaApiException) as exc:
            await client.async_get("/fail")
        assert exc.value.error.error_code == "REQUEST_FAILED"