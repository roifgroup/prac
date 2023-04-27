import boto3
import json

def lambda_handler(event, context):
    # Create a Secrets Manager client
    secretsmanager_client = boto3.client('secretsmanager')

    # Get the secret value
    get_secret_value_response = secretsmanager_client.get_secret_value(
        SecretId='<your-secret-name>'
    )

    # Parse and return the secret value
    if 'SecretString' in get_secret_value_response:
        secret_value = json.loads(get_secret_value_response['SecretString'])
    else:
        secret_value = json.loads(get_secret_value_response['SecretBinary'])

    return secret_value

