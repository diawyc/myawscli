## 参数设置Set Parameter:
```
region=me-central-1
adminid=$(aws guardduty list-organization-admin-accounts --region=$region --query 'AdminAccounts[*].AdminAccountId' --output text)
echo $adminid
admemail=$(aws organizations describe-account --account-id $adminid --region=$region --query 'Account.Email' --output text)
echo $admemail
```

指定管理员账户Set a delegated admin account for Guardduty:

```
aws guardduty enable-organization-admin-account --admin-account-id=$adminid --region=$region 
```

```
orgids=($(aws organizations list-accounts  --query 'Accounts[*].Id' --output text ))
accountids=( ${orgids[*]/$adminid} )
orgemails=($(aws organizations list-accounts  --query 'Accounts[*].Email' --output text ))
accountemails=(${orgemails[*]/$admemail})
len=${#accountids[*]}
echo $len
```
```
for ((i=1; i<=len; i++));do
echo $accountids[i] $accountemails[i]
aws guardduty create-members --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)  --account-details AccountId=$accountids[i],Email=$accountemails[i]  --region=$region
aws guardduty update-detector --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region) --data-sources   S3Logs={Enable=true} --enable --finding-publishing-frequency FIFTEEN_MINUTES --region=$region
aws guardduty update-organization-configuration --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)   --auto-enable --data-sources S3Logs={AutoEnable=true} --region=$region
done
```
