from app.services.aws_client import (
    ec2_client,
    s3_client,
    iam_client,
    cloudtrail_client
)


def security_scan():

    issues = []
    security_score = 100

    # ==========================================
    # Check 1: Security Groups Open to Internet
    # ==========================================

    try:
        groups = ec2_client.describe_security_groups()

        for sg in groups["SecurityGroups"]:

            for permission in sg["IpPermissions"]:

                for ip in permission.get("IpRanges", []):

                    if ip.get("CidrIp") == "0.0.0.0/0":

                        issues.append({

                            "resource": sg["GroupId"],

                            "name": sg.get("GroupName"),

                            "type": "Security Group",

                            "issue": "Inbound rule open to the Internet (0.0.0.0/0)",

                            "severity": "High"

                        })

                        security_score -= 10

    except Exception as e:

        issues.append({

            "resource": "Security Groups",

            "type": "Scanner",

            "issue": str(e),

            "severity": "Info"

        })

    # ==========================================
    # Check 2: Public S3 Buckets
    # ==========================================

    try:

        buckets = s3_client.list_buckets()

        for bucket in buckets["Buckets"]:

            bucket_name = bucket["Name"]

            try:

                status = s3_client.get_bucket_policy_status(
                    Bucket=bucket_name
                )

                if status["PolicyStatus"]["IsPublic"]:

                    issues.append({

                        "resource": bucket_name,

                        "type": "S3",

                        "issue": "Public Bucket",

                        "severity": "Critical"

                    })

                    security_score -= 15

            except Exception:
                pass

    except Exception as e:

        issues.append({

            "resource": "S3",

            "type": "Scanner",

            "issue": str(e),

            "severity": "Info"

        })

    # ==========================================
    # Check 3: IAM Users Without MFA
    # ==========================================

    try:

        users = iam_client.list_users()

        for user in users["Users"]:

            username = user["UserName"]

            devices = iam_client.list_mfa_devices(
                UserName=username
            )

            if len(devices["MFADevices"]) == 0:

                issues.append({

                    "resource": username,

                    "type": "IAM",

                    "issue": "MFA Not Enabled",

                    "severity": "Medium"

                })

                security_score -= 5

    except Exception as e:

        issues.append({

            "resource": "IAM",

            "type": "Scanner",

            "issue": str(e),

            "severity": "Info"

        })

    # ==========================================
    # Check 4: CloudTrail Enabled
    # ==========================================

    try:

        trails = cloudtrail_client.describe_trails()

        if len(trails["trailList"]) == 0:

            issues.append({

                "resource": "CloudTrail",

                "type": "Logging",

                "issue": "CloudTrail is Disabled",

                "severity": "Critical"

            })

            security_score -= 20

    except Exception as e:

        issues.append({

            "resource": "CloudTrail",

            "type": "Scanner",

            "issue": str(e),

            "severity": "Info"

        })

    # ==========================================
    # Prevent Negative Score
    # ==========================================

    if security_score < 0:
        security_score = 0

    return {

        "SecurityScore": security_score,

        "TotalIssues": len(issues),

        "Issues": issues

    }