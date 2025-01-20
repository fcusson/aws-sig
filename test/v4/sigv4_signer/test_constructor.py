"""module to test the constructor of the SigV4Signer object"""

import unittest as test

from aws_sig.v4 import SigV4Signer


class TestDataRetention(test.TestCase):

    def setUp(self):

        self.signer = SigV4Signer(
            "access",
            "secret",
            "token",
            "service",
            "region",
        )

    def test_credentials_value_is_retained(self):
        self.assertEqual(self.signer._credentials.access_key, "access")
        self.assertEqual(self.signer._credentials.secret_key, "secret")
        self.assertEqual(self.signer._credentials.token, "token")

    def test_service_value_is_retained(self):
        self.assertEqual(self.signer._service, "service")

    def test_region_value_is_retained(self):
        self.assertEqual(self.signer._region, "region")
