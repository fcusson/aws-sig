"""module to test the get_string_to_sign function"""

import unittest as test
import datetime as dt

from aws_sig.v4 import (
    SigV4,
    TIMESTAMP_FORMAT
)


class TestAwsCases(test.TestCase):

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
            "AWS4-HMAC-SHA256\n"
            "20130524T000000Z\n"
            "20130524/us-east-1/s3/aws4_request\n"
            "7344ae5b7ee6c3e7e6b0fe0640412a37625d1fbfff95c48bbb2dc43964946972"
        )

        canonical_request = (
            "GET\n"
            "/test.txt\n"
            "\n"
            "host:examplebucket.s3.amazonaws.com\n"
            "range:bytes=0-9\n"
            "x-amz-content-sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b"
            "934ca495991b7852b855\n"
            "x-amz-date:20130524T000000Z\n"
            "\n"
            "host;range;x-amz-content-sha256;x-amz-date\n"
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        )

        result = self.signer._get_string_to_sign(
            self.timestamp,
            canonical_request
        )

        self.assertEqual(result, expected)

    def test_put_object(self):

        expected = (
            "AWS4-HMAC-SHA256\n"
            "20130524T000000Z\n"
            "20130524/us-east-1/s3/aws4_request\n"
            "9e0e90d9c76de8fa5b200d8c849cd5b8dc7a3be3951ddb7f6a76b4158342019d"
        )

        canonical_request = (
            "PUT\n"
            "/test%24file.text\n"
            "\n"
            "date:Fri, 24 May 2013 00:00:00 GMT\n"
            "host:examplebucket.s3.amazonaws.com\n"
            "x-amz-content-sha256:44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e"
            "99e42034a8b803f8b072\n"
            "x-amz-date:20130524T000000Z\n"
            "x-amz-storage-class:REDUCED_REDUNDANCY\n"
            "\n"
            "date;host;x-amz-content-sha256;x-amz-date;x-amz-storage-class\n"
            "44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a8b803f8b072"
        )

        result = self.signer._get_string_to_sign(
            self.timestamp,
            canonical_request
        )

        self.assertEqual(result, expected)

    def test_get_bucket_lifecycle(self):

        expected = (
            "AWS4-HMAC-SHA256\n"
            "20130524T000000Z\n"
            "20130524/us-east-1/s3/aws4_request\n"
            "9766c798316ff2757b517bc739a67f6213b4ab36dd5da2f94eaebf79c77395ca"
        )

        canonical_request = (
            "GET\n"
            "/\n"
            "lifecycle=\n"
            "host:examplebucket.s3.amazonaws.com\n"
            "x-amz-content-sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b"
            "934ca495991b7852b855\n"
            "x-amz-date:20130524T000000Z\n"
            "\n"
            "host;x-amz-content-sha256;x-amz-date\n"
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        )

        result = self.signer._get_string_to_sign(
            self.timestamp,
            canonical_request
        )

        self.assertEqual(result, expected)

    def test_get_bucket(self):

        expected = (
            "AWS4-HMAC-SHA256\n"
            "20130524T000000Z\n"
            "20130524/us-east-1/s3/aws4_request\n"
            "df57d21db20da04d7fa30298dd4488ba3a2b47ca3a489c74750e0f1e7df1b9b7"
        )

        canonical_request = (
            "GET\n"
            "/\n"
            "max-keys=2&prefix=J\n"
            "host:examplebucket.s3.amazonaws.com\n"
            "x-amz-content-sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b"
            "934ca495991b7852b855\n"
            "x-amz-date:20130524T000000Z\n"
            "\n"
            "host;x-amz-content-sha256;x-amz-date\n"
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        )

        result = self.signer._get_string_to_sign(
            self.timestamp,
            canonical_request
        )

        self.assertEqual(result, expected)


class TestInvalidInput(test.TestCase):

    def test_invalid_type_raises_error(self):

        with self.assertRaises(TypeError):
            self.signer._get_string_to_sign("", "")

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
