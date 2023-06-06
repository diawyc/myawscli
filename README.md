# [I love aws cli](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws)

## 选profile

```
aws configure list-profiles
export AWS_PROFILE=cnrole
aws ec2 describe-regions
```

## use role instead of user
可以直接改文件或者使用


```
role='arn:aws-cn:iam::accountid:role/rolename'
profile=
sessionname=
region=
```

```
aws configure set role_arn $role
aws configure set source_profile $profile
aws configure set role_session_name $sessionname
aws configure set region $region
aws configure set output json

```

## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
```
for region in $regions; do
echo $region

done
```
## service quota
```
code=L-0DA4ABF3
region=cn-north-1
servicename=lambda
name='Managed policies per role'
```
```
aws service-quotas get-aws-default-service-quota \
    --service-code ec2 \
    --quota-code $code  --region=$region

```
### 查看一个service的所有quota code和数量
```
 aws service-quotas list-aws-default-service-quotas \
    --service-code $servicename --query  'Quotas[*].[QuotaName,QuotaCode,Value]' --output table --region=$region 
```

### 根据名字获得code

```
eval "aws service-quotas list-aws-default-service-quotas --service-code $servicename --query  'Quotas[?QuotaName==\`$name\`].QuotaCode' --output text --region=$region"
```
```
code=$(aws service-quotas list-aws-default-service-quotas --service-code $servicename --query 'Quotas[?QuotaName==`Managed policies per role`].QuotaCode' --output text --region=$region)

```
### 查看现在的quota
```
aws service-quotas get-service-quota \
    --service-code $servicename\
    --quota-code $code --region=$region --query  'Quota.[{name:QuotaName},{value:Value}]' --output table

```

## 遍历
```
len=${#names[*]}
echo $len
```
```
for ((i=1; i<=len; i++));do



done
```
### 不换页
```
--no-cli-pager
```
### query
```
--query 'level1[0].level2[*].level3' --output text
--query 'StackSummaries[?StackName!=`PVRE`].StackName' 
```
### 查看当前账户，账号
```
aws sts get-caller-identity
```

```
aws sts get-caller-identity --query 'Account' --output table
```
## sns
```
region=eu-west-2
arn='arn:aws:sns:eu-west-2:883600840440:SecurityHubAnnouncements'
```

```
aws  sns --region $region subscribe --topic-arn $arn --protocol email --notification-endpoint 36256586@qq.com
```


```
aws cloudtrail create-trail --name my-trail --s3-bucket-name my-bucket --is-multi-region-trail --tags-list [key=Group,value=Marketing]
```
