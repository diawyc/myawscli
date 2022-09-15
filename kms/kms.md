## create a key
keyid=$(aws kms create-key --region=us-east-1 --query 'KeyMetadata.Arn' --output text)
