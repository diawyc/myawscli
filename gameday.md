
# create a bucket and upload resource
```
bucketregion=us-east-1
bucketname=
filename=
```
```
aws s3api create-bucket \
    --bucket $bucketname \
    --region $bucketregion
```
```
aws s3 cp $filename s3://$bucketname/ --region=$bucketregion --recursive
```
```
aws s3api list-objects --bucket=$bucketname --query 'Contents[].Key' --output text
```
# Network design
```
vpcid=$(aws ec2 describe-vpcs --query 'Vpcs[?IsDefault!=`true`].VpcId' --output text)
```
## run CFN to create network components

```
stackname=gamedaynetwork
template=gameday-network.yml
```
```

aws cloudformation create-stack --stack-name $stackname --template-body file://$template \
--capabilities CAPABILITY_NAMED_IAM 
```

