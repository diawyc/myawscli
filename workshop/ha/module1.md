# [Module 1: Configure the Network](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/introduction/lab1)
## 1.create 1 VPC and 6 Subnets in 2 AZs
VPC ,IGW,Name Tag:	Wordpress-Workshop


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
PublicSubnetBCIDR='192.168.1.0/24
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
echo $pubsub1 $pubsub2
```
## 2.Internet Connectivity
```
igwid=$(aws ec2 create-internet-gateway \
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=Wordpress-Workshop}]'\
    --query 'InternetGateway.InternetGatewayId' --output text)
echo $igwid
```
```
aws ec2 attach-internet-gateway \
    --internet-gateway-id $igwid\
    --vpc-id $vpcid 
```
#### NAT Gateway

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
## 3.Routing Configuration
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
## 4.Security Groups
[cli](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-security-group.html)https://docs.aws.amazon.com/cli/latest/reference/ec2/create-security-group.html)
#### step1-2
```
sgname='internet-lb'
des='external load banlancer security group'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=2.internet-lb}]' --query 'GroupId' --output text)
echo $groupid

```
```
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
```
#### step 3
```
sourcesg=$groupid
sgname='WebTierSg'
des='sg for the web tier'

```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=3.webtier}]' --query 'GroupId' --output text)
echo $groupid

```
```
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 80 \
    --source-group $sourcesg
```
#### step 4
```
sourcesg=$groupid
sgname='Internal-LB'
des='sg for the internal load balancer'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=4.webtier}]' --query 'GroupId' --output text)
echo $groupid

```
```
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 80 \
    --source-group $sourcesg
```
#### step 5

```
sourcesg=$groupid
echo $sourcesg
sgname='Private-instance'
des='sg for the private app tier instance'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=5.Private-instance}]' --query 'GroupId' --output text)
echo $groupid
```

```
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 4000 \
    --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 4000 \
    --source-group $sourcesg
```
#### step 6

```
sourcesg=$groupid
echo $sourcesg
sgname='DB-private'
des='sg for the private database'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=6.DB-private}]' --query 'GroupId' --output text)
echo $groupid
```
```

aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 3306 \
    --source-group $sourcesg
```
```
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-06b52efb9f0dd54f7`].[GroupName,GroupId]' --output table
```
[back](readme.md)
