# [Lab 2: Set up your RDS database]([url](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/database/lab2))
## Create an RDS subnet group


SBname='WP Database SG'
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
## Create the Aurora database cluster

```
dbname='Wordpress-Workshop'
type=aurora-mysql
sg=?
username='jessica'
password='password123'
engine='aurora-mysql'
inclass='db.r5.large'
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
     --db-cluster-identifier $dbname --engine $engine --db-instance-class $inclass
```

[reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html)
[back to readme](readme.md)
