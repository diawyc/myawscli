```
name='prodkey1'
des='used for ota prod api with smc'
```
```
aws apigateway create-api-key --name $name --description $des --enabled --query 'value' --output text
```
