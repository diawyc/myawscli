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
name='lvli-event-dev'
runtime='python3.11'
filename='lambda.zip'
rolearn=''
region='cn=northwest-1'
```
lambdaarn=$(aws lambda create-function \
    --function-name $name \
    --runtime $runtime \
    --zip-file fileb://$filename \
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

```

pip3 install --target ./package -r requirements.txt
cd package
zip -r ../lambda.zip .
```
### upload function code
```
fname='ddb-lambda-aos-ddbaosesgithub-8rZa1DESAWdy'
zname='lambda.zip'
```
```
aws lambda update-function-code \
    --function-name  $fname \
    --zip-file fileb://$zname --region=$region

```
### add env variables
```
aws lambda update-function-configuration \
    --function-name  $fname \
    --environment "Variables={DB_HASH_KEY='logid',ES_HOST='https://search-lambda-wu67m6l2am5kopbmzs43vejag4.cn-northwest-1.es.amazonaws.com.cn',ES_INDEX_1=test-gb,ES_INDEX_2=test-db,S3_name=lvliserver-info,KEY=mapping.json}"
   
```

