# [Module 2](https://catalog.us-east-1.prod.workshops.aws/workshops/5ceb632a-c07f-44a5-a3bd-b8f616a631c0/en-US/database/lab2)

cloudformation中有错误，要将aurora修改为aurora-mysql
vpcid是使用前一个module1的输出

## RDS

## create DB subnet group 
[CLI reference](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-subnet-group.html)

```
sngname='module2-databasesubnetgroup'
des='subnetgroup for database mysql'
aws rds create-db-subnet-group \
    --db-subnet-group-name $name \
    --db-subnet-group-description $des \
    --subnet-ids '["subnet-0877032c0c23c7368","subnet-0c979a57817ecb053"]' 

```
## create a security group for DB and client

```
sourcesg=$groupid
echo $sourcesg
sgname='WP Database Client SG'
des='sg for the private app tier instance'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=5.Private-instance}]' --query 'GroupId' --output text)
echo $groupid
```

```
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 4000 \
    --cidr 0.0.0.0/0

```


```
sourcesg=$groupid
echo $sourcesg
sgname='WP Database SG'
des='sg for the private database'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=6.DB-private}]' --query 'GroupId' --output text)
echo $groupid
```
```

aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 3306 \
    --source-group $sourcesg
```
```
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-`].[GroupName,GroupId]' --output table
```
```

dbsg=''
serversg=''

```

```

dbsg='WP Database SG'
serversg='WP Database Client SG'

```

## create database
```
dbname='wordpressb'
type=aurora-mysql
sg=?
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
    --db-subnet-group-name $sngname \
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
