# EC2

https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html
## 列出region内所有intanceID
```
ids=($(aws ec2 describe-instances  --region=$region --query 'Reservations[].Instances[].InstanceId' --output text))
echo $ids
len=${#ids[*]}
echo $len
```
```
for region in $regions; do
echo $region
aws ec2 describe-instances  --region=$region --query 'Reservations[].Instances[].InstanceId' --output table         
done
```
## 取到一台机器的IAM role arn
```
iid=i-0cc97b29f9c0448ed 
```
```
iparn=$(aws ec2 describe-instances --instance-ids=$iid  --region=$region --output=text  --query='Reservations[].Instances[].IamInstanceProfile[].Arn')
```
## 停机所有regions的所有机器
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
```
for region in $regions; do
echo $region
ids=($(aws ec2 describe-instances  --region=$region --query 'Reservations[].Instances[].InstanceId' --output text))
echo $ids
len=${#ids[*]}
echo $len
for ((i=1; i<=len; i++));do
aws ec2   stop-instances --instance-ids $ids[i] --region=$region
echo $ids[i]
done
done
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
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html
```
ami='ami-0f8ca7e3caf65286e'
num=1
type='t2.micro'
sg='sg-06885e46ad85c2417'
subnet=''
region=cn-north-1

```

```
aws ec2 run-instances \
    --image-id $ami \
    --count $num \
    --instance-type $type \
    --security-group-ids $sg \
    --subnet-id $subnet \
    --block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"Ebs\":{\"VolumeSize\":30,\"DeleteOnTermination\":false}}]" \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=demo-server}]' 'ResourceType=volume,Tags=[{Key=Env,Value=Prod}]'
 --region=$region
```
user data
```
#!/bin/bash
sudo yum install -y httpd
echo "Hello AWS，" | sudo tee /var/www/html/index.html
sudo systemctl start httpd
sudo systemctl enable httpd

```
