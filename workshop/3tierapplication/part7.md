# Part 7 Security

## Configure https for ALB

### SSL/TLS certificate

### create https listener
```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,LoadBalancerArn]' --output table
```

```
lbarn=
tgarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:loadbalancer/app/web-tier-external-lb/5676738e64e4f677'
```

```
aws elbv2 create-listener --load-balancer-arn $lbarn \
--protocol HTTPS --port 443  \
--default-actions Type=forward,TargetGroupArn=$tgarn
```



## WAF



[Back to readme](readme.md)
