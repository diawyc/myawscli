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
## Launch Template
## Auto Scaling


[Back to readme](readme.md)
