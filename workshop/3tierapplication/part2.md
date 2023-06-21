# Part 2: Database Deployment
## Subnet Groups
```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table 
```
```
name='3tierdb'
des='subnetgroup for database mysql '
```





## Database Deployment




[back to readme](readme.md)
