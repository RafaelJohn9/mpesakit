import unittest
from mpesa.api.c2b import C2B


class C2BTests(unittest.TestCase):
    def setUp(self):
        self.mpesa_c2b_object = C2B("sandbox",
                                    app_key="wThWqhoWPORf7YjF3jgxdS1t9WQGn6GE",
                                    app_secret="kCQVbJIqmOnDXeNJ",
                                    sandbox_url="https://sandbox.safaricom.co.ke",
                                    live_url="https://safaricom.co.ke"
                                    )

        self.token = self.mpesa_c2b_object.authenticate()

    def test_register(self):
        self.response = self.mpesa_c2b_object.register(shortcode="601526",
                                                       response_type="Completed",
                                                       confirmation_url="http://my.api/confirm",
                                                       validation_url="http://my.api/validate"
                                                       )
        print(str(self.response))
        assert self.response.get('ResponseDescription', None) is not None or self.response.get('errorMessage', None) is not None

    def test_simulate(self):
        self.response = self.mpesa_c2b_object.simulate(command_id="CustomerBuyGoodsOnline",
                                                       amount=1,
                                                       msisdn=254708374149,
                                                       bill_ref_number="RANDOM",
                                                       shortcode="601526"
                                                       )
        print(str(self.response))
        assert self.response.get('ConversationID', None) is not None or self.response.get('requestId', None) is not None
