"""Module to test the type_error_ol exception"""

from unittest import TestCase

from aws_sig.exceptions import TypeErrorOL


class TestConstructor(TestCase):

    def setUp(self):

        self.exception = TypeErrorOL(str, int)

    def test_proper_message_setup(self):
        self.assertEqual(
            str(self.exception),
            "Expected '<class 'str'>', received '<class 'int'>'",
        )
