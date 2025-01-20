"""module to test the x_www_form_encode function"""

import unittest as test

from aws_sig._utils import x_www_form_encode


class TestEncoding(test.TestCase):

    def test_content_is_encoded(self):

        body = {
            "hello": "hello=world",
            "this": "is a test",
        }

        result = x_www_form_encode(body)

        expected = "hello=hello%3Dworld&this=is%20a%20test"

        self.assertEqual(result, expected)

    def test_no_body_returns_empty_string(self):

        result = x_www_form_encode(None)

        self.assertEqual(result, "")

    def test_skip_encoding_doesnt_encode_content(self):

        body = {
            "hello": "hello=world",
            "this": "is a test",
        }

        result = x_www_form_encode(body, True)

        expected = "hello=hello=world&this=is a test"

        self.assertEqual(result, expected)
