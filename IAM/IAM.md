## create user

```
username='brclient'
policyname='BRClient-Policy'
filename='policy.json'
region='us-east-1'
```
```
arn=$(aws iam create-user --user-name=$username --query 'User.Arn' --output text --region=$region)
policyarn=$(aws iam create-policy --policy-name $policyname --policy-document file://$filename --region=$region --quer 'Policy.Arn' --output text)
aws iam attach-user-policy --user-name $username --policy-arn $policyarn --region=$region
aws iam create-access-key --user-name $username --region=$region --query 'AccessKey.[AccessKeyId,SecretAccessKey]' --output table

```


## get a custom policy content
```
aws iam get-role-policy \
    --role-name $rolename \
    --policy-name $policyname

```
## list SSO role in an account
```

aws iam list-roles --quer 'Roles[?RoleName<=`AWSReservedSSO_o`].Arn' --output table
```
## 为user配置 assume role权限
[permission sample](assume-role.json)


create a policy
```
username='smc001'
policyname='pbforsmc'
filename='pbforsmc.json'
```
```
policyarn=$(aws iam create-policy \    
    --policy-name $policyname \       
    --policy-document file://$filename --quer 'Policy[].Arn' --output text)
```
```
aws iam list-policies --scope Local 
```
```
aws iam put-user-permissions-boundary \
    --permissions-boundary $policyarn\
    --user-name $username


```
## user to assume role
```
username='smc001'
aws iam list-user-policies --user-name $username
```
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
## list all roles by names

```
aws iam list-roles --quer 'Roles[].RoleName' --output table
```
## list all roles by assume role principal
```

aws iam list-roles --quer 'Roles[].[RoleName,AssumeRolePolicyDocument.Statement[].Principal.AWS]' --output json
```
## list role policy
```
aws iam list-attached-role-policies --role-name $rolename
aws iam list-role-policies \
    --role-name $rolename
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
## [with local policy files to create inline policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html)

```

aws iam put-role-policy --role-name=$rolename --policy-name $policyname --policy-document file://$rolepolicyfile
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
## get group policy
### parameter
```
groupname=
policyname
```

```
aws iam get-group-policy --group-name $groupname --policy-name $policyname
```
