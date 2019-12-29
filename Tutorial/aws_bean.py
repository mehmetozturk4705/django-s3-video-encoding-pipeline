import boto3
from botocore.client import Config
from django.conf import settings


class S3Client:
    __instance__ = None
    @staticmethod
    def getInstance():
        if not S3Client.__instance__:
            S3Client.__instance__=boto3.client('s3', region_name=settings.AWS_REGION, aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                  config=Config(s3={'addressing_style': 'path'},
                                signature_version='s3v4'))
        return S3Client.__instance__