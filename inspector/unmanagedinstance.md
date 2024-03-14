# Inspector
## Enable multi-account
https://github.com/aws-samples/inspector2-enablement-with-cli

## check each region's number of unmanaged ec2
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text))
```
```
for region in $regions;do
echo $region
aws inspector2 \
list-coverage-statistics \
--group-by SCAN_STATUS_CODE \
--filter-criteria \
'resourceType=[{comparison=EQUALS,value=AWS_EC2_INSTANCE}]'  \
--region=$region \
--query 'countsByGroup[1].[groupKey,count]' --output text
done

```
