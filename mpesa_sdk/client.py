"""MpesaClient: A unified client for M-PESA services."""

from mpesa_sdk.auth import TokenManager
from mpesa_sdk.http_client import HttpClient
from mpesa_sdk.services import (
    B2BService,
    B2CService,
    BalanceService,
    BillService,
    C2BService,
    DynamicQRCodeService,
    StkPushService,
    RatibaService,
    ReversalService,
    TaxService,
    TransactionService,
)


class MpesaClient:
    """Unified client for all M-PESA services."""

    def __init__(self, http_client: HttpClient, token_manager: TokenManager):
        """Initialize the MpesaClient with all service facades."""
        # express => M-PESA STK Push
        self.express = StkPushService(
            http_client=http_client, token_manager=token_manager
        )

        # b2c => M-PESA Business to Customer services
        self.b2c = B2CService(http_client=http_client, token_manager=token_manager)

        # b2b => M-PESA Business to Business services
        self.b2b = B2BService(http_client=http_client, token_manager=token_manager)

        # transaction => M-PESA Transaction status services
        self.transactions = TransactionService(
            http_client=http_client, token_manager=token_manager
        )

        # tax => M-PESA Tax services
        self.tax = TaxService(http_client=http_client, token_manager=token_manager)

        # balance => M-PESA Account balance services
        self.balance = BalanceService(
            http_client=http_client, token_manager=token_manager
        )

        # reversal => M-PESA Transaction reversal services
        self.reversal = ReversalService(
            http_client=http_client, token_manager=token_manager
        )

        # bill => M-PESA Bill services
        self.bill = BillService(http_client=http_client, token_manager=token_manager)

        # dynamic_qr => M-PESA Dynamic QR services
        self.dynamic_qr = DynamicQRCodeService(
            http_client=http_client, token_manager=token_manager
        )

        # c2b => M-PESA Customer to Business services
        self.c2b = C2BService(http_client=http_client, token_manager=token_manager)

        # ratiba => M-PESA Ratiba services
        self.ratiba = RatibaService(
            http_client=http_client, token_manager=token_manager
        )
