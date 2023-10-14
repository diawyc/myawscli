# I love aws cli

## 查看所有regions中lambda functions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```

```
for region in $regions; do
echo $region
aws lambda list-functions  --region=$region --no-cli-pager
done
```
list function name
```
aws lambda list-functions --query 'Functions[].FunctionName' --output table
```
## create lambda function
```
lambdaarn=$(aws lambda create-function \
    --function-name $function \
    --runtime python3.9 \
    --zip-file fileb://index.zip \
    --handler index.lambda_handler \
    --role $rolearn --region=$region --no-cli-pager --query 'FunctionArn' --output text)
echo $lambdaarn
```
## add to a eventbridge rule to trigger
```
aws lambda add-permission \
--function-name $function \
--statement-id eb-rule \
--action 'lambda:InvokeFunction' \
--principal events.amazonaws.com \
--source-arn $rulearn --region=$region
aws events put-targets --rule $rulename  --targets "Id"="1","Arn"=$lambdaarn --region=$region
```
## [download requirement](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html#integrations-s3-lambda-deployment-package)
```
cd foldername

pip install --target ./package requests
pip install --target ./package requests_aws4auth
```
