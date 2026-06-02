import boto3
import json
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

INSTANCE_ID = 'i-0a3ea0632822c4665'
IMAGE_ID = 'ami-0685bcc683dadb6b9'
INSTANCE_TYPE = 't3.micro'


def get_metric(namespace, metric_name, dimensions):

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=15)

    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average'],
        Dimensions=dimensions
    )

    datapoints = response.get('Datapoints', [])

    if datapoints:
        latest = sorted(
            datapoints,
            key=lambda x: x['Timestamp'],
            reverse=True
        )[0]

        return round(
            latest.get('Average', 0),
            2
        )

    return None


def lambda_handler(event, context):

    try:

        # CPU
        cpu = get_metric(
            'AWS/EC2',
            'CPUUtilization',
            [
                {
                    'Name': 'InstanceId',
                    'Value': INSTANCE_ID
                }
            ]
        )

        # Memory
        memory = get_metric(
            'CWAgent',
            'mem_used_percent',
            [
                {
                    'Name': 'ImageId',
                    'Value': IMAGE_ID
                },
                {
                    'Name': 'InstanceId',
                    'Value': INSTANCE_ID
                },
                {
                    'Name': 'InstanceType',
                    'Value': INSTANCE_TYPE
                }
            ]
        )

        # Disk
        disk = get_metric(
            'CWAgent',
            'disk_used_percent',
            [
                {
                    'Name': 'ImageId',
                    'Value': IMAGE_ID
                },
                {
                    'Name': 'InstanceId',
                    'Value': INSTANCE_ID
                },
                {
                    'Name': 'InstanceType',
                    'Value': INSTANCE_TYPE
                },
                {
                    'Name': 'device',
                    'Value': 'nvme0n1p1'
                },
                {
                    'Name': 'fstype',
                    'Value': 'xfs'
                },
                {
                    'Name': 'path',
                    'Value': '/'
                }
            ]
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'timestamp': datetime.utcnow().isoformat(),
                'cpu_utilization': {
                    'average': cpu
                },
                'memory_utilization': {
                    'average': memory
                },
                'disk_utilization': {
                    'average': disk
                },
                'message': 'Metrics retrieved successfully'
            })
        }

    except Exception as e:

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }