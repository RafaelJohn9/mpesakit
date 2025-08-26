"""MpesaRatiba: Handles M-Pesa Standing Order (Ratiba) API interactions.

This module provides functionality to initiate a Standing Order transaction and handle result/timeout notifications
using the M-Pesa API. Requires a valid access token for authentication and uses the HttpClient for HTTP requests.
"""

from pydantic import BaseModel, ConfigDict
from mpesakit.auth import TokenManager
from mpesakit.http_client import HttpClient

from .schemas import (
    StandingOrderRequest,
    StandingOrderResponse,
)


class MpesaRatiba(BaseModel):
    """Represents the Standing Order (Ratiba) API client for M-Pesa operations.

    https://developer.safaricom.co.ke/APIs/MpesaRatiba

    Attributes:
        http_client (HttpClient): HTTP client for making requests to the M-Pesa API.
        token_manager (TokenManager): Manages access tokens for authentication.
    """

    http_client: HttpClient
    token_manager: TokenManager

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def create_standing_order(
        self, request: StandingOrderRequest
    ) -> StandingOrderResponse:
        """Initiates a Standing Order transaction.

        Args:
            request (StandingOrderRequest): The Standing Order request data.

        Returns:
            StandingOrderResponse: Response from the M-Pesa API.
        """
        url = "/standingorder/v1/createStandingOrderExternal"
        headers = {
            "Authorization": f"Bearer {self.token_manager.get_token()}",
            "Content-Type": "application/json",
        }
        response_data = self.http_client.post(
            url, json=request.model_dump(mode="json"), headers=headers
        )
        return StandingOrderResponse(**response_data)
