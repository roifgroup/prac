import boto3
import json

# Create a Secrets Manager client
secretsmanager_client = boto3.client('secretsmanager')

# Get the secret value
get_secret_value_response = secretsmanager_client.get_secret_value(
    SecretId='testvalue'
)

# Parse and print the secret value
if 'SecretString' in get_secret_value_response:
    secret_value = json.loads(get_secret_value_response['SecretString'])
else:
    secret_value = json.loads(get_secret_value_response['SecretBinary'])

print(secret_value)


