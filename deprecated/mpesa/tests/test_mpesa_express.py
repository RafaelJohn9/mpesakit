import unittest
from mpesa.api.mpesa_express import MpesaExpress


class MpesaExpressTests(unittest.TestCase):
    def setUp(self):
        self.mpesa_express_object = MpesaExpress("sandbox",
                                                 app_key="wThWqhoWPORf7YjF3jgxdS1t9WQGn6GE",
                                                 app_secret="kCQVbJIqmOnDXeNJ",
                                                 sandbox_url="https://sandbox.safaricom.co.ke",
                                                 live_url="https://safaricom.co.ke"
                                                 )

        self.token = self.mpesa_express_object.authenticate()

    def test_query(self):
        self.response = self.mpesa_express_object.query(business_shortcode="174379",
                                                        passcode="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
                                                        checkout_request_id="ws_co_123456789"
                                                        )
        print(str(self.response))
        assert self.response.get('requestId', None) is not None

    def test_stk_push(self):
        self.response = self.mpesa_express_object.stk_push(business_shortcode="174379",
                                                           passcode="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
                                                           amount=1,
                                                           phone_number=254708374149,
                                                           callback_url="http://my.api/callback",
                                                           reference_code="RANDOMREFERENCE",
                                                           description="RANDOM DESCRIPTION"
                                                           )
        print(str(self.response))
        assert self.response.get('ResponseDescription', None) is not None or self.response.get('errorMessage', None) is not None

