# [Module 2](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/database/lab2)

cloudformation中有错误，要将aurora修改为aurora-mysql
vpcid是使用前一个module1的输出
## RDS

```
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-06b52efb9f0dd54f7`].[GroupName,GroupId]' --output table
aws rds describe-db-subnet-groups --query 'DBSubnetGroups[*].DBSubnetGroupName' --output table

```
```
dbname='threetierdb'
type=aurora-mysql
sg=sg-0d10449341610d9bf
name='threetierdb'
username='jessica'
password='password'
```

```
dbendpoint=$(aws rds create-db-cluster \
    --db-cluster-identifier $dbname \
    --engine $type \
    --engine-version 5.7 \
    --master-username $username \
    --master-user-password $password \
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

## Security Groups

```

dbsg='WP Database SG'
serversg='WP Database Client SG'
des='subnetgroup for database mysql'

```

[CLI reference](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)


```
aws rds create-db-subnet-group \
    --db-subnet-group-name $dbsg \
    --db-subnet-group-description $des \
    --subnet-ids '["subnet-0877032c0c23c7368","subnet-0c979a57817ecb053"]' 

```


[reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html)
[back to readme](readme.md)
