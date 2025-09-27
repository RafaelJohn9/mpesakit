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
    """
    Handles non-successful HTTP responses.
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
    """
    Custom hook to handle exceptions after all retries fail.
    It raises a custom MpesaApiException with the appropriate error code.
    """
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


class MpesaHttpClient(HttpClient):
    """A client for making HTTP requests to the M-Pesa API."""

    base_url: str
    _session: Optional[requests.Session] = None

    def __init__(self, env: str = "sandbox", use_session: bool = False):
        self.base_url = self._resolve_base_url(env)
        if use_session:
            self._session = requests.Session()
            self._session.trust_env = False

    def _resolve_base_url(self, env: str) -> str:
        if env.lower() == "production":
            return "https://api.safaricom.co.ke"
        return "https://sandbox.safaricom.co.ke"

    def post(
        self, url: str, json: Dict[str, Any], headers: Dict[str, str]
    ) -> Dict[str, Any]:
        """Sends a POST request to the M-Pesa API.

        Args:
            url (str): The endpoint URL to send the POST request to.
            json (Dict[str, Any]): The JSON payload to include in the request body.
            headers (Dict[str, str]): The headers to include in the request.

        Returns:
            Dict[str, Any]: The JSON response from the M-Pesa API.

        Raises:
            MpesaApiException: If the request fails or returns an error response.
        """
        try:
            full_url = f"{self.base_url}{url}"
            if self._session:
                response = self._session.post(full_url, json=json, headers=headers, timeout=10)
            else:
                 response = requests.post(full_url, json=json, headers=headers, timeout=10)

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

            return response_data

        except requests.Timeout:
            raise MpesaApiException(
                MpesaError(
                    error_code="REQUEST_TIMEOUT",
                    error_message="Request to Mpesa timed out.",
                    status_code=None,
                )
            )
        except requests.ConnectionError:
            raise MpesaApiException(
                MpesaError(
                    error_code="CONNECTION_ERROR",
                    error_message="Failed to connect to Mpesa API. Check network or URL.",
                    status_code=None,
                )
            )
        except requests.RequestException as e:
            raise MpesaApiException(
                MpesaError(
                    error_code="REQUEST_FAILED",
                    error_message=f"HTTP request failed: {str(e)}",
                    status_code=None,
                    raw_response=None,
                )
            )

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Sends a GET request to the M-Pesa API.

        Args:
            url (str): The endpoint URL to send the GET request to.
            params (Optional[Dict[str, Any]]): The query parameters to include in the request.
            headers (Optional[Dict[str, str]]): The headers to include in the request.

        Returns:
            Dict[str, Any]: The JSON response from the M-Pesa API.

        Raises:
            MpesaApiException: If the request fails or returns an error response.
        """
        try:
            if headers is None:
                headers = {}
            full_url = f"{self.base_url}{url}"
            if self._session:
                response = self._session.get(
                full_url, params=params, headers=headers, timeout=10
            )  # Add timeout
            else:
                response=requests.get(full_url,params=params,headers=headers,timeout=10)

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

            return response_data

        except requests.Timeout:
            raise MpesaApiException(
                MpesaError(
                    error_code="REQUEST_TIMEOUT",
                    error_message="Request to Mpesa timed out.",
                    status_code=None,
                )
            )
        except requests.ConnectionError:
            raise MpesaApiException(
                MpesaError(
                    error_code="CONNECTION_ERROR",
                    error_message="Failed to connect to Mpesa API. Check network or URL.",
                    status_code=None,
                )
            )
        except requests.RequestException as e:
            raise MpesaApiException(
                MpesaError(
                    error_code="REQUEST_FAILED",
                    error_message=f"HTTP request failed: {str(e)}",
                    status_code=None,
                    raw_response=None,
                )
            )
