# [Config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice)

## parameter
名称是区分大小写的
```
packname=cliEc2app
templatename='TestConformancePack.yaml'
region=us-east-1
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```

## create a conformance pack
```
packarn=$(aws configservice put-conformance-pack \
--conformance-pack-name $packname \
--template-body file://$templatename \
--region=$region --query 'ConformancePackArn' --output text)
```
## delete a conformance pack
## 查询所有或一个pack
```
packname=($(aws configservice describe-conformance-packs --region=$region --query 'ConformancePackDetails[*].ConformancePackName' --output text))
```
## 查看所有region的所有一致性包
```
for region in $regions; do
echo $region
aws configservice describe-conformance-packs --region=$region --no-cli-pager
done

```
