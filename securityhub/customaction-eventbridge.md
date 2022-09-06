# Securityhub
## create custom action
-----------------------------------------------------------------------
## 参数设置
region为securityhub指定的聚合aggregated region
```
region='eu-west-'
buttonname='Rem-Inspector-NoRBT'
actionid='send2email'
rulename='InspectorRemNoRBT'
email='**@**.com'

```
## CLI 命令复制粘贴
```
snsarn=$(aws sns create-topic   --name  $rulename  --region=$region  --output text --query 'TopicArn')
aws sns subscribe --topic-arn $snsarn --protocol email --notification-endpoint  $email --region=$region
buttonarn=$(aws securityhub create-action-target \
    --name $buttonname\
    --description $rulename \
    --id $actionid --region=$region  --output text --query 'ActionTargetArn')
aws events put-rule \
--name $rulename \
--event-pattern "{\"source\":[\"aws.securityhub\"], \
\"detail-type\": [\"Security Hub Findings - Custom Action\"], \
  \"resources\": [\"$buttonarn\"]}"  --region=$region
aws events put-targets --rule $rulename  --targets "Id"="1","Arn"=$snsarn --region=$region
```


## 打开eventbridge rule,复制以下内容至Target-Input transformer-config input transformer
### Input path
```
{
  "title": "$.detail.findings[0].Title",
  "Description": "$.detail.findings[0].Description",
  "account":"$.account",
  "region":"$.region"
  
}
```
### Template

```
"安全团队, there is an alert title : <title> in region:<region>"
"in account number:<account>"
"内容为:<Description>"
"请处理,谢谢!"
```
