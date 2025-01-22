"""module to test the get signature function"""

from unittest import TestCase
import datetime as dt

from aws_sig.v4 import (
    SigV4,
    TIMESTAMP_FORMAT,
)


class TestAwsCases(TestCase):

    def setUp(self):

        # these are mock keys from aws documetation
        access_key = "AKIAIOSFODNN7EXAMPLE"
        secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        service = "s3"
        region = "us-east-1"

        self.signer = SigV4(
            aws_access_key=access_key,
            aws_secret_key=secret_key,
            service=service,
            region=region,
        )

        self.timestamp = dt.datetime.strptime(
            "20130524T000000Z",
            TIMESTAMP_FORMAT
        )

    def test_get_object(self):

        expected = (
            "f0e8bdb87c964420e857bd35b5d6ed310bd44f0170aba48dd91039c6036bdb41"
        )

        result = self.signer._get_signature(
            (
                "AWS4-HMAC-SHA256\n"
                "20130524T000000Z\n"
                "20130524/us-east-1/s3/aws4_request\n"
                "7344ae5b7ee6c3e7e6b0fe0640412a37625d1fbfff95c48bbb2dc43964946"
                "972"
            ),
            self.timestamp
        )

        self.assertEqual(result, expected)

    def test_put_object(self):

        expected = (
            "98ad721746da40c64f1a55b78f14c238d841ea1380cd77a1b5971af0ece108bd"
        )

        result = self.signer._get_signature(
            (
                "AWS4-HMAC-SHA256\n"
                "20130524T000000Z\n"
                "20130524/us-east-1/s3/aws4_request\n"
                "9e0e90d9c76de8fa5b200d8c849cd5b8dc7a3be3951ddb7f6a76b41583420"
                "19d"
            ),
            self.timestamp
        )

        self.assertEqual(result, expected)

    def test_get_bucket_lifecycle(self):

        expected = (
            "fea454ca298b7da1c68078a5d1bdbfbbe0d65c699e0f91ac7a200a0136783543"
        )

        result = self.signer._get_signature(
            (
                "AWS4-HMAC-SHA256\n"
                "20130524T000000Z\n"
                "20130524/us-east-1/s3/aws4_request\n"
                "9766c798316ff2757b517bc739a67f6213b4ab36dd5da2f94eaebf79c7739"
                "5ca"
            ),
            self.timestamp
        )

        self.assertEqual(result, expected)

    def test_get_bucket(self):

        expected = (
            "34b48302e7b5fa45bde8084f4b7868a86f0a534bc59db6670ed5711ef69dc6f7"
        )

        result = self.signer._get_signature(
            (
                "AWS4-HMAC-SHA256\n"
                "20130524T000000Z\n"
                "20130524/us-east-1/s3/aws4_request\n"
                "df57d21db20da04d7fa30298dd4488ba3a2b47ca3a489c74750e0f1e7df1b"
                "9b7"
            ),
            self.timestamp
        )

        self.assertEqual(result, expected)


class TestInvalidInput(TestCase):

    def test_invalid_type_raises_error(self):

        with self.assertRaises(TypeError):
            self.signer._get_signature("", "20230405T000000Z")

    def setUp(self):

        # these are mock keys from aws documetation
        access_key = "AKIAIOSFODNN7EXAMPLE"
        secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        service = "s3"
        region = "us-east-1"

        self.signer = SigV4(
            aws_access_key=access_key,
            aws_secret_key=secret_key,
            service=service,
            region=region,
        )

        self.timestamp = dt.datetime.strptime(
            "20130524T000000Z",
            TIMESTAMP_FORMAT
        )
