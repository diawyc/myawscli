# AWS Three Tier Web Architecture Workshop

## Architecture Overview
![Architecture Diagram](https://github.com/aws-samples/aws-three-tier-web-architecture-workshop/blob/main/application-code/web-tier/src/assets/3TierArch.png)

In this architecture, a public-facing Application Load Balancer forwards client traffic to our web tier EC2 instances. The web tier is running Nginx webservers that are configured to serve a React.js website and redirects our API calls to the application tier’s internal facing load balancer. The internal facing load balancer then forwards that traffic to the application tier, which is written in Node.js. The application tier manipulates data in an Aurora MySQL multi-AZ database and returns it to our web tier. Load balancing, health checks and autoscaling groups are created at each layer to maintain the availability of this architecture.

## Workshop Instructions:

See [AWS Three Tier Web Architecture](https://catalog.us-east-1.prod.workshops.aws/workshops/85cd2bb2-7f79-4e96-bdee-8078e469752a/en-US)

# CLI
## Part 0
### S3 Bucket Creation
```
bucketregion=cn-northwest-1
bucketname=workshopcode2023
filename=
```
```
aws s3api create-bucket \
    --bucket $bucketname \
    --region $bucketregion \
    --create-bucket-configuration LocationConstraint=$bucketregion
```

### IAM EC2 Instance Role Creation
```
rolename=workshopec2role
trustfile=trustpolicy-service.json

```

```
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://$trustfile --query 'Role.Arn' --output text)
echo $rolearn

```
```
policyname=AmazonSSMManagedInstanceCore
aws iam attach-role-policy --role-name=$rolename --policy-arn arn:aws-cn:iam::aws:policy/$policyname
policyname=AmazonS3ReadOnlyAccess
aws iam attach-role-policy --role-name=$rolename --policy-arn arn:aws-cn:iam::aws:policy/$policyname
aws iam list-attached-role-policies --role-name=$rolename
```
## Part 1: Networking and Security
### VPC and Subnets
```
vpcid=$(aws ec2 create-vpc \
    --cidr-block 10.0.0.0/16 \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=awsthreetierworkshop}]'\
    --query 'Vpc.VpcId' --output text)
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.1.0/28 --availability-zone=cn-northwest-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Web-1}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.2.0/28 --availability-zone=cn-northwest-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-App-1}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.3.0/28 --availability-zone=cn-northwest-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-DB-1}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.4.0/28 --availability-zone=cn-northwest-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Web-2}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.5.0/28 --availability-zone=cn-northwest-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-App-2}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.6.0/28 --availability-zone=cn-northwest-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-DB-2}]' --no-cli-pager
```
### Internet Connectivity
```
igwid=$(aws ec2 create-internet-gateway \
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=3tier-workshop-igw}]'\
    --query 'InternetGateway.InternetGatewayId' --output text)
echo $igwid
```
```
aws ec2 attach-internet-gateway \
    --internet-gateway-id $igwid\
    --vpc-id $vpcid 
```
#### NAT Gateway
列出之前创建的6个subnetsID,找到两个public的
```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table 
```
```
eip=$(aws ec2 allocate-address --query 'AllocationId' --output text )
echo $eip
subnet=
```
```
nat=$(aws ec2 create-nat-gateway \
    --subnet-id $subnet \
    --allocation-id $eip --query 'NatGateway.NatGatewayId' --output text)
echo $nat
```
###  Routing Configuration
```
rtb=$( aws ec2 create-route-table --vpc-id $vpcid --query 'RouteTable.RouteTableId' --output text)
echo $rtb
aws ec2 create-route --route-table-id $rtb --destination-cidr-block 0.0.0.0/0 --gateway-id $igwid
```
```
subnet=
aws ec2 associate-route-table --route-table-id $rtb --subnet-id $subnet

```
找到之前的两个NAT
```
aws ec2 describe-nat-gateways --query 'NatGateways[].[NatGatewayId,VpcId,SubnetId]' --output table
```
```
nat1=nat-0a63d17f564fb0f81
nat2=nat-05e70be262eea345e
private1=subnet-043129110913f5e19
private2=subnet-075a7070eff627dda
```
```
rtb1=$( aws ec2 create-route-table --vpc-id $vpcid --query 'RouteTable.RouteTableId' --output text)
echo $rtb1
aws ec2 create-route --route-table-id $rtb1 --destination-cidr-block 0.0.0.0/0 --gateway-id $nat1
aws ec2 associate-route-table --route-table-id $rtb1 --subnet-id $private1

```

```
rtb2=$( aws ec2 create-route-table --vpc-id $vpcid --query 'RouteTable.RouteTableId' --output text)
echo $rtb2
aws ec2 create-route --route-table-id $rtb2 --destination-cidr-block 0.0.0.0/0 --gateway-id $nat2
aws ec2 associate-route-table --route-table-id $rtb2 --subnet-id $private2

```
