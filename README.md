# I love aws cli

## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
for region in $regions; do
echo $region

done
### 不换页
```
--no-cli-pager
```
### query
```
--query 'level1[0].level2[*].level3' --output text
```

## sns
```
region=eu-west-2
arn='arn:aws:sns:eu-west-2:883600840440:SecurityHubAnnouncements'
```

```
aws  sns --region $region subscribe --topic-arn $arn --protocol email --notification-endpoint 36256586@qq.com
```
## get Organizations ID
```
orgid=$(aws organizations describe-organization  --query 'Organization.Id' --output text --region=$region)
echo $orgid
```
## Get all OU Ids
```
orgunits=($(aws organizations list-organizational-units-for-parent --parent-id $(aws organizations list-roots --query "Roots[].Id" --output text)  --query "OrganizationalUnits[*].Id" --output text))
echo ${#orgunits[*]}
```
```
rootid=$(aws organizations list-roots --query "Roots[].Id" --output text)
```
## Get all admin account id and email
```
aws organizations list-delegated-administrators --region=$region 
```
