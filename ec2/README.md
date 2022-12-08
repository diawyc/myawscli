# EC2

https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html
## 列出所有intanceID
```
ids=($(aws ec2 describe-instances  --region=us-east-1 --query 'Reservations[].Instances[].InstanceId' --output text))
echo $ids
len=${#ids[*]}
echo $len
```
### 通过内网IP查询ec2的instanceid
```
ip=172.31.21.178
region=us-east-1
```

```
instanceid=$(aws ec2 describe-instances  --filters Name=network-interface.addresses.private-ip-address,Values=$ip --region=$region --query 'Reservations[0].Instances[*].InstanceId'   --output text)
```
### 通过内网IP与VPC共同查询ec2的instanceid
### paramter
```
ip=172.31.21.178
region=us-east-1
vpc=vpc-0ed0c20198b73ff13
```

```
instanceid=$(aws ec2 describe-instances  --filters Name=network-interface.addresses.private-ip-address,Values=$ip Name=vpc-id,Values=$vpc --region=$region --query 'Reservations[0].Instances[0].InstanceId'   --output text)

```
### 查询NACL现有的Rule
https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-acls.html

```
aws ec2 describe-network-acls --output text --query 'NetworkAcls[0].[Entries]' --region=$region
```
## create 一台带httpt web的EC2

```
aws ec2 describe-network-acls --output text --query 'NetworkAcls[0].[Entries]' --region=$region
```
user data
```
#!/bin/bash
sudo yum install -y httpd
echo "Hello AWS，" | sudo tee /var/www/html/index.html
sudo systemctl start httpd
sudo systemctl enable httpd

```
