# [Lab 5: Create the load balancer](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/application/lab5)
## create security group
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


[Back to readme](readme.md)
