import unittest
from mpesa.api.transaction_status import TransactionStatus


class TransactionStatusTests(unittest.TestCase):
    def setUp(self):
        self.mpesa_transaction_status_object = TransactionStatus("sandbox",
                                                                 app_key="wThWqhoWPORf7YjF3jgxdS1t9WQGn6GE",
                                                                 app_secret="kCQVbJIqmOnDXeNJ",
                                                                 sandbox_url="https://sandbox.safaricom.co.ke",
                                                                 live_url="https://safaricom.co.ke"
                                                                 )

        self.token = self.mpesa_transaction_status_object.authenticate()

    def test_check_transaction_status(self):
        self.response = self.mpesa_transaction_status_object.check_transaction_status(party_a="apitest526",
                                                                                      initiator="apitest526",
                                                                                      identifier_type=4,
                                                                                      remarks="Random REMARK",
                                                                                      passcode="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
                                                                                      transaction_id="LKXXXX1234",
                                                                                      occassion="Random OCCASSION",
                                                                                      shortcode=174379,
                                                                                      queue_timeout_url="http://my.api/timeout",
                                                                                      result_url="http://my.api/result"
                                                                                      )
        assert self.response.get('ConversationID', None) is not None or self.response.get('requestId', None) is not None
