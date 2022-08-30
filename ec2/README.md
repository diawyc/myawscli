# EC2

https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html

### 通过内网IP查询ec2的
```
ip=172.31.21.178
region=us-east-1
```

```
aws ec2 describe-instances  --filters Name=network-interface.addresses.private-ip-address,Values=$ip --region=$region --query 'Reservations[0].Instances[*].InstanceId'   --output text
```
