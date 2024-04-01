## vpc endpoint
## 查看现有的
https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html
```
aws ec2 describe-vpc-endpoints --region=$region --quer 'VpcEndpoints[*].[ServiceName,VpcEndpointType,SubnetIds[0],SubnetIds[1]]' --output table
```
```
aws ec2 describe-vpc-endpoints --region=$region --quer 'VpcEndpoints[*].Groups[*].GroupId' --output table

```
## Delete VPC
```
aws ec2 delete-vpc --vpc-id $vpcid --region=$region 

```

https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html

# 等级保护
## 安全通信网络

###  check VPC
```
aws ec2 describe-vpcs --quer 'Vpcs[*].VpcId' --output table

```
### Check subnets
```
aws ec2 describe-subnets --query 'Subnets[*].[Tags[0].Value,SubnetId,VpcId]' --output table
```

## 安全区域边界
```

aws ec2 describe-nat-gateways --quer 'NatGateways[*].[NatGatewayId,SubnetId,VpcId]' --output table
```
```

aws ec2 describe-network-acls --query 'NetworkAcls[*].Entries' --output table
```
```
aws cloudtrail describe-trails --quer 'trailList[*].[Name,S3BucketName,LogFileValidationEnabled]' --output table
```
# -------------------------
## create a default VPC
```
vpcid=$(aws ec2 create-default-vpc --query 'Vpc.VpcId' --output text)  
```
## delete the default VPC
### get VPCID
```
vpcid=$(aws ec2 describe-vpcs --filters "Name=isDefault,Values=true" --quer 'Vpcs[*].VpcId' --output text)
```
二选一
```
vpcid=$(aws ec2 describe-vpcs --quer 'Vpcs[?IsDefault!=`true`].VpcId' --output text)
```
### get subnets
```
subnets=($(aws ec2 describe-subnets --filters "Name=default-for-az,Values=true"  --quer 'Subnets[*].SubnetId' --output text))
len=${#subnets[*]}
echo $len
```
## delete all subnets
```
for ((i=1; i<=len; i++));do
aws ec2 delete-subnet --subnet-id $subnets[i] --region=$region
done
```
## delete IGW
```
igw=$(aws ec2 describe-internet-gateways --region=$region --filters "Name=attachment.vpc-id,Values=$vpcid" --quer 'InternetGateways[].InternetGatewayId' --output text)
aws ec2 detach-internet-gateway --internet-gateway-id $igw --vpc-id $vpcid --region=$region
aws ec2 delete-internet-gateway --internet-gateway-id $igw --region=$region
```
### delete the empty VPC
```
aws ec2 delete-vpc --vpc-id $vpcid
```
### full script
```
vpcid=$(aws ec2 describe-vpcs --filters "Name=isDefault,Values=true" --quer 'Vpcs[*].VpcId' --output text)
subnets=($(aws ec2 describe-subnets --filters "Name=default-for-az,Values=true"  --quer 'Subnets[*].SubnetId' --output text))
len=${#subnets[*]}
echo $len
for ((i=1; i<=len; i++));do
aws ec2 delete-subnet --subnet-id $subnets[i] --region=$region
done
igw=$(aws ec2 describe-internet-gateways --region=$region --filters "Name=attachment.vpc-id,Values=$vpcid" --quer 'InternetGateways[].InternetGatewayId' --output text)
aws ec2 detach-internet-gateway --internet-gateway-id $igw --vpc-id $vpcid --region=$region
aws ec2 delete-internet-gateway --internet-gateway-id $igw --region=$region
aws ec2 delete-vpc --vpc-id $vpcid
```


## [create a VPC]([url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html))
tag打不上，有问题，sample少了个S,没有加上引号。
```
vpcid=$(aws ec2 create-vpc \
    --cidr-block 10.0.0.0/16 \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=awsthreetierworkshop}]'\
    --query 'Vpc.VpcId' --output text)  
```
可以补充tag
```
value=myvpc
aws ec2 create-tags --resources $vpcid --tags Key=Name,Value=$value
```
## create subnets
```
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.1.0/28 --availability-zone=cn-northwest-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Web-1}]' --no-cli-pager
```
