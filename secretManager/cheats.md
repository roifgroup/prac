### Create:
aws secretsmanager create-secret --name <secret-name> --secret-string "<secret-value>"

### Delete: 
aws secretsmanager delete-secret --secret-id <secret-id>

### Update: 
aws secretsmanager update-secret --secret-id <secret-id> --secret-string "<new-secret-value>"


