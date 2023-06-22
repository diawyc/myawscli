# Internal Load Balancing and Auto Scaling

## App Tier AMI
```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value]' --output table
name=AppTierImage
des='App tier ec2 image with running app'

```
```
ec2id=
```
```

aws ec2 create-image \
    --instance-id $ec2id \
    --name $name \
    --description $des
```
## Target Group
## Internal Load Balancer
## Launch Template
## Auto Scaling
[back to content](readme.md)
