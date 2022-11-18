# [Config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-conformance-pack.html)

## parameter
```
packname=cliec2app
templatename='TestConformancePack.yaml'
region=use-east-1
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```

## create conformance pack
```
aws configservice put-conformance-pack \
--conformance-pack-name $packname \
--template-body file://$templatename \
--delivery-s3-bucket AmazonS3bucketname \
--region=$region
```
## 查询所有或一个pack
```
aws configservice describe-conformance-packs --conformance-pack-name=$packname --region=$region
```

