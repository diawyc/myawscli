## add new item

```
name=
region=cn-northwest-1

```

```
aws dynamodb put-item --table-name $name --item '{"PK": {"S": "001"}, "SK": {"S": "test"},"company_id": {"N": "200"}}'\
 --region $region

```
```
aws dynamodb delete-item --table-name $name --key '{"PK": {"S": "001"}, "SK": {"S": "test"}}' --region $region

```

```
aws dynamodb put-item --table-name $name --item '{"id": {"S": "001"}}'\
 --region $region

```
```
aws dynamodb delete-item --table-name $name --key '{"id": {"S": "001"}}' --region $region

```
