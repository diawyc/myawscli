# Alarm
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```

## list all current metric alarms in all regions
```
for region in $regions; do
echo $region
aws cloudwatch describe-alarms  --region=$region  --query 'MetricAlarms[]' --output table
done
```
