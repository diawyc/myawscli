# Sechub
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
## get delegated admin account ID
```
adminid=$(aws securityhub list-organization-admin-accounts --region=$region --output text --query 'AdminAccounts[*].AccountId') 

```
## 查看所有region的standards情况
```
for region in $regions; do
echo $region
aws securityhub get-enabled-standards --query 'StandardsSubscriptions[*].StandardsSubscriptionArn' --output table --region=$region
done
```
## 打开SecurityHub
```
for region in $regions; do
echo $region
AWS securityhub enable-organization-admin-account --admin-account-id=$adminid --region=$region 
echo $(aws securityhub list-organization-admin-accounts --region=$region --query 'AdminAccounts')
done
```
## [关闭standard in all regions](https://docs.aws.amazon.com/cli/latest/reference/securityhub/batch-disable-standards.html)
```

echo $len
```
standard arn look like :"arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"
```
for region in $regions; do
sarns=($(aws securityhub get-enabled-standards  --region=$region --query 'StandardsSubscriptions[*].StandardsSubscriptionArn' --output text)) 
len=${#sarns[*]}
for ((i=1; i<=len; i++));do

aws securityhub batch-disable-standards \
    --standards-subscription-arns $sarns[i] \
    --region=$region
done
done
```

