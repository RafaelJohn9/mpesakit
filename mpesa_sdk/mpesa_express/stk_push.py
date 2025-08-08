"""STK Push: Initiates an M-Pesa STK Push transaction.

This module provides functionality to initiate an M-Pesa STK Push transaction using the M-Pesa API.
It requires a valid access token for authentication and uses the MpesaHttpClient for making HTTP requests.
"""

from pydantic import BaseModel, ConfigDict

from mpesa_sdk.auth import TokenManager
from mpesa_sdk.http_client import MpesaHttpClient
from .schemas import StkPushRequest, StkPushResponse


class StkPush(BaseModel):
    """Represents the request payload for initiating an M-Pesa STK Push transaction.

    https://developer.safaricom.co.ke/APIs/MpesaExpressQuery
    https://developer.safaricom.co.ke/APIs/MpesaExpressSimulate
    Attributes:
        http_client (MpesaHttpClient): The HTTP client used to make requests to the M-Pesa API.
        request (StkPushRequest): The request data for the STK Push transaction.
    """

    http_client: MpesaHttpClient
    token_manager: TokenManager

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def push(self, request: StkPushRequest) -> StkPushResponse:
        """Initiates an M-Pesa STK Push transaction.

        Returns:
            StkPushResponse: The response from the M-Pesa API after initiating the STK Push.
        """
        url = "/mpesa/stkpush/v1/processrequest"
        headers = {
            "Authorization": f"Bearer {self.token_manager.get_token()}",
            "Content-Type": "application/json",
        }

        response_data = self.http_client.post(url, json=dict(request), headers=headers)

        return StkPushResponse(**response_data)
