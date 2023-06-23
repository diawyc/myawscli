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

ImageId='ami-09bbd796941eecbe7'





## Target Group
## Internet Facing Load Balancer 
## Launch Template
## Auto Scaling


[Back to readme](readme.md)
