"""module to test the url parse function"""

import unittest as test

from aws_sig._utils import url_parse


class TestParsing(test.TestCase):

    def setUp(self):

        self.url = "http://www.google.ca/?hello=world&test=true"

        self.result = url_parse(self.url)

    def test_parsing_provides_expected_scheme(self):
        self.assertEqual(self.result["scheme"], "http")

    def test_parsing_provides_expected_netloc(self):
        self.assertEqual(self.result["netloc"], "www.google.ca")

    def test_parsing_provides_expected_path(self):
        self.assertEqual(self.result["path"], "/")

    def test_parsing_provides_expected_query(self):
        self.assertEqual(
            self.result["query"],
            {"hello": "world", "test": "true"}
        )
