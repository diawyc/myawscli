
## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=cn-north-1))
echo ${#regions[*]}
name=default
```
```
aws backup describe-backup-vault --backup-vault-name $name --region=$region
```
```
aws backup list-recovery-points-by-backup-vault --backup-vault-name $name --region--region=$region
```
