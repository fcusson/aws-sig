"""module to test the sign function"""

from unittest import TestCase

from aws_sig.v4 import SigV4Signer


class TestSignatures(TestCase):

    def test_sign_returns_str_by_default(self):

        result = SigV4Signer.sign("key", "message")
        self.assertIsInstance(result, bytes)

    def test_sign_returns_bytes_on_request(self):

        result = SigV4Signer.sign("key", b"message", return_hex=True)
        self.assertIsInstance(result, str)
