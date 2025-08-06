import unittest
from mpesa.api.b2b import B2B


class B2BTests(unittest.TestCase):
    def setUp(self):
        self.mpesa_b2b_object = B2B("sandbox",
                                    app_key="wThWqhoWPORf7YjF3jgxdS1t9WQGn6GE",
                                    app_secret="kCQVbJIqmOnDXeNJ",
                                    sandbox_url="https://sandbox.safaricom.co.ke",
                                    live_url="https://safaricom.co.ke"
                                    )

        self.token = self.mpesa_b2b_object.authenticate()

    def test_transact(self):
        self.response = self.mpesa_b2b_object.transact(initiator="apitest526",
                                                       security_credential="ns5lxrntuGUBJvWwPpYSx726YfPjQhbbjwBnZlci51uT2WI7Ukm9Fwp2rYZPTMKHbxr/okWe8HwhcLeTk/lY2Nl7raAkDokRQ4hts4H+SN8wazhwMPEOdG5sXM2egUF/IUegJBSwao9FlXpOHcxzUT9ILF+x/HaD0L2DkrbCuixsQ/A3gwLZTkFiCUtYgWaJpvbVr9GiMFzAfZsHG9b/JCKnkytmCYiRt9jqXdHbJ9VzRM6EdLvtum7Tnmaq7AxDORtSS1J37B7Rgt6imV1VjD06m3rndkIWHbeew+xpJaMFYRV+erdPjFN5DPUTY1xSH4R4HzfN/JKSAaTZgeVh/w==",
                                                       command_id="BusinessPayBill", sender_identifier_type=4,
                                                       receiver_identifier_type=4, amount=1, party_a=601526,
                                                       party_b=600000, remarks="Testing b2c payment",
                                                       account_reference="testing-reference",
                                                       queue_timeout_url="http://my.api/timeout",
                                                       result_url="http://my.api/result")
        assert self.response.get('ConversationID', None) is not None or self.response.get('requestId', None) is not None
