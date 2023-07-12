# Part 7 Security

## Configure https for ALB

### SSL/TLS certificate

### create https listener
```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,LoadBalancerArn]' --output table
aws elbv2 describe-target-groups --query 'TargetGroups[*].[TargetGroupName,TargetGroupArn]' --output table
aws acm list-certificates --query 'CertificateSummaryList[*].[DomainName,CertificateArn]' --output table
```

```
lbarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:loadbalancer/app/web-tier-external-lb/5676738e64e4f677'
tgarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:targetgroup/WebTierTargetGroup/297340c7e341f9d4'
certarn='arn:aws-cn:acm:cn-northwest-1:337075903349:certificate/5b371213-d424-4cd3-867a-500497d82586'
```

```
aws elbv2 create-listener --load-balancer-arn $lbarn \
--protocol HTTPS --port 443  \
--default-actions Type=forward,TargetGroupArn=$tgarn \
--certificates CertificateArn=$certarn,IsDefault=true
```



## WAF



[Back to readme](readme.md)
