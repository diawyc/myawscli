# Enable with Orgs
## 参数设置Set Parameter:
```
region=me-central-1
adminid=$(aws guardduty list-organization-admin-accounts --region=$region --query 'AdminAccounts[*].AdminAccountId' --output text)
echo $adminid
admemail=$(aws organizations describe-account --account-id $adminid --region=$region --query 'Account.Email' --output text)
echo $admemail
```

## 指定管理员账户Set a delegated admin account for Guardduty:

```
aws guardduty enable-organization-admin-account --admin-account-id=$adminid --region=$region 
```
## Enable for all memeber accounts
```
orgids=($(aws organizations list-accounts  --query 'Accounts[*].Id' --output text ))
accountids=( ${orgids[*]/$adminid} )
orgemails=($(aws organizations list-accounts  --query 'Accounts[*].Email' --output text ))
accountemails=(${orgemails[*]/$admemail})
len=${#accountids[*]}
echo $len
```
## 缺少k8s malware的配置，需要补充
```
for ((i=1; i<=len; i++));do
echo $accountids[i] $accountemails[i]
aws guardduty create-members --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)  --account-details AccountId=$accountids[i],Email=$accountemails[i]  --region=$region
aws guardduty update-detector --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region) --data-sources   S3Logs={Enable=true} --enable --finding-publishing-frequency FIFTEEN_MINUTES --region=$region
aws guardduty update-organization-configuration --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)   --auto-enable --data-sources S3Logs={AutoEnable=true} --region=$region
done
```
必须要一个一个开S3，好奇怪的命令。

# [导出到S3](https://docs.aws.amazon.com/cli/latest/reference/guardduty/create-publishing-destination.html)
## 参数设置
```
s3arn='arn:aws:s3:::aes-siem-295158943844-log'
kms='arn:aws:kms:eu-west-2:295158943844:key/d61c289f-c35e-4b73-a809-6d42378599e2'
```
## CLI command

```
for region in $regions; do
echo $region
aws guardduty create-publishing-destination \
    --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)   \
    --destination-type S3 \
    --destination-properties DestinationArn=$s3arn,KmsKeyArn=$kms --region=$region
done
```
