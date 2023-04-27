import boto3
import os
from urllib.parse import unquote

s3_client = boto3.client("s3")
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    S3_BUCKET = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = unquote(event["Records"][0]["s3"]["object"]["key"])
    
    file_content = s3_client.get_object(
        Bucket=S3_BUCKET, Key=object_key)["Body"].read()
    print(file_content.decode("utf-8")[0:10])
    sendsns(file_content.decode("utf-8")[0:10])

def sendsns(a):
    topic_arn = os.environ["snsarn"]
    message = a
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )

    # Print the message ID returned by SNS
    print(response['MessageId'])

