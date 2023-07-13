# Part 6: External Load Balancer and Auto Scaling


## Web Tier AMI

```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value]' --output text
name=WebTierImage
des='Web tier ec2 image with running app'

```
```
ec2id='i-081bc7776c51b1fb4'
```
```

aws ec2 create-image \
    --instance-id $ec2id \
    --name $name \
    --description $des
```

 "ImageId": "ami-0ad640263352b6473"


## Target Group

```
name='WebTierTargetGroup'
vpcid=vpc-06b52efb9f0dd54f7
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
name='web-tier-external-lb'

```
```
sub1=subnet-01b6fb1492d8d49a3
sub2=subnet-0f9190f6ac6207318
sg=sg-0d08aeec68c3dfe93
```

```
lbarn=$(aws elbv2 create-load-balancer \
    --name $name \
    --subnets $sub1 $sub2 \
    --security-groups $sg --query 'LoadBalancers[].LoadBalancerArn' --output text)
echo $lbarn
```

```
aws elbv2 create-listener --load-balancer-arn $lbarn \
--protocol HTTP --port 80  \
--default-actions Type=forward,TargetGroupArn=$tgarn

```
## Launch Template
```
name=WebTierLaunchTemplate
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

![如图](workshop/3tierapplication/Screenshot 2023-07-12 at 12.14.47.png)

[Back to readme](readme.md)
