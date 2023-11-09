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

# -------------------------
## create a defaul VPC
```
vpcid=$(aws ec2 create-default-vpc --query 'Vpc.Vpcid' --output text)  
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
