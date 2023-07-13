# Part 7 Security

## Configure https for ALB
###  Custome Domain Name
在route53上创建一条A record，选择ALB

### SSL/TLS certificate
```
dns='alb.wyc.people.a2z.org.cn'
```
```
certarn=$(aws acm request-certificate --domain-name $dns --validation-method DNS --query 'CertificateArn' --output text)
echo $certarn
```
valida in route53, no CLI ,must use console
### create https listener
```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,LoadBalancerArn]' --output table
aws elbv2 describe-target-groups --query 'TargetGroups[*].[TargetGroupName,TargetGroupArn]' --output table
aws acm list-certificates --query 'CertificateSummaryList[*].[DomainName,CertificateArn]' --output table
```

```
lbarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:'
tgarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:'
certarn='arn:aws-cn:acm:cn-northwest-1:6'
```

```
aws elbv2 create-listener --load-balancer-arn $lbarn \
--protocol HTTPS --port 443  \
--default-actions Type=forward,TargetGroupArn=$tgarn \
--certificates CertificateArn=$certarn
```
删除旧的http listener
```
aws elbv2 describe-listeners --load-balancer-arn $lbarn --query 'Listeners[*].[ListenerArn,Protocol]' --output table
httparn=
```
```

aws elbv2 delete-listener \
    --listener-arn $httparn

```

[reference](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-listener.html#:~:text=%2D%2D-,certificates,-(list))

#### update Security group


```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,SecurityGroups[0]]' --output table
groupid='sg-0d08aeec68c3dfe93'
```
```

aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0
```
## 查看结果
http://alb.wyc.people.a2z.org.cn/
无法访问
https://alb.wyc.people.a2z.org.cn/#/

[显示如下](Screenshot 2023-07-12 at 12.14.47.png)

[Back to readme](readme.md)
