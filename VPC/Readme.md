https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html

## create a defaul VPC
```
vpcid=$(aws ec2 create-default-vpc --query 'Vpc.Vpcid' --output text)  
```
## [create a VPC]([url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html))
tag打不上，有问题，sample少了个S,没有加上引号。
```
vpcid=$(aws ec2 create-vpc \
    --cidr-block 10.0.0.0/16 \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=awsthreetierworkshop}]' --query 'Vpc.Vpcid' --output text)  
```
可以补充tag
```
value=myvpc
aws ec2 create-tags --resources $vpcid --tags Key=Name,Value=$value
```
