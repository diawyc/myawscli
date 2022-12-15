

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
appnames=($(aws elasticbeanstalk describe-applications --region=$region  --query 'Applications[].ApplicationName' --output text))
len=${#appnames[*]}
echo $len
for ((i=1; i<=len; i++));do
echo $appnames[i]
aws elasticbeanstalk delete-application --application-name $appnames[i]
done
done
```
