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
## Auto Scaling


[Back to readme](readme.md)
