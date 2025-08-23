"""Facade for M-Pesa B2C APIs (Business to Customer, Account TopUp)."""

from mpesa_sdk.auth import TokenManager
from mpesa_sdk.http_client import HttpClient
from mpesa_sdk.B2C import B2C, B2CRequest, B2CResponse
from mpesa_sdk.B2C_account_top_up import (
    B2CAccountTopUp,
    B2CAccountTopUpRequest,
    B2CAccountTopUpResponse,
)


class B2CService:
    """Facade for all M-Pesa B2C APIs."""

    def __init__(self, http_client: HttpClient, token_manager: TokenManager) -> None:
        """Initialize the B2C service facade."""
        self.http_client = http_client
        self.token_manager = token_manager
        self.b2c = B2C(http_client=self.http_client, token_manager=self.token_manager)
        self.account_topup = B2CAccountTopUp(
            http_client=self.http_client, token_manager=self.token_manager
        )

    def send_payment(
        self,
        originator_conversation_id: str,
        initiator_name: str,
        security_credential: str,
        amount: int,
        shortcode: str,
        recipient_phone: str,
        queue_timeout_url: str,
        result_url: str,
        **kwargs,
    ) -> B2CResponse:
        """Initiate a B2C payment request.

        Args:
            originator_conversation_id: Unique ID for the transaction.
            initiator_name: The name of the initiator.
            security_credential: The encrypted security credential.
            amount: The amount to be sent.
            shortcode: The business short code.
            recipient_phone: The recipient's phone number.
            queue_timeout_url: URL for timeout notifications.
            result_url: URL for result notifications.
            kwargs: Fields for B2CRequest.

        Returns:
            B2CResponse: Response from M-Pesa API.
        """
        request = B2CRequest(
            originator_conversation_id=originator_conversation_id,
            initiator_name=initiator_name,
            security_credential=security_credential,
            amount=amount,
            shortcode=shortcode,
            recipient_phone=recipient_phone,
            queue_timeout_url=queue_timeout_url,
            result_url=result_url,
            **{k: v for k, v in kwargs.items() if k in B2CRequest.model_fields},
        )
        return self.b2c.send_payment(request)

    def account_topup(
        self,
        initiator: str,
        security_credential: str,
        amount: int,
        party_a: str,
        party_b: str,
        account_reference: str,
        requester: str,
        remarks: str,
        queue_timeout_url: str,
        result_url: str,
        **kwargs,
    ) -> B2CAccountTopUpResponse:
        """Initiate a B2C Account TopUp transaction.

        Args:
            initiator: The name of the initiator.
            security_credential: The encrypted security credential.
            amount: The amount to be topped up.
            party_a: The party initiating the transaction.
            party_b: The party receiving the transaction.
            account_reference: Reference for the transaction.
            requester: Optional requester name.
            remarks: Remarks for the transaction.
            queue_timeout_url: URL for timeout notifications.
            result_url: URL for result notifications.
            kwargs: Additional fields for B2CAccountTopUpRequest.

        Returns:
            B2CAccountTopUpResponse: Response from M-Pesa API.
        """
        request = B2CAccountTopUpRequest(
            initiator=initiator,
            security_credential=security_credential,
            amount=amount,
            party_a=party_a,
            party_b=party_b,
            account_reference=account_reference,
            requester=requester,
            remarks=remarks,
            queue_timeout_url=queue_timeout_url,
            result_url=result_url,
            **{
                k: v
                for k, v in kwargs.items()
                if k in B2CAccountTopUpRequest.model_fields
            },
        )
        return self.account_topup.topup(request)
