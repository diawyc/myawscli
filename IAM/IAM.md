arn=$(aws iam create-user --user-name=$username --query 'User.Arn' --output text)
