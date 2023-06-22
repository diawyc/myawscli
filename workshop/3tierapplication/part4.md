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
name='AppTierTargetGroup'
vpcid=vpc-06b52efb9f0dd54f7
```

```
aws elbv2 create-target-group \
    --name $name \
    --protocol HTTP \
    --port 4000 \
    --target-type instance \
    --vpc-id $vpcid --health-check-path /health

```
    
## Internal Load Balancer


```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table 
name='app-tier-internal-lb'

```
```
sub1=subnet-043129110913f5e19
sub2=subnet-075a7070eff627dda
```

```
aws elbv2 create-load-balancer \
    --name $name \
    --scheme internal \
    --subnets $sub1 $sub2 \
    --security-groups sg-07e8ffd50fEXAMPLE

```

## Launch Template
## Auto Scaling
[back to content](readme.md)
