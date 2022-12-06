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
```
```
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file:$trustfile --query 'Role.Arn' --output text)
aws iam put-role-policy --role-name=$rolename --policy-name $rolepolicy --policy-document file://$rolepolicyfile
```
