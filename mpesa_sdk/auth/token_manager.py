import base64
from datetime import datetime
from pydantic import BaseModel, PrivateAttr
from typing import Optional

from mpesa_sdk.http_client import MpesaHttpClient
from mpesa_sdk.auth import AccessToken
from mpesa_sdk.errors import MpesaError, MpesaApiException


class TokenManager(BaseModel):
    consumer_key: str
    consumer_secret: str
    http_client: MpesaHttpClient

    _access_token: Optional[AccessToken] = PrivateAttr(default=None)

    class Config:
        arbitrary_types_allowed = True

    def _get_basic_auth_header(self) -> str:
        credentials = f"{self.consumer_key}:{self.consumer_secret}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
            "utf-8"
        )
        return f"Basic {encoded_credentials}"

    def get_token(self, force_refresh: bool = False) -> str:
        if (
            self._access_token
            and not self._access_token.is_expired()
            and not force_refresh
        ):
            return self._access_token.token

        url = "/oauth/v1/generate"
        params = {"grant_type": "client_credentials"}
        headers = {"Authorization": self._get_basic_auth_header()}

        try:
            response = self.http_client.get(url, headers=headers, params=params)
        except MpesaApiException as e:
            if e.error.status_code == 400 and (
                e.error.error_message is None or len(e.error.error_message) == 0
            ):
                raise MpesaApiException(
                    MpesaError(
                        error_code="AUTH_INVALID_CREDENTIALS",
                        error_message="Invalid credentials provided. Please check your consumer key and secret.",
                        status_code=400,
                    )
                ) from e  # Preserve traceback
            # Re-raise other errors as-is
            raise

        token = response.get("access_token")
        expires_in = int(response.get("expires_in", 3600))

        if not token:
            raise MpesaApiException(
                MpesaError(
                    error_code="TOKEN_MISSING",
                    error_message="No access token returned by Mpesa API.",
                    status_code=None,
                    raw_response=response,
                )
            )

        self._access_token = AccessToken(
            token=token,
            creation_datetime=datetime.now(),
            expiration_time=expires_in,
        )
        return self._access_token.token
