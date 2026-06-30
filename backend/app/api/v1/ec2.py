from fastapi import APIRouter
from app.services.aws_client import ec2_client

router = APIRouter()

@router.get("/ec2")
def get_ec2_instances():

    try:

        response = ec2_client.describe_instances()

        instances = []

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                instances.append({

                    "InstanceId": instance["InstanceId"],

                    "State": instance["State"]["Name"],

                    "InstanceType": instance["InstanceType"],

                    "PublicIP": instance.get("PublicIpAddress", "N/A"),

                    "PrivateIP": instance.get("PrivateIpAddress", "N/A")

                })

        return {

            "count": len(instances),

            "instances": instances

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }
    
router = APIRouter(

    prefix="/api/v1",

    tags=["EC2"]

)