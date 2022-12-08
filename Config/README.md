# [Config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice)
## 查看config是否开启
```
for region in $regions; do
echo $region
aws configservice  describe-configuration-recorder-status --region=$region
done
```

## 开启config的三步
### put-configuration-recorder
put-delivery-channel
start-configuration-recorder
```
role=arn:aws:iam::123456789012:role/config-role
```

```
aws configservice put-configuration-recorder --configuration-recorder name=default,roleARN=$role \
--recording-group \
allSupported=true,includeGlobalResourceTypes=true \
--region=$region
```
```
aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json --region=$region
```
```
aws configservice start-configuration-recorder --configuration-recorder-name configRecorderName --region=$region
```

## 关闭config的三步
### [delete delivery](https://docs.aws.amazon.com/cli/latest/reference/configservice/delete-delivery-channel.html)
```
aws configservice stop-configuration-recorder --configuration-recorder-name default --region=$region
aws configservice delete-delivery-channel --delivery-channel-name default --region=$region
aws configservice \
delete-configuration-recorder \
--configuration-recorder-name default --region=$region
```
```
for region in $regions; do
echo $region
aws configservice stop-configuration-recorder --configuration-recorder-name default --region=$region
aws configservice delete-delivery-channel --delivery-channel-name default --region=$region
aws configservice \
delete-configuration-recorder \
--configuration-recorder-name default --region=$region
done

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
