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
id=$(aws ec2 run-instances \
    --image-id $ami\
    --instance-type $type \
    --subnet-id $subnet \
    --security-group-ids $sg \
    --iam-instance-profile Name=$role \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Applayer}]' --query 'Instances[].InstanceId' --output text)

echo $id

```
## Connect to Instance
```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value]' --output table
```
```
id="i-0dcd53c37b94bebd2"

aws ssm start-session \
    --target $id
```
exit断开session,此处最好新开一个window
## Configure Database
https://catalog.us-east-1.prod.workshops.aws/workshops/85cd2bb2-7f79-4e96-bdee-8078e469752a/en-US/part3/configuredatabase
```
aws rds describe-db-cluster-endpoints

```
```
mysql -h threetierdb.cluster-c2fs4j8mvbrb.rds.cn-northwest-1.amazonaws.com.cn -u admin -p
```
[see there](https://github.com/jessicawyc/myawscli/blob/main/workshop/3tierapplication/part2.md#database-deployment)
## Configure App Instance
aws
```
bucketname=workshopcode2023
```

```
aws s3 cp aws-three-tier-web-architecture-workshop s3://$bucketname/ --recursive
aws s3 ls s3://$bucketname/
```
session manager
```
bucketname=workshopcode2023
cd ~/
aws s3 cp s3://$bucketname/app-tier/ app-tier --recursive
```
## Test App Tier




[back](readme.md)
