# Part 3: App Tier Instance Deployment
## App Instance Deployment

```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-06b52efb9f0dd54f7`].[GroupName,GroupId]' --output table
aws iam list-roles --query 'Roles[*].RoleName' --output table

```

```
ami=ami-06520f8b43f60048c
subnet=subnet-043129110913f5e19
sg=sg-0ba686ac638d76062
type=t2.micro
role=workshopec2role
```
```
aws ec2 run-instances \
    --image-id $ami\
    --instance-type $type \
    --subnet-id $subnet \
    --security-group-ids $sg \
    --iam-instance-profile $role \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Applayer}]' 



```
## Connect to Instance
## Configure Database
## Configure App Instance
## Test App Tier




[back](readme.md)
