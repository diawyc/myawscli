# [Lab 2: Set up your RDS database]([url](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/database/lab2))
## Create an RDS subnet groupHeader anchor link
[CLI](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)

```
name='Aurora-Wordpress'
des='RDS subnet group used by Wordpress '
echo $datasub1 $datasub2
```
```
aws rds create-db-subnet-group \
    --db-subnet-group-name $name \
    --db-subnet-group-description $des \
    --subnet-ids '["<datasub1>","<datasub2>"]' 

```
? 有什么办法带参数进去？
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
aws rds create-db-instance --db-instance-identifier $dbname \
     --db-cluster-identifier $dbname --engine aurora-mysql --db-instance-class db.r5.large
```

[reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html)
[back to readme](readme.md)
