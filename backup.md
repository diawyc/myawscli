
## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=cn-north-1))
echo ${#regions[*]}
name=default
```
```
aws backup describe-backup-vault --backup-vault-name $name --region=$region
```
## 得到所有vault name
```
names=($(aws backup list-backup-vaults --region=$region --query 'BackupVaultList[].BackupVaultName[]' --output text))
len=${#names[*]}
echo $len
```

## 得到所有文件ARN
```
rps=($(aws backup list-recovery-points-by-backup-vault --backup-vault-name $name --region=$region --query 'RecoveryPoints[].RecoveryPointArn[]' --output text))
len=${#rps[*]}
echo $len
```
## 删除一个vault里所有recovery point
```
for ((i=1; i<=len; i++));do
aws backup delete-recovery-point --backup-vault-name $name --recovery-point-arn $rp --region=$region
done
```
## 删除所有regions中Default中所有recovery point
```
name=Default
for region in $regions; do
echo $region
rps=($(aws backup list-recovery-points-by-backup-vault --backup-vault-name $name --region=$region --query 'RecoveryPoints[].RecoveryPointArn[]' --output text))
len=${#rps[*]}
echo $len
for ((i=1; i<=len; i++));do
rp=$rps[i]
aws backup delete-recovery-point --backup-vault-name $name --recovery-point-arn $rp --region=$region
echo $i
done
done
```
