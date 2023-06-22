# Part 5: Web Tier Instance Deployment

## Update Config File

```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].DNSName' --output table
```


```
bucketname=workshopcode2023
```

```
aws s3 cp aws-three-tier-web-architecture-workshop/application-code/web-tier s3://$bucketname/web-tier --recursive
aws s3 cp aws-three-tier-web-architecture-workshop/application-code/nginx.conf s3://$bucketname/
aws s3 ls s3://$bucketname/
```

Web Instance Deployment
Connect to Instance
Configure Web Instance


[back to content](readme.md)
