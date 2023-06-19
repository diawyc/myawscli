https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html

##create a defaul VPC
```
vpcid=$(aws ec2 create-default-vpc --query 'Vpc.Vpcid' --output text )  
```
