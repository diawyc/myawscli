# [Module 1: Configure the Network](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/introduction/lab1)
```
aid=$(aws sts get-caller-identity --query 'Account' --output text)
region=eu-west-1
```
## 1.VPC
create 1 VPC and 6 Subnets in 2 AZs



| Network Name Tag Table|
| --- | 
|Wordpress-Workshop-VPC|
|Public Subnet A|
|Public Subnet B|
|Application Subnet A|
|Application Subnet B|
|Data Subnet A|
|Data Subnet B|


```

VpcCIDR='10.2.0.0/16'
PublicSubnetACIDR='10.2.0.0/24'
PublicSubnetBCIDR='10.2.1.0/24'
AppSubnetACIDR='10.2.2.0/24'
AppSubnetBCIDR='10.2.3.0/24'
DataSubnetACIDR='10.2.4.0/24'
DataSubnetBCIDR='10.2.5.0/24'
az1='eu-west-1a'
az2='eu-west-1b'
```


```
vpcid=$(aws ec2 create-vpc \
    --cidr-block $VpcCIDR \
    --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Wordpress-Workshop-VPC}]'\
    --query 'Vpc.VpcId' --output text)
echo $vpcid
```
```
pubsub1=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $PublicSubnetACIDR --availability-zone=$az1  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public Subnet A}]' --no-cli-pager --query 'Subnet.SubnetId' --output text)
pubsub2=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $PublicSubnetBCIDR --availability-zone=$az2  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public Subnet B}]' --no-cli-pager --query 'Subnet.SubnetId' --output text)
appsub1=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $AppSubnetACIDR --availability-zone=$az1 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Application Subnet A}]' --no-cli-pager --query 'Subnet.SubnetId' --output text)
appsub2=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $AppSubnetBCIDR --availability-zone=$az2 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Application Subnet B}]' --no-cli-pager --query 'Subnet.SubnetId' --output text)
datasub1=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $DataSubnetACIDR --availability-zone=$az1 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Data Subnet A}]' --no-cli-pager  --query 'Subnet.SubnetId' --output text)
datasub2=$(aws ec2 create-subnet --vpc-id=$vpcid --cidr-block $DataSubnetBCIDR --availability-zone=$az2  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Data Subnet B}]' --no-cli-pager  --query 'Subnet.SubnetId' --output text)
```
```
echo  $pubsub1 $pubsub2 $appsub1 $appsub2 $datasub1 $datasub2

```
### Check the result
```
aws ec2 describe-subnets --query 'Subnets[*].[Tags[0].Value,SubnetId]' --output table

```
## 2.Internet Gateway
| Name Tag|
| --- | 
| WP Internet Gateway| 
```
igwid=$(aws ec2 create-internet-gateway \
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=WP Internet Gateway}]'\
    --query 'InternetGateway.InternetGatewayId' --output text)
echo $igwid

aws ec2 attach-internet-gateway \
    --internet-gateway-id $igwid\
    --vpc-id $vpcid 
```
## 3.Route Table
| Name Tag|
| --- | 
| Wordpress Public| 
```
rtb=$(aws ec2 create-route-table --vpc-id $vpcid --tag-specifications --query 'RouteTable.RouteTableId' --output text)
echo $rtb
aws ec2 create-route --route-table-id $rtb --destination-cidr-block 0.0.0.0/0 --gateway-id $igwid
aws ec2 associate-route-table --route-table-id $rtb --subnet-id $pubsub1
aws ec2 associate-route-table --route-table-id $rtb --subnet-id $pubsub2
```

## 3.NAT Gateways

```
tag1=WP-Natgateway-A
eip=$(aws ec2 allocate-address --query 'AllocationId' --output text )
echo $eip
nat1=$(aws ec2 create-nat-gateway \
    --subnet-id $pubsub1 \
    --allocation-id $eip --query 'NatGateway.NatGatewayId' --output text)
arn1=arn:aws:ec2:$region:$aid:natgateway/$nat1
echo $natarn1
aws resourcegroupstaggingapi tag-resources \
    --resource-arn-list $arn1 \
    --tags Name=$tag1

```
```
rtb1=$( aws ec2 create-route-table --vpc-id $vpcid --query 'RouteTable.RouteTableId' --output text)
echo $rtb1
aws ec2 create-route --route-table-id $rtb1 --destination-cidr-block 0.0.0.0/0 --gateway-id $nat1
aws ec2 associate-route-table --route-table-id $rtb1 --subnet-id $appsub1

```

```
eip=$(aws ec2 allocate-address --query 'AllocationId' --output text )
echo $eip
nat2=$(aws ec2 create-nat-gateway \
    --subnet-id $pubsub2 \
    --allocation-id $eip --query 'NatGateway.NatGatewayId' --output text)
echo $nat2
arn2=arn:aws:ec2:$region:$aid:natgateway/$nat2
echo $arn2
aws resourcegroupstaggingapi tag-resources \
    --resource-arn-list $natarn2 \
    --tags Name=$tag2
```
```
rtb2=$( aws ec2 create-route-table --vpc-id $vpcid --query 'RouteTable.RouteTableId' --output text)
echo $rtb2
aws ec2 create-route --route-table-id $rtb2 --destination-cidr-block 0.0.0.0/0 --gateway-id $nat2
aws ec2 associate-route-table --route-table-id $rtb2 --subnet-id $appsub2

```
[back](readme.md)
