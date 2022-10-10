参数设置Set Parameter:
```
region=me-central-1
adminid=$(aws guardduty list-organization-admin-accounts --region=$region)
```
## Guardduty
指定管理员账户Set a delegated admin account for Guardduty:
```
aws guardduty create-detector --data-sources   S3Logs={Enable=true} --enable --finding-publishing-frequency FIFTEEN_MINUTES --region=$region
AWS  guardduty enable-organization-admin-account --admin-account-id=$adminid --region=$region 
```
