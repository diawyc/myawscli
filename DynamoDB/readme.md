## add new item

```
name=
region=cn-northwest-1

```
```
aws dynamodb describe-table --table-name $name
```

```
aws dynamodb put-item --table-name $name --item '{"PK": {"S": "001"}, "SK": {"S": "test"},"company_id": {"N": "200"}}'\
 --region $region

```
```
aws dynamodb delete-item --table-name $name --key '{"id": {"S": "001"}, "sk": {"S": "test"}}' --region $region

```

```
aws dynamodb put-item --table-name $name --item '{"id": {"S": "001"}}'\
 --region $region

```
```
aws dynamodb delete-item --table-name $name --key '{"id": {"S": "001"}}' --region $region

```
