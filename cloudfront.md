
Depracated
```
number=2022
des=fors3web
```

```
id=$(aws cloudfront create-cloud-front-origin-access-identity \
       --cloud-front-origin-access-identity-config \
       CallerReference=$number,Comment=$des --query 'CloudFrontOriginAccessIdentity.Id' --output text)
echo $id
```
