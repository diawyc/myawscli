# Organizations
```
adminid=$(aws securityhub list-organization-admin-accounts --region=$region --output text --query 'AdminAccounts[*].AccountId') 

```
