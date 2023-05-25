## pass role
```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "iam:GetRole",
            "iam:PassRole"
        ],
        "Resource": "arn:aws-cn:iam::043378916688:role/*"
    }]
}
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
