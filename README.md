# I love aws cli

### 不换页
```
--no-cli-pager
```
## sns
```
region=eu-west-2
arn='arn:aws:sns:eu-west-2:883600840440:SecurityHubAnnouncements'
```

```
aws  sns --region $region subscribe --topic-arn $arn --protocol email --notification-endpoint 36256586@qq.com
```
## get Organizations ID
```
aws organizations describe-organization  --query 'Organization.Id' --output text --region=$region))
```
