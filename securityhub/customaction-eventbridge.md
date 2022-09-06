# Securityhub
From this blog, I change the manual work part into below CLI command. Easier to copy
https://aws.amazon.com/blogs/mt/automate-vulnerability-management-and-remediation-in-aws-using-amazon-inspector-and-aws-systems-manager-part-1/

## create custom action
-----------------------------------------------------------------------
## 参数设置
region为securityhub指定的聚合aggregated region
```
region='eu-west-2'
buttonnames=('Rem-Inspector-NoRBT' 'Rem-Inspector-RBT')
actionids=('InspectorRemNoRBT' 'InspectorRemRBT')

```

```
rulename=''
email='**@**.com'

```
## CLI 命令复制粘贴
```
for ((i=1; i<=${#buttonnames[@]}; i++));do
arn=$(aws securityhub create-action-target \
    --name $buttonnames[$i]\
    --description $buttonnames[$i] \
    --id $actionids[$i] --region=$region  --output text --query 'ActionTargetArn')
echo $arn
done
```

```
snsarn=$(aws sns create-topic   --name  $rulename  --region=$region  --output text --query 'TopicArn')
aws sns subscribe --topic-arn $snsarn --protocol email --notification-endpoint  $email --region=$region
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
