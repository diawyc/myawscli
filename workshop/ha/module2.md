# [Module 2](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/database/lab2)

cloudformation中有错误，要将aurora修改为aurora-mysql
vpcid是使用前一个module1的输出
## RDS

## create DB subnet group 
[CLI reference](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)

```
module2-databasesubnetgroup
des='subnetgroup for database mysql'
```
```
aws rds create-db-subnet-group \
    --db-subnet-group-name $name \
    --db-subnet-group-description $des \
    --subnet-ids '["subnet-0877032c0c23c7368","subnet-0c979a57817ecb053"]' 

```

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



```

dbsg='WP Database SG'
serversg='WP Database Client SG'


```



[reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html)
[back to readme](readme.md)
