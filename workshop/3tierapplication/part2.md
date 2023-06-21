# Part 2: Database Deployment
## Subnet Groups
[CLI](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)
```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table 
```
```
name='threetierDB'
des='subnetgroup for database mysql '
sub1='subnet-056292e902d22a7e1'
sub2='subnet-036b90652a69b55ec'
```
```
aws rds create-db-subnet-group \
    --db-subnet-group-name $name \
    --db-subnet-group-description $des \
    --subnet-ids $sub1,$sub2

```

## Database Deployment




[back to readme](readme.md)
