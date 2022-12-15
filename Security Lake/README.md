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

## [delegated admin] (https://docs.aws.amazon.com/ja_jp/cli/latest/reference/securitylake/create-datalake-delegated-admin.html)
```
admin=295158943844
```
```
aws securitylake  create-datalake-delegated-admin --account $admin --region=$region
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
--configurations '{"us-east-2":{"replicationDestinationRegions":["eu-west-1"],"replicationRoleArn":"arn:aws:iam::230032173446:role/SecurityLakeRegion"},"eu-west-1":{"replicationDestinationRegions":[]}}'
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
## 删除遗留的S3
```
aws s3api list-buckets --query 'Buckets[?Name<`aws-security-data-lake-z`].Name' --output table
bucketnames=($(aws s3api list-buckets --query 'Buckets[?Name<`aws-security-data-lake-z`].Name' --output text))
len=${#bucketnames[*]}
```

```
for ((i=1; i<=len; i++));do
bucketname=$bucketnames[i]
echo $bucketname
aws s3api delete-objects  --bucket $bucketname --delete "$(aws s3api list-object-versions --bucket $bucketname --output=json --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
aws s3 rb s3://$bucketnames[i] --force 
done
```

## 删除遗留的SQS
## 查看所有的securitylake开头的SQS

```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
```
目前开放的6个regions

```
regions=(eu-west-1 ap-northeast-1 ap-southeast-2 eu-central-1 us-east-2 us-west-2)
for region in $regions; do
echo $region
aws sqs list-queues --queue-name-prefix SecurityLake  --region=$region --query 'QueueUrls' --output table
done
```
### 删除查看到的
```
for region in $regions; do
echo $region
urls=($(aws sqs list-queues --queue-name-prefix SecurityLake  --region=$region --query 'QueueUrls' --output text))
len=${#urls[*]}
for ((i=1; i<=len; i++));do
echo $urls[i]
aws sqs delete-queue --queue-url $urls[i] --region=$region
done
done
```
