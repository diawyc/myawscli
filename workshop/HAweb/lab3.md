# [Lab 3: Set up Elasticache for Memcached](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/database/lab3)
## create security group
```
sgname='WP Cache SG'

```


des='external load banlancer security group'
port=''
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=DBSG}]' --query 'GroupId' --output text)
echo $groupid

aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port $port \
    --source-group $sourcesg
```
## create subnet group


sgname='Wordpress-Elasticache'
