# Sechub
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
## get delegated admin account ID
```
adminid=$(aws securityhub list-organization-admin-accounts --region=$region --output text --query 'AdminAccounts[*].AccountId') 

```
## [关闭standard](https://docs.aws.amazon.com/cli/latest/reference/securityhub/batch-disable-standards.html)
```
sarn=$(aws securityhub get-enabled-standards --query 'StandardsSubscriptions[0].StandardsSubscriptionArn' --output text --region=$region)
arn="arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"
```
```
aws securityhub batch-disable-standards \
    --standards-subscription-arns $arn \
    --region=$region
```
```
for region in $regions; do
echo $region
aws securityhub get-enabled-standards --query 'StandardsSubscriptions[*].StandardsSubscriptionArn' --output text --region=$region
done
```
