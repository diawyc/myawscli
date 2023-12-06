```
name='prodkey1'
des='used for ota prod api with smc'
```
```
aws apigateway create-api-key --name $name --description $des --enabled --query 'value' --output text
```
```
aws apigateway get-rest-apis --query 'items[?name==`ota-23my-st-apigw-omc_access_front`].[id,name]' --output table
```
```
aws apigateway get-rest-api --rest-api-id $id
```

```
id=$(aws apigateway get-rest-apis --query 'items[?name==`ota-23my-stg-apigw-omc_access_front`].id' --output text) 

```
