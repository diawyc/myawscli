# I love aws cli

## 查看所有regions中lambda functions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```

```
for region in $regions; do
echo $region
aws lambda list-functions  --region=$region --no-cli-pager
done
```
