# Part 2: Database Deployment
## Subnet Groups
[CLI](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)
```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table 
```
```
name='threetierdb'
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
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-06b52efb9f0dd54f7`].[GroupName,GroupId]' --output table
aws rds describe-db-subnet-groups --query 'DBSubnetGroups[*].DBSubnetGroupName' --output table

```
```
dbname='threetierdb'
type=aurora-mysql
sg=sg-0d10449341610d9bf
name='threetierdb'
```

```
dbendpoint=$(aws rds create-db-cluster \
    --db-cluster-identifier $dbname \
    --engine $type \
    --engine-version 5.7 \
    --master-username admin \
    --master-user-password secret99 \
    --db-subnet-group-name $name \
--no-publicly-accessible \
    --vpc-security-group-ids $sg \
--query 'DBCluster.Endpoint' --output text)

echo $dbendpoint
```
```
aws rds create-db-instance --db-instance-identifier $dbname
     --db-cluster-identifier $dbname --engine aurora-mysql --db-instance-class db.r4.large --db-parameter-group aurora_pg --port 3306
```
[back to readme](readme.md)
