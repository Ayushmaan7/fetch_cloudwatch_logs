
# CloudWatch Logs Access with Boto3

This repository contains a Python script that demonstrates how to access logs from AWS CloudWatch using the Boto3 library.

## Prerequisites

1. **AWS Account**: Ensure you have an AWS account.
2. **AWS CLI**: Install and configure the AWS CLI with your credentials.
   ```bash
   aws configure
   ```
3. **Python**: Install Python 3.x on your machine.
4. **Boto3**: Install the Boto3 library via pip.
   ```bash
   pip install boto3
   ```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cloudwatch-logs-access.git
   cd cloudwatch-logs-access
   ```

2. **Edit the script**:
   - Open `fetch_cloudwatch_logs.py` and replace:
     - `'your-log-group-name'` with your actual CloudWatch log group name.
     - `'your-log-stream-name'` with your actual CloudWatch log stream name.

3. **Run the script**:
   ```bash
   python fetch_cloudwatch_logs.py
   ```

## Explanation of the Script

- **Initialization**: A Boto3 client for CloudWatch Logs is created.
- **Log Group and Stream**: The script specifies the log group and log stream names from which to fetch logs.
- **Time Range**: The script retrieves logs for the last hour (modifiable in the script).
- **Fetch Logs**: The `filter_log_events` method is used to retrieve logs, which are printed to the console.

## Additional Notes

- Ensure that the IAM role or user you are using has the necessary permissions to access CloudWatch Logs.
- Adjust the time range and log group/stream names as per your requirements.
