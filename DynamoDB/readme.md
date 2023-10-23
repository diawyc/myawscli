## add new item

```
name=result_update
region=cn-northwest-1

```
```
aws dynamodb describe-table --table-name $name --no-cli-pager
```
# 进口车正确，错误数据
```
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "001"}, "vin": {"S": "JH1TG687785000035"},"date_created_epoch": {"N": "1698056260"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "001"}}'\
 --region $region
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "009"}, "vin": {"S": "JH2TG687785000035"},"date_created_epoch": {"N": "1698056260"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "009"}}'\
 --region $region
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "008"}, "vin": {"S": "JHFGR987795000035"},"date_created_epoch": {"N": "1698056260"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "008"}}'\
 --region $region
```
#JV车，正确，错误
```
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "002"}, "vin": {"S": "LVHTG6877H5000035"},"date_created_epoch": {"N": "1698056060"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "002"}}'\
 --region $region
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "004"}, "vin": {"S": "LVKTG6877H5000035"},"date_created_epoch": {"N": "1698056060"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "004"}}'\
 --region $region
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "003"}, "vin": {"S": "LHGGE6877H5000035"},"date_created_epoch": {"N": "1698056160"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "003"}}'\
 --region $region

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
