## create a key
```
aws kms list-aliases --quer 'Aliases[*].[AliasName,TargetKeyId]' --output table
```


keyid=$(aws kms create-key --region=us-east-1 --query 'KeyMetadata.Arn' --output text)
