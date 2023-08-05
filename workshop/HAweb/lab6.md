# [Lab 6: Create a launch Template](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/application/lab6)

sgname='WP Wordpress SG'

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
