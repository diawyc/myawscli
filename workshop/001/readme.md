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
vpcid=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.Vpcid' --output text)
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.1.0/28 --availability-zone=cn-northwest-1a
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.2.0/28 --availability-zone=cn-northwest-1a
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.3.0/28 --availability-zone=cn-northwest-1a
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.4.0/28 --availability-zone=cn-northwest-1b
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.5.0/28 --availability-zone=cn-northwest-1b
aws ec2 create-subnet --vpc-id=$vpcid --cidr-block 10.0.6.0/28 --availability-zone=cn-northwest-1b

```

