"""module to test the sorted_dictionary function"""

import unittest as test

from aws_sig._utils import sorted_dictionary


class TestDictionarySorting(test.TestCase):

    def test_sorted_dictionary_returns_itself(self):

        value = {
            "a": 1,
            "b": 2,
            "c": 3,
        }

        result = sorted_dictionary(value)

        self.assertEqual(value, result)

    def test_unsorted_dictionary(self):

        value = {
            "c": 3,
            "b": 2,
            "a": 1,
        }

        result = sorted_dictionary(value)

        expected = {
            "a": 1,
            "b": 2,
            "c": 3,
        }

        self.assertEqual(result, expected)
