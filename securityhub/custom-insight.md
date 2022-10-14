## create a custom insight and get its ARN
### Set parameter参数设置

region为securityhub指定的聚合aggregated region

```
region='eu-west-2'
insight='BackupAlert'
```

### CLI command 
```
insightarn=$(aws securityhub create-insight \
--filters \
 '{"RecordState": [{ "Comparison": "EQUALS", "Value": "ACTIVE"}], "WorkflowStatus": [{"Comparison": "EQUALS", "Value": "NEW"}], "ProductName": [{"Comparison": "EQUALS", "Value": "Default"}]}' \
 --group-by-attribute "ResourceId" \
--name $insight \
--query 'InsightArn' --output text --region=$region)
```
## Get all custom insights ARN
### Set parameter参数设置
```
region='eu-west-2'

```
### command
```
aws securityhub get-insights  --region=$region
```
```
customarn=$(aws securityhub get-insights  --query 'Insights[*].InsightArn' --output text --region=$region)
```
```
aws securityhub get-insights  --query 'Insights[*].{n:Name,arn:InsightArn}' --output text --region=$region
```
## Get all custom insights results
```
aws securityhub get-insight-results \
    --insight-arn $customarn --region=$region
```
