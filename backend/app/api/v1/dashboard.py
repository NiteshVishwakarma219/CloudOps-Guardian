from fastapi import APIRouter
from app.services.aws_client import ec2_client, s3_client

router = APIRouter()

@router.get("/dashboard")
def dashboard():

    try:

        instances = ec2_client.describe_instances()

        ec2_count = sum(
            len(r["Instances"])
            for r in instances["Reservations"]
        )

        buckets = s3_client.list_buckets()

        s3_count = len(buckets["Buckets"])

        vpcs = ec2_client.describe_vpcs()

        security_groups = ec2_client.describe_security_groups()

        volumes = ec2_client.describe_volumes()

        snapshots = ec2_client.describe_snapshots(
        OwnerIds=["self"]
        )

        elastic_ips = ec2_client.describe_addresses()

        return {

            "EC2": ec2_count,

            "S3": s3_count ,

            "VPC": len(vpcs["Vpcs"]),

            "SecurityGroups": len(
            security_groups["SecurityGroups"]
            ),

            "Volumes": len(volumes["Volumes"]),

            "Snapshots": len(
             snapshots["Snapshots"]
            ),

            "ElasticIPs": len(
             elastic_ips["Addresses"]
             )

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }