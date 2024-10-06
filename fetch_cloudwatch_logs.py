import boto3
import datetime

# Initialize a session using Amazon CloudWatch Logs
client = boto3.client('logs')

# Specify the log group and log stream
log_group_name = 'your-log-group-name'  # Replace with your log group name
log_stream_name = 'your-log-stream-name'  # Replace with your log stream name

# Set the time range for the logs you want to retrieve
start_time = int((datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp() * 1000)  # Last 1 hour
end_time = int(datetime.datetime.now().timestamp() * 1000)  # Current time

try:
    # Fetch logs from the specified log group and log stream
    response = client.filter_log_events(
        logGroupName=log_group_name,
        logStreamNames=[log_stream_name],
        startTime=start_time,
        endTime=end_time
    )

    # Print the retrieved log events
    for event in response['events']:
        print(f"Timestamp: {datetime.datetime.fromtimestamp(event['timestamp'] / 1000)}")
        print(f"Message: {event['message']}\n")

except Exception as e:
    print(f"Error fetching logs: {str(e)}")
