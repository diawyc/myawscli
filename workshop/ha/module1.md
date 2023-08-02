# [Module 1: Configure the Network](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/introduction/lab1)
## 1.VPC
create 1 VPC and 6 Subnets in 2 AZs

| Basic Information|
| --- | 
| VPC ,IGW,Name Tag| 
| Wordpress-Workshop| 

| Subnet Name Tag|
| --- | 
|Wordpress-Workshop App Subnet A (AZ1)|
|Wordpress-Workshop App Subnet B (AZ2)|
|Wordpress-Workshop Data Subnet A (AZ1)|
|Wordpress-Workshop Data Subnet B (AZ2)|
|Wordpress-Workshop Public Subnet A (AZ1)|
|Wordpress-Workshop Public Subnet A (AZ1) |
|Wordpress-Workshop App Subnet B (AZ2)|



```
AppSubnetACIDR='192.168.2.0/24'
AppSubnetBCIDR='192.168.3.0/24'
DataSubnetACIDR='192.168.4.0/24'
DataSubnetBCIDR='192.168.5.0/24'
PublicSubnetACIDR='192.168.0.0/24'
PublicSubnetBCIDR='192.168.1.0/24'
VpcCIDR='192.168.0.0/16'
az1='us-east-1a'
az2='us-east-1b'
```


```
vpcid=$(aws ec2 create-vpc \
    --cidr-block $VpcCIDR \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Wordpress-Workshop}]'\
    --query 'Vpc.VpcId' --output text)
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $AppSubnetACIDR --availability-zone=$az1 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Wordpress-Workshop App Subnet A (AZ1)}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $AppSubnetBCIDR --availability-zone=$az2 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Wordpress-Workshop App Subnet B (AZ2)}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $DataSubnetACIDR --availability-zone=$az1 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Wordpress-Workshop Data Subnet A (AZ1)}]' --no-cli-pager
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $DataSubnetBCIDR --availability-zone=$az2  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Wordpress-Workshop Data Subnet B (AZ2)}]' --no-cli-pager
pubsub1=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $PublicSubnetACIDR --availability-zone=$az1  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Wordpress-Workshop App Subnet A (AZ1)}]' --no-cli-pager --query 'Subnet.SubnetId' --output text)
pubsub2=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $PublicSubnetBCIDR --availability-zone=$az2  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Wordpress-Workshop App Subnet B (AZ2)}]' --no-cli-pager --query 'Subnet.SubnetId' --output text)
echo $vpcid $pubsub1 $pubsub2
```
## 2.Internet Gateway
```
igwid=$(aws ec2 create-internet-gateway \
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=Wordpress-Workshop}]'\
    --query 'InternetGateway.InternetGatewayId' --output text)
echo $igwid

aws ec2 attach-internet-gateway \
    --internet-gateway-id $igwid\
    --vpc-id $vpcid 
```
## 3.NAT Gateways

```
subnet=$pubsub1
```
```
eip=$(aws ec2 allocate-address --query 'AllocationId' --output text )
echo $eip
nat=$(aws ec2 create-nat-gateway \
    --subnet-id $subnet \
    --allocation-id $eip --query 'NatGateway.NatGatewayId' --output text)
echo $nat
```
重复一次，需要两个NAT
```
subnet=$pubsub2
```
echo $vpcid $pubsub1 $pubsub2 $igwid > infor.text

[back](readme.md)
