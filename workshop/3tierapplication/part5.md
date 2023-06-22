# Part 5: Web Tier Instance Deployment

## Update Config File

```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].DNSName' --output table
```


```
bucketname=workshopcode2023
```

```
aws s3 cp aws-three-tier-web-architecture-workshop/application-code/web-tier s3://$bucketname/web-tier --recursive
aws s3 cp aws-three-tier-web-architecture-workshop/application-code/nginx.conf s3://$bucketname/
aws s3 ls s3://$bucketname/
```

Web Instance Deployment
Connect to Instance
Configure Web Instance

## Web Instance Deployment

```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-06b52efb9f0dd54f7`].[GroupName,GroupId]' --output table


```

```
ami=ami-06520f8b43f60048c
subnet=subnet-01b6fb1492d8d49a3
sg=sg-084acd7997e0276f3
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
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Weblayer}]' --query 'Instances[].InstanceId' --output text)

echo $id

```

[back to content](readme.md)
