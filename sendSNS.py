import boto3

# Create an SNS client
sns_client = boto3.client('sns')

# Publish a message to the specified topic
topic_arn = 'arn:aws:sns:eu-central-1:274937635582:alert-bad-lambda'
message = 'Hello, world!'
response = sns_client.publish(
    TopicArn=topic_arn,
    Message=message
)

# Print the message ID returned by SNS
print(response['MessageId'])
