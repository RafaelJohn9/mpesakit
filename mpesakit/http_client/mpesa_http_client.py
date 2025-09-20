"""MpesaHttpClient: A client for making HTTP requests to the M-Pesa API.

Handles GET and POST requests with error handling for common HTTP issues.
"""

from typing import Dict, Any, Optional
import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    retry_if_exception_type,
    RetryCallState
)
import logging
from mpesakit.errors import MpesaError, MpesaApiException
from .http_client import HttpClient


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_request_error(response: requests.Response):
    """Handles non-successful HTTP responses.

    This function is now responsible for converting HTTP status codes
    and JSON parsing errors into MpesaApiException.
    """
    try:
        response_data = response.json()
    except ValueError:
        response_data = {"errorMessage": response.text.strip() or ""}

    if not response.ok:
        error_message = response_data.get("errorMessage", "")
        raise MpesaApiException(
            MpesaError(
                error_code=f"HTTP_{response.status_code}",
                error_message=error_message,
                status_code=response.status_code,
                raw_response=response_data,
            )
        )

def handle_retry_exception(retry_state: RetryCallState):
    """Custom hook to handle exceptions after all retries fail.

    It raises a custom MpesaApiException with the appropriate error code.
    """
    
    if retry_state.outcome:
        exception = retry_state.outcome.exception()
        
        if isinstance(exception, requests.exceptions.Timeout):
            raise MpesaApiException(
                MpesaError(error_code="REQUEST_TIMEOUT", error_message=str(exception))
            ) from exception
        elif isinstance(exception, requests.exceptions.ConnectionError):
            raise MpesaApiException(
                MpesaError(error_code="CONNECTION_ERROR", error_message=str(exception))
            ) from exception
        
        raise MpesaApiException(
            MpesaError(error_code="REQUEST_FAILED", error_message=str(exception))
        ) from exception
    
    
    raise MpesaApiException(
        MpesaError(error_code="REQUEST_FAILED", error_message="An unknown retry error occurred.")
    )


class MpesaHttpClient(HttpClient):
    """A client for making HTTP requests to the M-Pesa API."""

    base_url: str
    _session: Optional[requests.Session] = None

    def __init__(self, env: str = "sandbox", use_session: bool = False):
        """Initializes the MpesaHttpClient instance.

        Args:
            env (str): The environment to connect to ('sandbox' or 'production').
            use_session (bool): Whether to use a persistent session.
        """
        self.base_url = self._resolve_base_url(env)
        if use_session:
            self._session = requests.Session()
            self._session.trust_env = False

    def _resolve_base_url(self, env: str) -> str:
        if env.lower() == "production":
            return "https://api.safaricom.co.ke"
        return "https://sandbox.safaricom.co.ke"

    @retry(
        retry=retry_if_exception_type(requests.exceptions.Timeout) |
              retry_if_exception_type(requests.exceptions.ConnectionError)|
              retry_if_exception_type(requests.exceptions.RequestException),
        wait=wait_fixed(2),
        stop=stop_after_attempt(3),
        retry_error_callback=handle_retry_exception
    )
    def post(
        self, url: str, json: Dict[str, Any], headers: Dict[str, str]
    ) -> Dict[str, Any]:
        """Sends a POST request to the M-Pesa API.

        Args:
            url (str): The URL path for the request.
            json (Dict[str, Any]): The JSON payload for the request body.
            headers (Dict[str, str]): The HTTP headers for the request.

        Returns:
            Dict[str, Any]: The JSON response from the API.
        """
        full_url = f"{self.base_url}{url}"
        if self._session:
            response = self._session.post(full_url, json=json, headers=headers, timeout=10)
        else:
            response = requests.post(full_url, json=json, headers=headers, timeout=10)

        handle_request_error(response)
        
        return response.json()

    @retry(
        retry=retry_if_exception_type(requests.exceptions.Timeout) |
              retry_if_exception_type(requests.exceptions.ConnectionError)|
              retry_if_exception_type(requests.exceptions.RequestException),

        wait=wait_fixed(2),
        stop=stop_after_attempt(3),
        retry_error_callback=handle_retry_exception
    )
    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Sends a GET request to the M-Pesa API.

        Args:
            url (str): The URL path for the request.
            params (Optional[Dict[str, Any]]): The URL parameters.
            headers (Optional[Dict[str, str]]): The HTTP headers.

        Returns:
            Dict[str, Any]: The JSON response from the API.
        """
        if headers is None:
            headers = {}
        full_url = f"{self.base_url}{url}"
        if self._session:
            response = self._session.get(full_url, params=params, headers=headers, timeout=10)
        else:
            response = requests.get(full_url, params=params, headers=headers, timeout=10)

        handle_request_error(response)

        return response.json()
