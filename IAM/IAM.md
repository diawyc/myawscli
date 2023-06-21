## user to assume role
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html
```
rolearn='arn:aws-cn:iam::337075903349:role/adminrole'
sessionname=test
```
```
aws sts assume-role --role-arn $rolearn --role-session-name $sessionname
```

## create user
```
arn=$(aws iam create-user --user-name=$username --query 'User.Arn' --output text)
```
## create a role 
### parameter
```
rolename=ManhitachilLimitedAdmin
trustfile=trustpolicy.json
rolepolicyfile=ManAdmin.json
policyname=AdministratorAccess
```
##  create role and get arn
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
把role变成ec2 instance profile, 同一个role会出现两个ARN，才能被ec2使用
```
aws iam create-instance-profile --instance-profile-name $rolename
aws iam add-role-to-instance-profile --role-name $rolename --instance-profile-name $rolename
```
## get role arn
```
 aws iam get-role --role-name $rolename --query 'Role.Arn' --output text
```
## get policy
### parameter
```
groupname=
policyname
```

```
aws iam get-group-policy --group-name $groupname --policy-name $policyname
```
