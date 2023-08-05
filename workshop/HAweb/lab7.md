# [Lab 7: Create the app server](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/application/lab7)
## create auto scaling group

```

name='Worldpress-asg'
```

```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name $name \
    --launch-template LaunchTemplateId=$lt \
    --target-group-arns $tgarn\
    --health-check-type ELB \
    --health-check-grace-period 600 \
    --min-size 0 \
    --max-size 2 \
    --vpc-zone-identifier $appsub1,$appsub2
```
