"""module to test the constructor of the credentials object"""

import unittest as test

from aws_sig._credentials import Credentials


class TestDataRetention(test.TestCase):

    def setUp(self):
        self.credentials = Credentials("access", "secret", "token")

    def test_access_key_value_is_retained(self):
        self.assertEqual(self.credentials.access_key, "access")

    def test_secret_key_value_is_retained(self):
        self.assertEqual(self.credentials.secret_key, "secret")

    def test_token_value_is_retained(self):
        self.assertEqual(self.credentials.token, "token")
