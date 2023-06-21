# Part 2: Database Deployment
## Subnet Groups
[CLI](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)
```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table 
```
```
name='threetierDB'
des='subnetgroup for database mysql '

```
```
aws rds create-db-subnet-group \
    --db-subnet-group-name $name \
    --db-subnet-group-description $des \
    --subnet-ids '["subnet-056292e902d22a7e1","subnet-036b90652a69b55ec"]' 

```

## Database Deployment

```
dbname='threetierDB'
type=aurora-mysql
```

```
aws rds create-db-cluster \
    --db-cluster-identifier $dbname \
    --engine $type \
    --engine-version 5.7 \
    --master-username admin \
    --master-user-password secret99 \
    --db-subnet-group-name $name \
    --vpc-security-group-ids sg-0b9130572daf3dc16


```

[back to readme](readme.md)
