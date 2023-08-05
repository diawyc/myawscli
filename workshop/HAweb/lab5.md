# [Lab 5: Create the load balancer](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/application/lab5)

```
 sgname='WP Load Balancer SG'
 port=80
 des='Load balancer security group'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --query 'GroupId' --output text)
echo $groupid

aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port $port \
    --cidr 0.0.0.0/0
```

## Create load balancer and application security groups




## Target Group

```
name='wordpress-targetgroup'
```

```
tgarn=$(aws elbv2 create-target-group \
    --name $name \
    --protocol HTTP \
    --port 80 \
    --target-type instance \
    --vpc-id $vpcid --health-check-path /health --query 'TargetGroups[].TargetGroupArn' --output text)
echo $tgarn
```
## Internet Facing Load Balancer 

```
name='wordpress-alb'

```


```
lbarn=$(aws elbv2 create-load-balancer \
    --name $name \
    --subnets $pubsub1 $pubsub2 \
    --security-groups $groupid --query 'LoadBalancers[].LoadBalancerArn' --output text)
echo $lbarn
```

```
aws elbv2 create-listener --load-balancer-arn $lbarn \
--protocol HTTP --port 80  \
--default-actions Type=forward,TargetGroupArn=$tgarn

```
## Launch Template
```
name=
ImageId=ami-0ad640263352b6473
security group  :sg-084acd7997e0276f3
instancerole name:workshopec2role
```

```
lt=$(aws ec2 create-launch-template \
    --launch-template-name $name \
    --version-description WebVersion1 \
    --launch-template-data '{"IamInstanceProfile": {"Name": "workshopec2role"},"NetworkInterfaces":[{"DeviceIndex":0,"Groups":["sg-084acd7997e0276f3"]}],"ImageId":"ami-0ad640263352b6473","InstanceType":"t2.micro"}' \
    --query 'LaunchTemplate.LaunchTemplateId' --output text)
echo $lt
```
## Auto Scaling
```
name='WebTierAsg'
```
```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name $name \
    --launch-template LaunchTemplateId=$lt \
    --target-group-arns $tgarn\
    --health-check-type ELB \
    --health-check-grace-period 600 \
    --min-size 2 \
    --max-size 2 \
    --vpc-zone-identifier $sub1,$sub2
```

## Get Web LB DNS NAME in webbrowser
```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,DNSName]' --output table
```

![如图](webpage.png)

[Back to readme](readme.md)
