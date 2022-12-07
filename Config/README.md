# [Config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice)
## 关闭config
### [delete delivery](https://docs.aws.amazon.com/cli/latest/reference/configservice/delete-delivery-channel.html）

```
name=
```
```
aws configservice delete-delivery-channel --delivery-channel-name $name
```


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
```
aws configservice delete-conformance-pack \
--conformance-pack-name $packname --region=$region 
```

## 查询所有pack 将name放进一个数组
```
packnames=($(aws configservice describe-conformance-packs --region=$region --query 'ConformancePackDetails[*].ConformancePackName' --output text))
```
## 查看所有region的所有一致性包
```
for region in $regions; do
echo $region
aws configservice describe-conformance-packs --region=$region --no-cli-pager
done

```
