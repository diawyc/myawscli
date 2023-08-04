# [Lab 4: Create the shared filesystem](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/database/lab4)
## Create filesystem security groups
```
sgname='WP FS Client SG'
des='file system client sg'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid  --query 'GroupId' --output text)
echo $groupid
sourcesg=$groupid

```

```
sgname='WP FS SG'
des='Allow NFS traffic from client to FS'
port='2049'
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --query 'GroupId' --output text)
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port $port \
    --source-group $sourcesg
```

## Create the EFS cluster
