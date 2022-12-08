# I love aws cli

## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
### 不换页
```
--no-cli-pager
```
## 查看所有region的DB
```
for region in $regions; do
echo $region
aws rds describe-db-instances --region=$region --no-cli-pager
done
```
## 复制出境
### 参数设置
```
region=ap-northeast-1
db=paris2tokyo
source=arn:aws:rds:eu-west-3:980217471394:db:testforcrossregion
```
### command
```
aws rds create-db-instance-read-replica \
    --db-instance-identifier $db \
    --source-db-instance-identifier $source --region=$region
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
