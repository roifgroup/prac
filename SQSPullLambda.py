import json
import boto3

def lambda_handler(event, context):
    # Create an SQS client
    sqs = boto3.client('sqs')

    # Get the URL for the queue
    queue_url = sqs.get_queue_url(QueueName='test')['QueueUrl']

    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10, # Set the maximum number of messages to receive
        WaitTimeSeconds=5 # Wait for up to 5 seconds for messages to become available
    )

    # Process the messages
    for message in response.get('Messages', []):
        # Print the message body
        print(message['Body'])

        # Delete the message from the queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed.')
    }
