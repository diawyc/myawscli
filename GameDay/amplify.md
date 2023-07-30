https://aws.amazon.com/cn/getting-started/hands-on/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/module-1/
## create codecommit repository
```
region=us-east-1
reponame=wildrydes-site
```

```
aws codecommit create-repository --repository-name $reponame --query 'repositoryMetadata.Arn' --output text --region=$region
```
