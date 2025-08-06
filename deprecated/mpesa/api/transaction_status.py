import base64
import requests
from .auth import MpesaBase
import datetime


class TransactionStatus(MpesaBase):
    def __init__(self, env="sandbox", app_key=None, app_secret=None, sandbox_url=None, live_url=None):
        MpesaBase.__init__(self, env, app_key, app_secret, sandbox_url, live_url)
        self.authentication_token = self.authenticate()

    def check_transaction_status(self, party_a=None, identifier_type=None, remarks=None, initiator=None, passcode=None,
                                 result_url=None, queue_timeout_url=None, transaction_id=None,
                                 occassion=None, shortcode=None):
        """This method uses Mpesa's Transaction Status API to check the status of a transaction.

            **Args:**
                - party_a (str): Organization/MSISDN receiving the transaction - MSISDN or shortcode.
                - identifier_type (str): Type of organization receiving the transaction 1-MSISDN. 2-Till Number, 3-Shortcode.
                - remarks (str): Comments that are sent along with the transaction(maximum 100 characters).
                - initiator (str): This is the credential/username used to authenticate the transaction request.
                - passcode (str): Get from developer portal
                - result_url (str): The url that handles information from the mpesa API call.
                - transaction_id (str): Unique identifier to identify a transaction on M-Pesa.
                - queue_timeout_url (str): The url that stores information of timed out transactions.
                - result_url (str): The url that receives results from M-Pesa api call.
                - shortcode (int): The short code of the organization.
                - occassion (str):


            **Returns:**
                - ResultDesc': ,
                - CheckoutRequestID': ,
                - ResponseDescription': ,
                - MerchantRequestID': ,
                - ResponseCode': ,
                - ResultCode':


        """

        time = str(datetime.datetime.now()).split(".")[0].replace("-", "").replace(" ", "").replace(":", "")
        password = "{0}{1}{2}".format(str(shortcode), str(passcode), time)
        encoded = base64.b64encode(bytes(password, encoding='utf-8'))
        payload = {
            "CommandID": "TransactionStatusQuery",
            "PartyA": party_a,
            "IdentifierType": identifier_type,
            "Remarks": remarks,
            "Initiator": initiator,
            "SecurityCredential": encoded.decode("utf-8"),
            "QueueTimeOutURL": queue_timeout_url,
            "ResultURL": result_url,
            "TransactionID": transaction_id,
            "Occasion": occassion
        }
        headers = {'Authorization': 'Bearer {0}'.format(self.authentication_token), 'Content-Type': "application/json"}
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        saf_url = "{0}{1}".format(base_safaricom_url, "/mpesa/stkpushquery/v1/query")
        r = requests.post(saf_url, headers=headers, json=payload)
        return r.json()
