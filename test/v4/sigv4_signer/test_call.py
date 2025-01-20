"""module to test the call dunder of the SigV4Signer"""

import unittest as test
from unittest.mock import MagicMock

from aws_sig.v4 import SigV4Signer


class TestAuthenticationCall(test.TestCase):

    def setUp(self):
        self.signer = SigV4Signer("access", "secret", "token")

    def test_basic_request(self):

        mock_request = MagicMock()

        mock_request.url = "https://www.google.ca/test?hello=world"
        mock_request.headers = None
        mock_request.body = None

        self.signer(mock_request)

    def test_request_without_token(self):

        self.signer._credentials.token = None

        mock_request = MagicMock()

        mock_request.url = "https://www.google.ca/test?hello=world"
        mock_request.headers = None
        mock_request.body = None

        self.signer(mock_request)

    def test_request_with_content_header(self):

        mock_request = MagicMock()

        mock_request.url = "https://www.google.ca/test?hello=world"
        mock_request.headers = {
            "X-Amz-Content-SHA256": "test"
        }
        mock_request.body = None

        self.signer(mock_request)

    def test_request_with_byte_body(self):

        mock_request = MagicMock()

        mock_request.url = "https://www.google.ca/test?hello=world"
        mock_request.headers = {
            "Authorization": "test",
            "X-Amz-Content-SHA256": "test"
        }
        mock_request.body = b"test"

        self.signer(mock_request)
