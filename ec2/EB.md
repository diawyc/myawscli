
aws elasticbeanstalk delete-application --application-name my-app
## list all active application in all regions
```
for region in $regions; do
echo $region
aws elasticbeanstalk describe-applications --region=$region  --query 'Applications[].ApplicationName' --output table
echo $ids
done
```
##删除所有applications

```
for region in $regions; do
echo $region
appnames=($(aws elasticbeanstalk describe-applications --region=$region  --query 'Applications[].ApplicationName' --output table))
echo $ids
done
```
