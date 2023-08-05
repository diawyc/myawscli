# [Highly Available Web Application Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/introduction/overview)
## ![Overall Architecture](https://github.com/aws-samples/aws-refarch-wordpress/raw/master/images/aws-refarch-wordpress-v20171026.jpeg)


```
aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupName,GroupId]' --output table
aws rds describe-db-subnet-groups --query 'DBSubnetGroups[*].DBSubnetGroupName' --output table
aws ec2 describe-subnets --query 'Subnets[*].[Tags[0].Value,SubnetId]' --output table

```

## [Lab 1: Configure the network](lab1.md)
## [Lab 2: Set up your RDS database](lab2.md)
## [Lab 3: Set up Elasticache for Memcached](lab3.md)
## [Lab 4: Create the shared filesystem](lab4.md)

## [Lab 5: Create the load balancer](lab5.md)
## [Lab 6: Create a launch Template](lab6.md)
## [Lab 7: Create the app server](lab7.md)
## [Lab 5: Create the load balancer](lab8.md)
