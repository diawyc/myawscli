# Part 0
### S3 Bucket Creation
```
bucketregion=cn-northwest-1
bucketname=workshopcode2023
filename=
```
```
aws s3api create-bucket \
    --bucket $bucketname \
    --region $bucketregion \
    --create-bucket-configuration LocationConstraint=$bucketregion
```

### IAM EC2 Instance Role Creation
```
rolename=workshopec2role
trustfile=trustpolicy-service.json

```

```
rolearn=$(aws iam create-role --role-name $rolename --assume-role-policy-document file://$trustfile --query 'Role.Arn' --output text)
echo $rolearn

```
```
policyname=AmazonSSMManagedInstanceCore
aws iam attach-role-policy --role-name=$rolename --policy-arn arn:aws-cn:iam::aws:policy/$policyname
policyname=AmazonS3ReadOnlyAccess
aws iam attach-role-policy --role-name=$rolename --policy-arn arn:aws-cn:iam::aws:policy/$policyname
aws iam list-attached-role-policies --role-name=$rolename
```
[back to table of content](readme.md)
