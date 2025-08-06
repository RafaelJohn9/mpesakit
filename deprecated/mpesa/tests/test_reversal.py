import unittest
from mpesa.api.reversal import Reversal


class ReversalTests(unittest.TestCase):
    def setUp(self):
        self.mpesa_reversal_object = Reversal("sandbox",
                                              app_key="wThWqhoWPORf7YjF3jgxdS1t9WQGn6GE",
                                              app_secret="kCQVbJIqmOnDXeNJ",
                                              sandbox_url="https://sandbox.safaricom.co.ke",
                                              live_url="https://safaricom.co.ke"
                                              )

        self.token = self.mpesa_reversal_object.authenticate()

    def test_reverse(self):
        self.response = self.mpesa_reversal_object.reverse(initiator="apitest526",
                                                           security_credential="ns5lxrntuGUBJvWwPpYSx726YfPjQhbbjwBnZlci51uT2WI7Ukm9Fwp2rYZPTMKHbxr/okWe8HwhcLeTk/lY2Nl7raAkDokRQ4hts4H+SN8wazhwMPEOdG5sXM2egUF/IUegJBSwao9FlXpOHcxzUT9ILF+x/HaD0L2DkrbCuixsQ/A3gwLZTkFiCUtYgWaJpvbVr9GiMFzAfZsHG9b/JCKnkytmCYiRt9jqXdHbJ9VzRM6EdLvtum7Tnmaq7AxDORtSS1J37B7Rgt6imV1VjD06m3rndkIWHbeew+xpJaMFYRV+erdPjFN5DPUTY1xSH4R4HzfN/JKSAaTZgeVh/w==",
                                                           command_id="TransactionReversal",
                                                           transaction_id='LKXXXX1234',
                                                           amount=1, receiver_party=601526,
                                                           receiver_identifier_type=11,
                                                           occassion="Random OCCASSION",
                                                           remarks="Testing REVERSAL",
                                                           queue_timeout_url="http://my.api/timeout",
                                                           result_url="http://my.api/result",
                                                           )
        print(str(self.response))
        assert self.response.get('ConversationID', None) is not None or self.response.get('requestId', None) is not None
