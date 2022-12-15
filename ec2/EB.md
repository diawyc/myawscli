
aws elasticbeanstalk delete-application --application-name my-app
## list all active application in all regions
```
for region in $regions; do
echo $region
aws elasticbeanstalk describe-applications --region=$region  --query 'Applications[].ApplicationName' --output table
echo $ids
done
```

