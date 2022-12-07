# I love aws cli

## regions
```
regions=($(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text --region=us-east-1))
echo ${#regions[*]}
```
### 不换页
```
--no-cli-pager
```

## get Organizations ID
```
orgid=$(aws organizations describe-organization  --query 'Organization.Id' --output text --region=$region)
echo $orgid
```
## Get all OU Ids
```
orgunits=($(aws organizations list-organizational-units-for-parent --parent-id $(aws organizations list-roots --query "Roots[].Id" --output text)  --query "OrganizationalUnits[*].Id" --output text))
echo ${#orgunits[*]}
```
```
rootid=$(aws organizations list-roots --query "Roots[].Id" --output text)
```
## Get all admin account id and email
```
aws organizations list-delegated-administrators --region=$region 
```


## [list all delegated admin ](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-delegated-administrators.html)
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
adminid=
service=
```

```
aws organizations deregister-delegated-administrator \
--account-id $adminid \
--service-principal $service
```
