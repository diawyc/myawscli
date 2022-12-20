# [I love aws cli](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws)

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
