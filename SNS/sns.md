
## parameter
```
email=36256586@qq.com
region=us-east-1
rulename=snstopic2022
keyid='arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias'
```
## create and sub to email
```
snsarn=$(aws sns create-topic   --name  $rulename  --region=$region  --attributes  --output text --query 'TopicArn')
aws sns subscribe --topic-arn $snsarn --protocol email --notification-endpoint  $email --region=$region
```
## 加密
```
aws sns set-topic-attributes --topic-arn $nsarn --attribute-name KmsMasterKeyId --attribute-value $keyid
```
## list all sns topics
```
aws sns  list-topics
```
