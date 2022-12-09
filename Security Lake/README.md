# I love aws cli

## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
```
regions=(eu-west-1 us-east-1)
region=us-east-1
```
### 不换页
```
--no-cli-pager
```

## [开启服务 ](https://docs.aws.amazon.com/ja_jp/cli/latest/reference/securitylake/create-datalake.html)

## 

### create iam role
```
rolename=AmazonSecurityLakeMetaStoreManager
trustfile=trustpolicy.json
rolepolicyfile=skpolicy.json
rolepolicy=SecurityLakeMetaStoreManagerpolicy
```
## [get role arn](https://docs.aws.amazon.com/security-lake/latest/userguide/manage-regions.html#iam-role-partitions)
```
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://$trustfile --query 'Role.Arn' --output text)
echo $rolearn
aws iam put-role-policy --role-name=$rolename --policy-name $rolepolicy --policy-document file://$rolepolicyfile
```
## create datalake
```
aws securitylake create-datalake --regions $regions[1] $regions[2] \
--meta-store-manager-role-arn $rolearn \
--region=$region
```
## [2个regions开启所有](https://docs.aws.amazon.com/ja_jp/cli/latest/reference/securitylake/create-aws-log-source.html)
```
aws securitylake create-aws-log-source \
 --input-order REGION \
 --enable-single-dimension $regions[1] $regions[2] \
 --region=$region
```
# 关闭服务

## Disable in all regions
```
aws securitylake  delete-datalake --region=$region
```
## 删除管理员
```
adminid=295158943844 
```

```
aws securitylake  delete-datalake-delegated-admin --account $adminid --region=$region
```
