import requests
from .auth import MpesaBase


class Reversal(MpesaBase):
    def __init__(self, env="sandbox", app_key=None, app_secret=None, sandbox_url=None, live_url=None):
        MpesaBase.__init__(self, env, app_key, app_secret, sandbox_url, live_url)
        self.authentication_token = self.authenticate()

    def reverse(self, initiator=None, security_credential=None, command_id="TransactionReversal", transaction_id=None,
                 amount=None, receiver_party=None, receiver_identifier_type=None, queue_timeout_url=None,
                result_url=None, remarks=None, occassion=None):
        """This method uses Mpesa's Transaction Reversal API to reverse a M-Pesa transaction.

                                                            **Args:**
                                                                - initiator (str): Username used to authenticate the transaction.
                                                                - security_credential (str): Generate from developer portal
                                                                - command_id (str): TransactionReversal
                                                                - transaction_id (str): Unique identifier to identify a transaction on M-Pesa.
                                                                - amount (int): The amount being transacted
                                                                - receiver_party (int): Organization/MSISDN making the transaction - Shortcode (6 digits) - MSISDN (12 digits).
                                                                - receiver_identifier_type (int): MSISDN receiving the transaction (12 digits).
                                                                - queue_timeout_url (str): The url that handles information of timed out transactions.
                                                                - result_url (str): The url that receives results from M-Pesa api call.
                                                                - remarks (str): Comments that are sent along with the transaction(maximum 100 characters)
                                                                - occassion (str):


                                                            **Returns:**
                                                                - OriginatorConverstionID (str): The unique request ID for tracking a transaction.
                                                                - ConversationID (str): The unique request ID returned by mpesa for each request made
                                                                - ResponseDescription (str): Response Description message


        """

        payload = {
            "Initiator": initiator,
            "SecurityCredential": security_credential,
            "CommandID": command_id,
            "TransactionID": transaction_id,
            "Amount": amount,
            "ReceiverParty": receiver_party,
            "ReceiverIdentifierType": receiver_identifier_type,
            "QueueTimeOutURL": queue_timeout_url,
            "ResultURL": result_url,
            "Remarks": remarks,
            "Occassion": occassion
        }
        headers = {'Authorization': 'Bearer {0}'.format(self.authentication_token), 'Content-Type': "application/json"}
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        saf_url = "{0}{1}".format(base_safaricom_url, "/mpesa/reversal/v1/request")
        r = requests.post(saf_url, headers=headers, json=payload)
        return r.json()

