"""module to test the query_parse function"""

import unittest as test

from aws_sig._utils import query_parse


class TestQueryParsing(test.TestCase):

    def test_query_is_converted_to_dictionary(self):

        value = "hello=hello%3Dworld&this=is%20a%20test"
        result = query_parse(value)
        expected = {
            "hello": "hello%3Dworld",
            "this": "is%20a%20test",
        }

        self.assertEqual(result, expected)

    def test_no_body_returns_empty_dictionary(self):

        result = query_parse(None)

        self.assertEqual(result, {})

    def test_empty_string_returns_empty_dictionary(self):

        result = query_parse("")

        self.assertEqual(result, {})


class TestInvalidInput(test.TestCase):

    def test_none_string_raises_error(self):

        with self.assertRaises(TypeError):
            query_parse(1)

    def test_wrong_format_query_raises_error(self):

        value = "hello=world&test"

        with self.assertRaises(ValueError):
            query_parse(value)
