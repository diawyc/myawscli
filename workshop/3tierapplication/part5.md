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
    --associate-public-ip-address \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Weblayer}]' --query 'Instances[].InstanceId' --output text)

echo $id

```

## Connect to Instance
ASG新启动的两台没有Name Tag所以无法呈现table
```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value]' --output text
```
```
id="i-02350bdbc3f9a8185"

aws ssm start-session \
    --target $id
```
有可能curl的时候连不github了就自己下载放到S3上再下载到本机运行， sudo aws s3 cp s3://yourbucketname/install.sh install.sh --region=cn-northwest-1

sudo chmod u+x install.sh
sudo ./install.sh

```
aws configure set region cn-northwest-1
bucketname=workshopcode2023
cd ~/
aws s3 cp s3://$bucketname/web-tier/ web-tier --recursive --region=cn-northwest-1
```

```

bucketname=workshopcode2023
sudo rm nginx.conf
sudo aws s3 cp s3://$bucketname/nginx.conf nginx.conf --region=cn-northwest-1
```

```
sudo service nginx restart
sudo chmod -R 755 /home/ec2-user
```
```
aws ec2 describe-instances --query 'Reservations[*].Instances[?InstanceId==`i-02350bdbc3f9a8185`].PublicIpAddress' --output text
```
[back to content](readme.md)
