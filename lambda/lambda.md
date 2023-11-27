# 等级保护
## 数据库访问权限
```
aws lambda list-functions --quer 'Functions[*].[FunctionName,Role]' --output table
```

```
name=
```
```
aws iam list-role-policies --role-name $name
aws iam list-attached-role-policies \
    --role-name $name --quer 'AttachedPolicies[*].PolicyName' --output table
```
```
aws iam list-attached-role-policies \
    --role-name $name --quer 'AttachedPolicies[*].PolicyArn' --output table
```
```
 aws iam get-policy-version --policy-arn $arn --version-id v1  
```
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
## [create lambda function](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html)
```
name='lvli-event-dev'
runtime='python3.11'
filename='lambda.zip'
rolearn='arn:aws-cn:iam::'$accountid':role/service-role/'$rolename
region='cn-northwest-1'
vdic={k1=v1,k2=v2}
```

```
lambdaarn=$(aws lambda create-function \
    --function-name $name \
    --runtime $runtime \
    --zip-file fileb://$filename \
    --handler index.lambda_handler \
    --environment Variables=$vdic \
    --role $rolearn --region=$region --no-cli-pager --query 'FunctionArn' --output text)
echo $lambdaarn
```
## add Resource-based policy statements to lambda

```
des='dynamodbstream'
trigger='dynamodb.amazonaws.com'
name='event_update'
fname='lvli_result_qt'
region=cn-northwest-1
sourcearn=$(aws dynamodb describe-table --table-name $name --no-cli-pager --query 'Table.LatestStreamArn' --output text)
```
```
aws lambda add-permission \
--function-name $fname \
--statement-id $des \
--action 'lambda:InvokeFunction' \
--principal $trigger \
--source-arn $sourcearn --region=$region
```
## Add DynamoDB stream trigger

aws lambda create-event-source-mapping \
    --region $region \
    --function-name $fname \
    --event-source $sourcearn \
    --batch-size 1 \
    --starting-position TRIM_HORIZON
## 从eventbridge 关联source trigger到lambda
```
aws events put-targets --rule $rulename  --targets "Id"="1","Arn"=$lambdaarn --region=$region
```
## 查看现有的mapping
```
aws lambda get-event-source-mapping \
    --uuid "f221ba63-6a11-45cb-8850-7a477f1c0e95"
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

