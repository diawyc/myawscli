# AWS Three Tier Web Architecture Workshop

## Architecture Overview
![Architecture Diagram](https://github.com/aws-samples/aws-three-tier-web-architecture-workshop/blob/main/application-code/web-tier/src/assets/3TierArch.png)

In this architecture, a public-facing Application Load Balancer forwards client traffic to our web tier EC2 instances. The web tier is running Nginx webservers that are configured to serve a React.js website and redirects our API calls to the application tier’s internal facing load balancer. The internal facing load balancer then forwards that traffic to the application tier, which is written in Node.js. The application tier manipulates data in an Aurora MySQL multi-AZ database and returns it to our web tier. Load balancing, health checks and autoscaling groups are created at each layer to maintain the availability of this architecture.

## Workshop Instructions:

See [AWS Three Tier Web Architecture](https://catalog.us-east-1.prod.workshops.aws/workshops/85cd2bb2-7f79-4e96-bdee-8078e469752a/en-US)

# CLI
## [Part 0](part0.md)
## [Part 1](part1.md)
## [Part 2](part2.md)
## [Part 3](part3.md)
## [Part 4](part4.md)
## [Part 5](part5.md)
## [Part 6](part6.md)

AppTier Inforamtion
```
tgarn=arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:targetgroup/AppTierTargetGroup/600f78217667ede8
vpcid=vpc-06b52efb9f0dd54f7
lbarn=arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:loadbalancer/app/app-tier-internal-lb/b960d1bde66b4465
lt=lt-0f0fd715fec3a3c60
ImageId='ami-09bbd796941eecbe7'
```
```
aws ec2 describe-subnets --query 'Subnets[?VpcId==`vpc-06b52efb9f0dd54f7`].[Tags[0].Value,SubnetId]' --output table
aws ec2 describe-security-groups --query 'SecurityGroups[?VpcId==`vpc-06b52efb9f0dd54f7`].[GroupName,GroupId]' --output table
aws ec2 describe-launch-templates --query 'LaunchTemplates[*].[LaunchTemplateName,LaunchTemplateId]' --output table
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].DNSName' --output table

```
WebTier Inforamtion

```
tgarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:targetgroup/WebTierTargetGroup/297340c7e341f9d4'
lbarn='arn:aws-cn:elasticloadbalancing:cn-northwest-1:337075903349:loadbalancer/app/web-tier-external-lb/5676738e64e4f677'
lt='lt-04c981b53f95b1c6c'
```
