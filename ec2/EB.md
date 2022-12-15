# Elastic Beanstalk
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```

## list all active application in all regions
```
for region in $regions; do
echo $region
aws elasticbeanstalk describe-applications --region=$region  --query 'Applications[].ApplicationName' --output table
done
```
##删除所有applications

```
for region in $regions; do
echo $region
appnames=($(aws elasticbeanstalk describe-applications --region=$region  --query 'Applications[].ApplicationName' --output text))
len=${#appnames[*]}
echo $len
for ((i=1; i<=len; i++));do
echo $appnames[i]
aws elasticbeanstalk delete-application --application-name $appnames[i] --region=$region --terminate-env-by-force 
done
done
```
# Load Balancer
## list all elb in all regions
```
for region in $regions; do
echo $region
aws elb describe-load-balancers --region=$region  
done
```
--query 'Applications[].ApplicationName' --output table
