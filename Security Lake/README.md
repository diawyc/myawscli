# I love aws cli

## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
```
regions=(eu-west-1 us-east-1)
```
### 不换页
```
--no-cli-pager
```

## [在多region开启](https://docs.aws.amazon.com/ja_jp/cli/latest/reference/securitylake/create-datalake.html)
```
aws securitylake create-datalake --regions $regions[1] $regions[2]
```


## 
```
adminlist=($(aws organizations list-delegated-administrators --no-cli-pager --query 'DelegatedAdministrators[].Id' --output text))
echo $adminlist
```
## [list admin's service](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-delegated-services-for-account.html)
```
services=($(aws organizations list-delegated-services-for-account --account-id $adminlist[1] --query 'DelegatedServices[].ServicePrincipal' --output text))
echo $services
```

## [de-register delegated admin account for each service](https://docs.aws.amazon.com/cli/latest/reference/organizations/deregister-delegated-administrator.html)

```
len=${#services[*]}
echo $len
admin=$adminlist[1]
```

```
for ((i=1; i<=len; i++));do
aws organizations deregister-delegated-administrator \
--account-id $admin \
--service-principal $services[i]
echo $services[i]
done
```
可以把adminlist再加一个遍历
## [remove account from org](https://docs.aws.amazon.com/cli/latest/reference/organizations/remove-account-from-organization.html)
```
aws organizations remove-account-from-organization --account-id $admin

```
## invite an account
```
accid=
```
```
aws organizations invite-account-to-organization \
--target Id=$accid,Type=ACCOUNT

```
