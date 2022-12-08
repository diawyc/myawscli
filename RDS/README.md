# RDS 非常贵，记得要删除

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
aws rds describe-db-instances --region=$region --no-cli-pager  --query 'DBInstances[].DBInstanceIdentifier' --output text 
done
```
## 查看一个region的DB是否有删除保护
```
aws rds describe-db-instances --region=$region --no-cli-pager  --query 'DBInstances[].[DBInstanceIdentifier,DeletionProtection]' --output text
```
### 没有删除保护的找出来
```
aws rds describe-db-instances --region=$region --no-cli-pager  --query 'DBInstances[?DeletionProtection ==`false`].DBInstanceIdentifier' --output text
```
## 删除RDS
```
dbid=wd1c6y0bblbqv19
```
```
for region in $regions; do
echo $region
aws rds   delete-db-instance \
--db-instance-identifier $dbid \
SkipFinalSnapshot \
--region=$region --no-cli-pager
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
