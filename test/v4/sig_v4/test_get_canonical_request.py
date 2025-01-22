"""module to test the get_canonical_request function"""

from unittest import TestCase
import datetime as dt

from aws_sig.v4 import (
    SigV4,
    TIMESTAMP_FORMAT
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

        result = self.signer._get_canonical_request(
            method="GET",
            host="examplebucket.s3.amazonaws.com",
            ressource="/test.txt",
            query={},
            headers={
                "range": "bytes=0-9",
                "x-amz-content-sha256": (
                    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7"
                    "852b855"
                )
            },
            time=self.timestamp,
        )

        self.assertEqual(expected, result)

    def test_put_object(self):

        expected = (
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

        result = self.signer._get_canonical_request(
            method="PUT",
            host="examplebucket.s3.amazonaws.com",
            ressource="/test$file.text",
            query={},
            headers={
                "date": "Fri, 24 May 2013 00:00:00 GMT",
                "x-amz-content-sha256": (
                    "44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a8b80"
                    "3f8b072"
                ),
                "x-amz-storage-class": "REDUCED_REDUNDANCY"
            },
            payload="Welcome to Amazon S3.",
            time=self.timestamp,
        )

        self.assertEqual(result, expected)

    def test_get_bucket_lifecyle(self):

        expected = (
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

        result = self.signer._get_canonical_request(
            method="GET",
            host="examplebucket.s3.amazonaws.com",
            ressource="/",
            query={
                "lifecycle": "",
            },
            headers={
                "x-amz-content-sha256": (
                    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7"
                    "852b855"
                ),
            },
            time=self.timestamp,
        )

        self.assertEqual(result, expected)

    def test_get_bucket(self):

        expected = (
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

        result = self.signer._get_canonical_request(
            method="GET",
            host="examplebucket.s3.amazonaws.com",
            ressource="/",
            query={
                "max-keys": "2",
                "prefix": "J",
            },
            headers={
                "x-amz-content-sha256": (
                    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7"
                    "852b855"
                ),
            },
            time=self.timestamp,
        )

        self.assertEqual(result, expected)


class TestInvalidInput(TestCase):

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

        self.base_data = {
            "method": "PUT",
            "host": "examplebucket.s3.amazonaws.com",
            "ressource": "/test$file.text",
            "query": {},
            "headers": {
                "date": "Fri, 24 May 2013 00:00:00 GMT",
                "x-amz-content-sha256": (
                    "44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a"
                    "8b803f8b072"
                ),
                "x-amz-storage-class": "REDUCED_REDUNDANCY"
            },
            "payload": "Welcome to Amazon S3.",
            "time": self.timestamp,

        }

    def test_invalid_payload_type(self):

        self.base_data["payload"] = 3.1415

        with self.assertRaises(TypeError):
            self.signer._get_canonical_request(**self.base_data)

    def test_invalid_header_type(self):

        self.base_data["headers"] = "test"

        with self.assertRaises(TypeError):
            self.signer._get_canonical_request(**self.base_data)

    def test_invalid_host_type(self):

        self.base_data["host"] = 42

        with self.assertRaises(TypeError):
            self.signer._get_canonical_request(**self.base_data)

    def test_invalid_time_type(self):

        self.base_data["time"] = "20130524T000000Z"

        with self.assertRaises(TypeError):
            self.signer._get_canonical_request(**self.base_data)

    def test_invalid_method_type(self):

        self.base_data["method"] = 1234436435

        with self.assertRaises(TypeError):
            self.signer._get_canonical_request(**self.base_data)

    def test_invalid_query_type(self):

        self.base_data["query"] = 1234436435

        with self.assertRaises(TypeError):
            self.signer._get_canonical_request(**self.base_data)
