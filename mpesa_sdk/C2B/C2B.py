"""C2B: Handles M-Pesa C2B (Customer to Business) API interactions.

This module provides functionality to register C2B URLs, validate payments, and send confirmation responses
using the M-Pesa API. Requires a valid access token for authentication and uses the HttpClient for HTTP requests.
"""

from pydantic import BaseModel, ConfigDict
from mpesa_sdk.auth import TokenManager
from mpesa_sdk.http_client import HttpClient


from .schemas import (
    C2BRegisterUrlRequest,
    C2BRegisterUrlResponse,
    C2BValidationRequest,
    C2BValidationResponse,
    C2BConfirmationResponse,
    C2BValidationResultCodeType,
)


class C2B(BaseModel):
    """Represents the C2B API client for M-Pesa Customer to Business operations.

    https://developer.safaricom.co.ke/APIs/CustomerToBusinessRegisterURL

    Attributes:
        http_client (HttpClient): HTTP client for making requests to the M-Pesa API.
        token_manager (TokenManager): Manages access tokens for authentication.
    """

    http_client: HttpClient
    token_manager: TokenManager

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def register_url(self, request: C2BRegisterUrlRequest) -> C2BRegisterUrlResponse:
        """Registers validation and confirmation URLs for C2B payments.

        Returns:
            C2BRegisterUrlResponse: Response from the M-Pesa API after URL registration.
        """
        url = "/mpesa/c2b/v1/registerurl"
        headers = {
            "Authorization": f"Bearer {self.token_manager.get_token()}",
            "Content-Type": "application/json",
        }
        response_data = self.http_client.post(url, json=dict(request), headers=headers)

        # Safaricom API Bug: There is a typo in the response field name
        # "OriginatorCoversationID" should be "OriginatorConversationID"
        if "OriginatorCoversationID" in response_data:
            # Rename the field to match the expected schema
            # This is a workaround for the API inconsistency
            # and should be removed once the API is fixed.
            response_data["OriginatorConversationID"] = response_data.pop(
                "OriginatorCoversationID"
            )

        return C2BRegisterUrlResponse(**response_data)

    def validate_payment(
        self,
        result_code: C2BValidationResultCodeType,
        result_desc: str,
        request: C2BValidationRequest,
    ) -> C2BValidationResponse:
        """Handles validation of incoming C2B payment requests.

        Args:
            result_code (C2BValidationResultCodeType): Validation result code.
            result_desc (str): Description of the validation result not more than 90 characters.
            request (C2BValidationRequest): Incoming payment request.

        Returns:
            C2BValidationResponse: Response indicating acceptance or rejection of payment.
        """
        return C2BValidationResponse(
            ResultCode=result_code.value,
            ResultDesc=result_desc,
            ThirdPartyTransID=request.ThirdPartyTransID,
        )

    def confirm_payment(self) -> C2BConfirmationResponse:
        """Returns confirmation acknowledgment for C2B payments.

        Returns:
            C2BConfirmationResponse: Always indicates success.
        """
        # This method is typically called by your server when Safaricom posts to your ConfirmationURL.
        return C2BConfirmationResponse()
