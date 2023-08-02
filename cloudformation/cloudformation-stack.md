# list stacks in each region for filter
```
for region in $regions; do
aws cloudformation list-stacks --no-cli-pager \
--output text \
--query 'StackSummaries[?StackName!=`PVRE`].StackName' \
--region=$region
echo $region
done

```


# Create Cloudformation Stack
## create stack with parameter from a local template
```
stackname=aossiem
region=us-east-1
template=siem-on-amazon-opensearch-service.template
```
```

aws cloudformation create-stack --stack-name $stackname --template-body file://$template \
--capabilities CAPABILITY_NAMED_IAM \
--region=$region
```
## creat with parameter
```
p1=RDSUserName
v1=jessica
p2=RDSDBName
v2=rdsbjsm
```
? 像是一个选择的list怎么写参数呢？
```
aws cloudformation create-stack --stack-name $stackname --template-body file://$template \
--parameters  \
ParameterKey=$p1,ParameterValue=$v1  \
ParameterKey=$p2,ParameterValue=$v2  \
--capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_NAMED_IAM \
--region=$region

```
 *roles https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html
## create stack with parameter in all regions from a local template
```
stackname=myfirststack
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text))
```
```
for region in $regions; do
aws cloudformation create-stack --stack-name $stackname --template-body file://$template \
--parameters  \
ParameterKey=level0,ParameterValue=public  \
ParameterKey=level1,ParameterValue=internal  \
ParameterKey=level2,ParameterValue=sensitive  \
ParameterKey=level3,ParameterValue=topsecret  \
ParameterKey=tagkey,ParameterValue=datalevel  \
ParameterKey=s3bucketname,ParameterValue=maciemappingbucket  \
ParameterKey=s3filepath,ParameterValue=mapping.json \
--capabilities CAPABILITY_IAM \
--region=$region
echo $region
done

```
## From s3 url
```
stackname=myfirststack
region=us-east-1
url='https://s3.amazonaws.com/cloudformation-examples/community/common-attacks.json'
```
```
aws cloudformation create-stack --stack-name $stackname --template-url $url \
--capabilities CAPABILITY_IAM \
--region=$region
```


# Get Outputs from a stack

```
outputs=($(aws cloudformation describe-stacks --stack-name $stackname --region=$region \
--query 'Stacks[*].Outputs[*].OutputValue' --output text))
```
# Delete a stack
```
aws cloudformation delete-stack --stack-name $stackname
```
