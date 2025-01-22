"""module to test the constructor of the SigV4Signer object"""

import unittest as test

from aws_sig.v4 import SigV4


class TestDataRetention(test.TestCase):

    def setUp(self):

        self.signer = SigV4(
            "access",
            "secret",
            "region",
            "service",
            "token",
        )

    def test_credentials_value_is_retained(self):
        self.assertEqual(self.signer._credentials.access_key, "access")
        self.assertEqual(self.signer._credentials.secret_key, "secret")
        self.assertEqual(self.signer._credentials.token, "token")

    def test_service_value_is_retained(self):
        self.assertEqual(self.signer._service, "service")

    def test_region_value_is_retained(self):
        self.assertEqual(self.signer._region, "region")
