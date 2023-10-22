## 部署S3
```
bucketregion=cn-northwest-1
bucketname='lvliserver-info'
filename=‘mapping.json’
aws s3 cp $filename s3://$bucketname/ --region=$bucketregion
```

