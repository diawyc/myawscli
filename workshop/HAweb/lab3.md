# [Lab 3: Set up Elasticache for Memcached](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/database/lab3)
## Create cache security groups
```
sgname='WP Cache Client SG'
des='Elasticache client'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid  --query 'GroupId' --output text)
echo $groupid
sourcesg=$groupid
```
```
sgname='WP Cache SG'
des='WP cache sg'
port='11211'
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid  --query 'GroupId' --output text)
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port $port \
    --source-group $sourcesg
sg=$groupid
```


## create subnet group
```
name='Wordpress-Elasticache'
des='subnet group used by elasticache'
```
```
aws elasticache create-cache-subnet-group \
    --cache-subnet-group-name $name \
    --cache-subnet-group-description $des \
    --subnet-ids $dbsubnet1 $dbsubnet2
```
