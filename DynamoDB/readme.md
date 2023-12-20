
# batch import data from a file
```
aws dynamodb batch-write-item --request-items file://$filename

```

## check the table status

```
name=result_update
region=cn-northwest-1

```
```
aws dynamodb describe-table --table-name $name --no-cli-pager
streamarn=$(aws dynamodb describe-table --table-name $name --no-cli-pager --query 'Table.LatestStreamArn' --output text)
```
# 进口车正确
```
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "001"}, "vin": {"S": "JH1TG687785000035"},"date_created_epoch": {"N": "1698056260"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "001"}}'\
 --region $region
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "008"}, "vin": {"S": "JHFGR987795000035"},"date_created_epoch": {"N": "1698056260"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "008"}}'\
 --region $region
```
# 进口车错误数据

```
 --region $region
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "009"}, "vin": {"S": "JH2TG687785000035"},"date_created_epoch": {"N": "1698056260"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "009"}}'\
 --region $region

```

# 国产车正确
```
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "002"}, "vin": {"S": "LVHTG6877H5000035"},"date_created_epoch": {"N": "1698056060"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "002"}}'\
 --region $region

aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "003"}, "vin": {"S": "LHGGE6877H5000035"},"date_created_epoch": {"N": "1698056160"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "003"}}'\
 --region $region

```
# 国产车错误

```
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "004"}, "vin": {"S": "LVKTG6877H5000035"},"date_created_epoch": {"N": "1698056060"}}'\
 --region $region
aws dynamodb  delete-item --table-name $name --key '{"log_id": {"S": "004"}}'\
 --region $region

```
```
aws dynamodb put-item --table-name $name --item '{"log_id": {"S": "004"}, "vin": {"S": "LVKTG6877H5000035"},"date_created_epoch": {"N": "1698056060"}}',"json": {"S": "{\"campaignId\": \"HT011CMPHAT11001\", \"VIN\": \"HTC011VCLHAT00001\", \"updateSw\": [{\"serialNumber\": \"SERIAL_NUMBER_FI02001\", \"protocol\": \"Ether\", \"diagProtocol\": null, \"softwarePartNumber\": \"HT011-ES02-FJ02\", \"compatibleSoftwarePartNumber\": \"HT011-ES02-FJ01\", \"targetSoftwarePartNumber\": \"HT011-ES02-FJ02\", \"datetimeUpdateStart\": \"20200701T000041Z\", \"datetimeUpdateFinish\": \"20200701T000141Z\", \"datetimeActivate\": \"20200701T000241Z\", \"codeResult\": 2, \"codeError\": [\"HT001ERR01\"], \"dtc\": null}], \"typeUpdate\": 1, \"typeNetwork\": 1, \"ipAddress\": \"103.114.101.225\", \"trigger\": 2, \"typeActivation\": 2, \"sourceActivation\": 1, \"versionUpdateClient\": \"1.0.0\", \"versionOsClient\": \"1.0.0\", \"datetimeCreated\": \"20231031T063819Z\", \"apiVersion\": \"1.0\", \"vciName\": null, \"repairOrderNum\": null, \"dealerNumber\": null, \"isoCountryCode\": null, \"computerIdentificationInformation\": null, \"oddDetection\": null, \"dstiSerialNumber\": null}"}\
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
