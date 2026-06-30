import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

ec2_client = boto3.client(
    "ec2",
    region_name=AWS_REGION
)