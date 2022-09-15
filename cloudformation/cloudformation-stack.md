# Cloudformation
## create stack with parameter in all regions from a local template
```
stackname=macieautotag2ways
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text))
```
```
for region in $regions; do
aws cloudformation create-stack --stack-name $stackname --template-body file://Arch1-template.yaml \
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
aws cloudformation create-stack --stack-name $stackname --template-url https://s3.amazonaws.com/cloudformation-examples/community/common-attacks.json \
--capabilities CAPABILITY_IAM \
--region=$region
```
## delete 
```
aws cloudformation delete-stack --stack-name $stackname
```
