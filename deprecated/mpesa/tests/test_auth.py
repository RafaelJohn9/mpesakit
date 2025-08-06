import unittest
from mpesa.api.auth import MpesaBase


class AuthTests(unittest.TestCase):
    def setUp(self):
        mpesa_auth_object = MpesaBase("sandbox",
                                      app_key="wThWqhoWPORf7YjF3jgxdS1t9WQGn6GE",
                                      app_secret="kCQVbJIqmOnDXeNJ",
                                      sandbox_url="https://sandbox.safaricom.co.ke",
                                      live_url="https://safaricom.co.ke"
                                      )

        self.token = mpesa_auth_object.authenticate()

    def test_authenticate_token(self):
        self.assertEqual(len(self.token), 28)
