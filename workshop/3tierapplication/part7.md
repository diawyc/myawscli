# Part 7 Security

## Configure https for ALB

### SSL/TLS certificate

### create https listener
```
aws elbv2 create-listener --load-balancer-arn $lbarn \
--protocol HTTPS --port 443  \
--default-actions Type=forward,TargetGroupArn=$tgarn
```



## WAF



[Back to readme](readme.md)
