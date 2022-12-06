# create a new repository from codecommit
create a new one 并获得arn
```
region=us-east-1
reponame=mytestrepository
```

```
aws codecommit create-repository --repository-name $reponame --query 'repositoryMetadata.Arn' --output text --region=$region
```
列出所有repository
```
aws codecommit list-repositories --region=us-east-1 --query 'repositories[*]' --output text
```
查看一个repo
```
aws codecommit get-repository \
    --repository-name $reponame --region=us-east-1
```
