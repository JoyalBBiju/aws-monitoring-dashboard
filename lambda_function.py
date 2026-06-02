import boto3
import json
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    """
    Lambda function to retrieve EC2 CPUUtilization metrics from CloudWatch.
    Returns average CPU utilization for the last 5 minutes.
    """
    try:
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(minutes=5)

        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Average', 'Maximum', 'Minimum'],
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': event.get('instance_id', 'i-0123456789abcdef0')
                }
            ]
        )

        datapoints = response.get('Datapoints', [])

        if datapoints:
            latest_datapoint = sorted(datapoints, key=lambda x: x['Timestamp'], reverse=True)[0]
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'timestamp': latest_datapoint['Timestamp'].isoformat(),
                    'cpu_utilization': {
                        'average': round(latest_datapoint.get('Average', 0), 2),
                        'maximum': round(latest_datapoint.get('Maximum', 0), 2),
                        'minimum': round(latest_datapoint.get('Minimum', 0), 2)
                    },
                    'metric_period_minutes': 5,
                    'message': 'EC2 CPU metrics retrieved successfully'
                })
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'timestamp': end_time.isoformat(),
                    'cpu_utilization': None,
                    'metric_period_minutes': 5,
                    'message': 'No data points available for the specified time period'
                })
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Failed to retrieve EC2 metrics from CloudWatch'
            })
        }
