## Set parameter参数设置
region为securityhub指定的聚合aggregated region

```
region='eu-west-2'
insight='BackupAlert'
```

## CLI command 
```
aws securityhub create-insight \
--filters \
 '{"RecordState": [{ "Comparison": "EQUALS", "Value": "ACTIVE"}], "WorkflowStatus": [{"Comparison": "EQUALS", "Value": "NEW"}], "ProductName": [{"Comparison": "EQUALS", "Value": "Default"}]}' \
 --group-by-attribute "ResourceId" \
--name $insight \
--query 'InsightArn' --output text --region=$region
```
