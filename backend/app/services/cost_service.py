from app.services.aws_client import ec2_client


def analyze_cost():

    recommendations = []
    total_savings = 0

    # --------------------------
    # Check Stopped EC2 Instances
    # --------------------------
    response = ec2_client.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            if instance["State"]["Name"] == "stopped":

                recommendations.append({
                    "resource": instance["InstanceId"],
                    "type": "EC2",
                    "issue": "Stopped EC2 instance",
                    "recommendation": "Terminate if unused",
                    "estimatedSavings": 8
                })

                total_savings += 8

    # --------------------------
    # Check Unattached EBS Volumes
    # --------------------------
    volumes = ec2_client.describe_volumes()

    for volume in volumes["Volumes"]:

        if len(volume["Attachments"]) == 0:

            recommendations.append({
                "resource": volume["VolumeId"],
                "type": "EBS",
                "issue": "Unused Volume",
                "recommendation": "Delete unattached volume",
                "estimatedSavings": 5
            })

            total_savings += 5

    # --------------------------
    # Check Unused Elastic IPs
    # --------------------------
    addresses = ec2_client.describe_addresses()

    for address in addresses["Addresses"]:

        if "InstanceId" not in address:

            recommendations.append({
                "resource": address["AllocationId"],
                "type": "Elastic IP",
                "issue": "Unused Elastic IP",
                "recommendation": "Release Elastic IP",
                "estimatedSavings": 3
            })

            total_savings += 3

    # --------------------------
    # Check Snapshots
    # --------------------------
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=["self"]
    )

    for snapshot in snapshots["Snapshots"]:

        recommendations.append({
            "resource": snapshot["SnapshotId"],
            "type": "Snapshot",
            "issue": "Review Snapshot",
            "recommendation": "Delete if no longer required",
            "estimatedSavings": 1
        })

        total_savings += 1

    return {
        "totalEstimatedSavings": total_savings,
        "recommendations": recommendations
    }