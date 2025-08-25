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
        self.config = {
            "http_client": http_client,
            "token_manager": token_manager,
        }
        self.express = StkPushService(**self.config)
        self.b2c = B2CService(**self.config)
        self.b2b = B2BService(**self.config)
        self.transactions = TransactionService(**self.config)
        self.tax = TaxService(**self.config)
        self.balance = BalanceService(**self.config)
        self.reversal = ReversalService(**self.config)
        self.bill = BillService(**self.config)
        self.dynamic_qr = DynamicQRCodeService(**self.config)
        self.c2b = C2BService(**self.config)
        self.ratiba = RatibaService(**self.config)
