import boto3

from app.core.config import settings

session = boto3.Session(

    region_name=settings.AWS_REGION

)

ec2_client = session.client("ec2")

s3_client = session.client("s3")

iam_client = session.client("iam")

cloudtrail_client = session.client("cloudtrail")

sts_client = session.client("sts")