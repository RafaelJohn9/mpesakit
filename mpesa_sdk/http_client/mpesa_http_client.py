from typing import Dict, Any
import requests

from mpesa_sdk.errors import MpesaError, MpesaApiException


class MpesaHttpClient:
    base_url: str

    def __init__(self, env: str = "sandbox"):
        self.base_url = self._resolve_base_url(env)

    def _resolve_base_url(self, env: str) -> str:
        if env.lower() == "production":
            return "https://api.safaricom.co.ke"
        return "https://sandbox.safaricom.co.ke"

    def post(
        self, url: str, json: Dict[str, Any], headers: Dict[str, str]
    ) -> Dict[str, Any]:
        try:
            full_url = f"{self.base_url}{url}"
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
        self, url: str, params: Dict[str, Any] = None, headers: Dict[str, str] = None
    ) -> Dict[str, Any]:
        try:
            if headers is None:
                headers = {}
            full_url = f"{self.base_url}{url}"

            response = requests.get(
                full_url, params=params, headers=headers, timeout=10
            )  # Add timeout

            try:
                response_data = response.json()
            except ValueError:
                response_data = {"errorMessage": response.text.strip() or ""}

            if response.status_code != 200:
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
