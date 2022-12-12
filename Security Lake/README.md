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

## delegated admin
```
aws securitylake  create-datalake-delegated-admin --region=$region
```

### create iam role for glue and lambda
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

### create iam role for roll up region
```
rolename=SecurityLakeRegion
trustfile=trustpolicy.json
rolepolicyfile=regionpolicy.json
rolepolicy=SecurityLakeregionpolicy
```
```
regionrolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://$trustfile --query 'Role.Arn' --output text)
echo $regionrolearn
aws iam put-role-policy --role-name=$rolename --policy-name $rolepolicy --policy-document file://$rolepolicyfile
```
### get role arn from role name
```
rolearn=$(aws iam get-role --role-name $rolename --query 'Role.Arn' --output text)
```
arn:aws:iam::accountid:role/AmazonSecurityLakeMetaStoreManager


## [create datalake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-datalake.html)
```
aws securitylake create-datalake --regions $regions[1] $regions[2] \
--meta-store-manager-role-arn $rolearn \
--region=$region
```

```
aws securitylake create-datalake --regions $regions[1] $regions[2] \
--meta-store-manager-role-arn $rolearn --region=$region \
--configurations '{"us-east-1":{"replicationDestinationRegions":["eu-west-1"],"replicationRoleArn":"arn:aws:iam::230032173446:role/SecurityLakeRegion"},"eu-west-1":{"replicationDestinationRegions":[]}'
```

    
## [2个regions开启所有](https://docs.aws.amazon.com/ja_jp/cli/latest/reference/securitylake/create-aws-log-source.html)
```
aws securitylake create-aws-log-source \
 --input-order REGION \
 --enable-single-dimension $regions[1] $regions[2] \
 --region=$region
```
## [set rollup region](https://docs.aws.amazon.com/ja_jp/cli/latest/reference/securitylake/create-aws-log-source.html)
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
