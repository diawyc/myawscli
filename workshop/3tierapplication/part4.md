# Internal Load Balancing and Auto Scaling

## App Tier AMI
```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value]' --output table
name=AppTierImage
des='App tier ec2 image with running app'

```
```
ec2id='i-0dcd53c37b94bebd2'
```
```

aws ec2 create-image \
    --instance-id $ec2id \
    --name $name \
    --description $des
```

ImageId='ami-09bbd796941eecbe7'
## Target Group

```
name='workshoptg'
```

```
aws elbv2 create-target-group \
    --name $name \
    --protocol HTTP \
    --port 4000 \
    --target-type instance \
    --vpc-id $vpcid
```
    
## Internal Load Balancer
## Launch Template
## Auto Scaling
[back to content](readme.md)
