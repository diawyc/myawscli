## add new item

```
name=
region=cn-northwest-1

```

```
aws dynamodb put-item --table-name $name --item '{"PK": {"S": "COMPANY#1001"}, "SK": {"S": "PRODUCT#CHOCOLATE#DARK"},"company_id": {"N": "1000"}}'\
 --region $region

```
```
aws dynamodb delete-item --table-name $name --key '{"PK": {"S": "COMPANY#1001"}, "SK": {"S": "PRODUCT#CHOCOLATE#DARK"}}' --region $region

```
