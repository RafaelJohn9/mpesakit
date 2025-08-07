from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime
import base64
from enum import Enum


class TransactionType(str, Enum):
    """
    Enum representing the types of M-Pesa transactions.

    CUSTOMER_PAYBILL_ONLINE: Used for PayBill transactions
    CUSTOMER_BUYGOODS_ONLINE: Used for Till Number transactions
    """

    CUSTOMER_PAYBILL_ONLINE = "CustomerPayBillOnline"
    CUSTOMER_BUYGOODS_ONLINE = "CustomerBuyGoodsOnline"


class StkPushRequest(BaseModel):
    """
    Represents the request payload for initiating an M-Pesa STK Push transaction.

    https://developer.safaricom.co.ke/APIs/MpesaExpressSimulate

    Attributes:
        BusinessShortCode (int): Organization's shortcode (Paybill or Buygoods - 5 to 6 digits).
        Password (Optional[str]): Base64 encoded string (Shortcode+Passkey+Timestamp).
        Timestamp (Optional[str]): Timestamp in the format YYYYMMDDHHmmss.
        TransactionType (str): Type of transaction (CustomerPayBillOnline for PayBill, CustomerBuyGoodsOnline for Till Numbers).
        Amount (int): Amount to be transacted (whole numbers only).
        PartyA (str): Phone number sending money in format 2547XXXXXXXX.
        PartyB (str): Organization shortcode receiving the funds (5-6 digits).
        PhoneNumber (str): Mobile number to receive the STK Pin Prompt in format 2547XXXXXXXX.
        CallBackURL (str): Secure URL to receive M-Pesa API notifications.
        AccountReference (str): Identifier for the transaction (max 12 characters).
        TransactionDesc (str): Additional transaction information (max 13 characters).
        Passkey (Optional[str]): Passkey for the shortcode (used to generate Password if not provided).
    """

    BusinessShortCode: int = Field(
        ...,
        description="Organization's shortcode (Paybill or Buygoods - 5 to 6 digits).",
    )
    Password: Optional[str] = Field(
        None, description="Base64 encoded string (Shortcode+Passkey+Timestamp)."
    )
    Timestamp: Optional[str] = Field(
        None, description="Timestamp in the format YYYYMMDDHHmmss."
    )
    TransactionType: str = Field(
        ...,
        description="Type of transaction (CustomerPayBillOnline for PayBill, CustomerBuyGoodsOnline for Till Numbers).",
    )
    Amount: int = Field(
        ..., description="Amount to be transacted (whole numbers only)."
    )
    PartyA: str = Field(
        ..., description="Phone number sending money in format 2547XXXXXXXX."
    )
    PartyB: str = Field(
        ..., description="Organization shortcode receiving the funds (5-6 digits)."
    )
    PhoneNumber: str = Field(
        ...,
        description="Mobile number to receive the STK Pin Prompt in format 2547XXXXXXXX.",
    )
    CallBackURL: str = Field(
        ..., description="Secure URL to receive M-Pesa API notifications."
    )
    AccountReference: str = Field(
        ..., description="Identifier for the transaction (max 12 characters)."
    )
    TransactionDesc: str = Field(
        ..., description="Additional transaction information (max 13 characters)."
    )
    Passkey: Optional[str] = Field(
        None,
        description="Passkey for the shortcode (used to generate Password if not provided).",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "BusinessShortCode": 654321,
                "Password": "bXlwYXNzd29yZA==",
                "Timestamp": "20240607123045",
                "TransactionType": "CustomerPayBillOnline",
                "Amount": 10,
                "PartyA": "254712345678",
                "PartyB": 654321,
                "PhoneNumber": "254712345678",
                "CallBackURL": "https://example.com/callback",
                "AccountReference": "Test",
                "TransactionDesc": "Payment",
            }
        }

    def __init__(self, **data):
        password = data.get("Password")
        passkey = data.get("Passkey")
        shortcode = data.get("BusinessShortCode")
        timestamp = data.get("Timestamp")

        if not timestamp:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            data["Timestamp"] = timestamp

        if not password and passkey and shortcode and timestamp:
            data["Password"] = self._generate_password(shortcode, passkey, timestamp)
        super().__init__(**data)

    @staticmethod
    def _generate_password(shortcode: int, passkey: str, timestamp: str) -> str:
        raw = f"{shortcode}{passkey}{timestamp}"
        return base64.b64encode(raw.encode("utf-8")).decode("utf-8")

    @model_validator(mode="before")
    @classmethod
    def validate_request(cls, values):
        """
        Validate the STK Push request fields.
        """
        password = values.get("Password")
        passkey = values.get("Passkey")

        if not password and not passkey:
            raise ValueError("Either 'Password' or 'Passkey' must be provided")

        # Validate phone number format (12 digits starting with 254)
        phone_number = values.get("PhoneNumber", "")
        if not (
            phone_number.isdigit()
            and len(phone_number) == 12
            and phone_number.startswith("254")
        ):
            raise ValueError("PhoneNumber must be 12 digits in the format 254XXXXXXXXX")

        # Validate that AccountReference is provided when TransactionType is CustomerPayBillOnline
        transaction_type = values.get("TransactionType")
        account_ref = values.get("AccountReference")
        if (
            transaction_type == TransactionType.CUSTOMER_PAYBILL_ONLINE.value
            and not account_ref
        ):
            raise ValueError("AccountReference must be provided when using PayBill")

        account_ref = values.get("AccountReference", "")
        if account_ref and len(account_ref) > 12:
            raise ValueError("AccountReference must be 12 characters or less")

        trans_desc = values.get("TransactionDesc", "")
        if trans_desc and len(trans_desc) > 13:
            raise ValueError("TransactionDesc must be 13 characters or less")

        return values


class StkPushResponse(BaseModel):
    """
    Represents the response returned after initiating an M-Pesa STK Push transaction.

    https://developer.safaricom.co.ke/APIs/MpesaExpressQuery
    Attributes:
        MerchantRequestID (str): Global unique identifier for the submitted payment request.
        CheckoutRequestID (str): Global unique identifier for the processed checkout transaction request.
        ResponseCode (int): Numeric status code indicating the status of the transaction submission. 0 means success.
        ResultDesc (str): Message from the API giving the status of the request processing.
        ResponseDescription (str): Acknowledgment message from the API about the request submission status.
        ResultCode (int): Numeric status code indicating the status of the transaction processing. 0 means success.
        CustomerMessage (str): Message that can be displayed to the customer as acknowledgment of payment request submission.
    """

    MerchantRequestID: str = Field(
        ..., description="Global unique Identifier for any submitted payment request."
    )
    CheckoutRequestID: str = Field(
        ...,
        description="Global unique identifier of the processed checkout transaction request.",
    )
    ResponseCode: int = Field(
        ...,
        description="Numeric status code indicating the status of the transaction submission. 0 means success.",
    )
    ResponseDescription: str = Field(
        ...,
        description="Acknowledgment message from the API about the request submission status.",
    )
    CustomerMessage: str = Field(
        ...,
        description="Message that can be displayed to the customer as acknowledgment of payment request submission.",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "MerchantRequestID": "16813-1590513-1",
                "CheckoutRequestID": "ws_CO_DMZ_123212312_2342347678234",
                "ResponseCode": 0,
                "ResultDesc": "The service request is processed successfully.",
                "ResponseDescription": "The service request has been accepted successfully",
                "CustomerMessage": "Success. Request accepted for processing.",
            }
        }


class StkPushCallbackMetadataItem(BaseModel):
    """
    Represents an item in the CallbackMetadata array from an M-Pesa STK Push callback.

    Attributes:
        Name (str): The name of the metadata field (e.g., Amount, MpesaReceiptNumber)
        Value (Optional[str | int | float]): The value of the metadata field
    """

    Name: str = Field(..., description="Name of the metadata field")
    Value: Optional[str | int | float] = Field(
        None, description="Value of the metadata field"
    )


class StkPushCallbackMetadata(BaseModel):
    """
    Represents the metadata returned in a successful STK Push transaction callback.

    Attributes:
        Item (list[StkPushCallbackMetadataItem]): List of metadata items with transaction details
    """

    Item: list[StkPushCallbackMetadataItem] = Field(
        ..., description="Array containing transaction details"
    )


class StkCallback(BaseModel):
    """
    Represents the STK Push callback data contained in the stkCallback field.

    Attributes:
        MerchantRequestID (str): Global unique identifier for the payment request
        CheckoutRequestID (str): Global unique identifier of the processed checkout transaction
        ResultCode (int): Numeric status code (0 means successful)
        ResultDesc (str): Description of the result
        CallbackMetadata (Optional[StkPushCallbackMetadata]): Additional transaction details for successful transactions
    """

    MerchantRequestID: str = Field(
        ..., description="Global unique identifier for the payment request"
    )
    CheckoutRequestID: str = Field(
        ...,
        description="Global unique identifier of the processed checkout transaction request",
    )
    ResultCode: int = Field(
        ...,
        description="Numeric status code indicating the status of the transaction processing. 0 means success",
    )
    ResultDesc: str = Field(
        ..., description="Message giving the status of the request processing"
    )
    CallbackMetadata: Optional[StkPushCallbackMetadata] = Field(
        None,
        description="Contains additional transaction details for successful transactions",
    )


class StkPushCallbackBody(BaseModel):
    """
    Represents the body of the STK Push callback.

    Attributes:
        stkCallback (StkCallback): The STK callback data
    """

    stkCallback: StkCallback = Field(
        ..., description="Contains the STK Push callback details"
    )


class StkPushCallback(BaseModel):
    """
    Represents the full STK Push callback received from M-Pesa.

    This model represents the data sent to the callback URL after an STK Push
    transaction has been processed by M-Pesa.

    Attributes:
        Body (StkPushCallbackBody): The body of the callback containing the transaction details
    """

    Body: StkPushCallbackBody = Field(
        ..., description="Root object containing stkCallback data"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "Body": {
                    "stkCallback": {
                        "MerchantRequestID": "29115-34620561-1",
                        "CheckoutRequestID": "ws_CO_191220191020363925",
                        "ResultCode": 0,
                        "ResultDesc": "The service request is processed successfully.",
                        "CallbackMetadata": {
                            "Item": [
                                {"Name": "Amount", "Value": 1.0},
                                {
                                    "Name": "MpesaReceiptNumber",
                                    "Value": "LHG31AA5TX",
                                },
                                {"Name": "Balance"},
                                {
                                    "Name": "TransactionDate",
                                    "Value": 20191219102115,
                                },
                                {"Name": "PhoneNumber", "Value": 254712345678},
                            ]
                        },
                    }
                }
            }
        }

    def get_metadata_value(self, name: str) -> Optional[str | int | float]:
        """
        Helper method to get a specific metadata value by name.

        Args:
            name: The name of the metadata field

        Returns:
            The value of the metadata field, or None if not found
        """
        if not (
            self.Body.stkCallback.CallbackMetadata
            and self.Body.stkCallback.CallbackMetadata.Item
        ):
            return None

        for item in self.Body.stkCallback.CallbackMetadata.Item:
            if item.Name == name:
                return item.Value
        return None

    @property
    def amount(self) -> Optional[float]:
        """Gets the transaction amount"""
        value = self.get_metadata_value("Amount")
        return float(value) if value is not None else None

    @property
    def mpesa_receipt_number(self) -> Optional[str]:
        """Gets the M-PESA receipt number"""
        value = self.get_metadata_value("MpesaReceiptNumber")
        return str(value) if value is not None else None

    @property
    def balance(self) -> Optional[float]:
        """Gets the account balance"""
        value = self.get_metadata_value("Balance")
        return float(value) if value is not None else None

    @property
    def transaction_date(self) -> Optional[str]:
        """Gets the transaction date"""
        value = self.get_metadata_value("TransactionDate")
        return str(value) if value is not None else None

    @property
    def phone_number(self) -> Optional[str]:
        """Gets the customer's phone number"""
        value = self.get_metadata_value("PhoneNumber")
        return str(value) if value is not None else None

    @property
    def is_successful(self) -> bool:
        """
        Indicates whether the STK Push transaction was successful.

        Returns:
            bool: True if ResultCode is 0, False otherwise.
        """
        return self.Body.stkCallback.ResultCode == 0
