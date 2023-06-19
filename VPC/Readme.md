https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html

## create a defaul VPC
```
vpcid=$(aws ec2 create-default-vpc --query 'Vpc.Vpcid' --output text)  
```
## create a VPC
```
vpcid=$(aws ec2 create-vpc \
    --cidr-block 10.0.0.0/16 \
    --tag-specification ResourceType=vpc,Tags=[{Key=Name,Value=awsthreetierworkshop}] --query 'Vpc.Vpcid' --output text --dry-run)  
    ```
