"""moduel to test the get_authorzation_header method"""

import unittest as test

from aws_sig.v4 import SigV4Signer


class TestAwsCases(test.TestCase):

    def setUp(self):

        # these are mock keys from aws documetation
        access_key = "AKIAIOSFODNN7EXAMPLE"
        secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        service = "s3"
        region = "us-east-1"

        self.signer = SigV4Signer(
            aws_access_key=access_key,
            aws_secret_key=secret_key,
            service=service,
            region=region,
        )

    def test_get_object(self):

        expected = (
            "AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east"
            "-1/s3/aws4_request,SignedHeaders=host;range;x-amz-content-sha256;"
            "x-amz-date,Signature=f0e8bdb87c964420e857bd35b5d6ed310bd44f0170ab"
            "a48dd91039c6036bdb41"
        )

        result = self.signer._get_authorization_headers(
            {
                "host": "examplebucket.s3.amazonaws.com",
                "range": "bytes=0-9",
                "x-amz-content-sha256": (
                    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7"
                    "852b855"
                ),
                "x-amz-date": "20130524T000000Z"
            },
            "f0e8bdb87c964420e857bd35b5d6ed310bd44f0170aba48dd91039c6036bdb41"
        )["Authorization"]

        self.assertEqual(result, expected)

    def test_put_object(self):

        expected = (
            "AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east"
            "-1/s3/aws4_request,SignedHeaders=date;host;x-amz-content-sha256;x"
            "-amz-date;x-amz-storage-class,Signature=98ad721746da40c64f1a55b78"
            "f14c238d841ea1380cd77a1b5971af0ece108bd"
        )

        result = self.signer._get_authorization_headers(
            {
                "host": "examplebucket.s3.amazonaws.com",
                "x-amz-content-sha256": (
                    "44ce7dd67c959e0d3524ffac1771dfbba87d2b6b4b4e99e42034a8b80"
                    "3f8b072"
                ),
                "x-amz-date": "20130524T000000Z",
                "x-amz-storage-class": "REDUCED_REDUNDANCY",
                "date": "Fri, 24 May 2013 00:00:00 GMT",
            },
            "98ad721746da40c64f1a55b78f14c238d841ea1380cd77a1b5971af0ece108bd"
        )["Authorization"]

        self.assertEqual(result, expected)

    def test_get_bucket_lifecycle(self):

        expected = (
            "AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east"
            "-1/s3/aws4_request,SignedHeaders=host;x-amz-content-sha256;x-amz-"
            "date,Signature=fea454ca298b7da1c68078a5d1bdbfbbe0d65c699e0f91ac7a"
            "200a0136783543"
        )

        result = self.signer._get_authorization_headers(
            {
                "host": "examplebucket.s3.amazonaws.com",
                "x-amz-content-sha256": (
                    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7"
                    "852b855"
                ),
                "x-amz-date": "20130524T000000Z",
            },
            "fea454ca298b7da1c68078a5d1bdbfbbe0d65c699e0f91ac7a200a0136783543"
        )["Authorization"]

        self.assertEqual(result, expected)

    def test_get_bucket(self):

        expected = (
            "AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east"
            "-1/s3/aws4_request,SignedHeaders=host;x-amz-content-sha256;x-amz-"
            "date,Signature=34b48302e7b5fa45bde8084f4b7868a86f0a534bc59db6670e"
            "d5711ef69dc6f7"
        )

        result = self.signer._get_authorization_headers(
            {
                "host": "examplebucket.s3.amazonaws.com",
                "x-amz-content-sha256": (
                    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7"
                    "852b855"
                ),
                "x-amz-date": "20130524T000000Z",
            },
            "34b48302e7b5fa45bde8084f4b7868a86f0a534bc59db6670ed5711ef69dc6f7"
        )["Authorization"]

        self.assertEqual(result, expected)


class TestInvalidInput(test.TestCase):

    def setUp(self):

        # these are mock keys from aws documetation
        access_key = "AKIAIOSFODNN7EXAMPLE"
        secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        service = "s3"
        region = "us-east-1"

        self.signer = SigV4Signer(
            aws_access_key=access_key,
            aws_secret_key=secret_key,
            service=service,
            region=region,
        )

    def test_none_dictionary_header_raises_error(self):

        with self.assertRaises(AttributeError):
            self.signer._get_authorization_headers("test", "test")

    def test_none_string_signature_raises_error(self):

        with self.assertRaises(TypeError):
            self.signer._get_authorization_headers({}, b"test")
