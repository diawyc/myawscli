# [Lab 2: Set up your RDS database]([url](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/database/lab2))
## Create an RDS subnet group

```
sgname='WP Database Client SG'
des='DB client security group'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=6.DB-private}]' --query 'GroupId' --output text)
echo $groupid
sourcesg=$groupid
```
```
sgname='WP Database SG'
des='allow rds/aurora traffic'
port=3306
```

```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=DBSG}]' --query 'GroupId' --output text)
echo $groupid

aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port $port \
    --source-group $sourcesg
```
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
