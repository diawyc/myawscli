# RDS 非常贵，记得要删除

```
show variables like '%have_ssl%';
show variables like '%max_connect_errors%';
```
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
## 查看所有region没有deletion protection的DB instance
```
for region in $regions; do
echo $region
aws rds describe-db-instances --region=$region --no-cli-pager  --query 'DBInstances[?DeletionProtection ==`false`].DBInstanceIdentifier' --output text
done
```
## 删除一个region的所有RDS
```
dbids=($(aws rds describe-db-instances --region=$region --no-cli-pager  --query 'DBInstances[].DBInstanceIdentifier' --output text))
len=${#dbids[*]}
echo $len
```
```
for ((i=1; i<=len; i++));do
dbid=$dbids[i]
aws rds delete-db-instance \
--db-instance-identifier $dbid \
--skip-final-snapshot --delete-automated-backups \
--region=$region --no-cli-pager
done
```
## 删除all region的所有RDS
```
for region in $regions; do
echo $region
dbids=($(aws rds describe-db-instances --region=$region --no-cli-pager  --query 'DBInstances[].DBInstanceIdentifier' --output text))
len=${#dbids[*]}
echo $len
for ((i=1; i<=len; i++));do
dbid=$dbids[i]
aws rds modify-db-instance \
--db-instance-identifier $dbid  \
--no-deletion-protection \
--apply-immediately \
--region=$region --no-cli-pager

aws rds delete-db-instance \
--db-instance-identifier $dbid \
--skip-final-snapshot --delete-automated-backups \
--region=$region --no-cli-pager
done
done
```

## [去掉删除保护](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html)
```
aws rds modify-db-instance \
--db-instance-identifier $dbid  \
--no-deletion-protection \
--apply-immediately \
--region=$region
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
