# create a new repository from codecommit

```
region=us-east-1
reponame=mytestrepository
```
```
aws codecommit create-repository --repository-name $reponame --query 'repositoryMetadata.Arn' --output text --region=$region
```
