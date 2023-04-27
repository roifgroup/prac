import boto3
import time

# Create an SQS client
sqs_client = boto3.client('sqs')

# Set the name of the queue you want to poll
queue_name = '<your-queue-name>'

# Get the URL of the queue
response = sqs_client.get_queue_url(QueueName=queue_name)
queue_url = response['QueueUrl']

# Poll the queue for messages
while True:
    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=20
    )

    # Check if any messages were received
    if 'Messages' in response:
        for message in response['Messages']:
            # Process the message
            print(message['Body'])

            # Delete the message from the queue
            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

    # Wait for some time before polling the queue again
    time.sleep(1)


