## create user
```
arn=$(aws iam create-user --user-name=$username --query 'User.Arn' --output text)
```
## create a role 
### parameter
```
rolename=AWSControlTowerExecution
trustfile=ct-trustpolicy.json
rolepolicyfile=
policyname=AdministratorAccess
```
## get role arn
```
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://$trustfile --query 'Role.Arn' --output text)
```
## [with local policy files](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html)

```

aws iam put-role-policy --role-name=$rolename --policy-name $rolepolicy --policy-document file://$rolepolicyfile
```
## [with managed policy](https://docs.aws.amazon.com/cli/latest/reference/iam/attach-role-policy.html)

```

aws iam attach-role-policy --role-name=$rolename --policy-arn arn:aws:iam::aws:policy/$policyname
```
