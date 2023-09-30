#  AOS domain

## create a domain

```
name='dr-domain'
engine='OpenSearch_2.7'
ec2type='c5.large.search'
ec2num=1
ebstype='gp3'
ebssize=20
region='cn-north-1'
```

```
aws opensearch create-domain \
  --domain-name $name\
  --engine-version $engine \
  --cluster-config InstanceType=$ec2type,InstanceCount=$ec2num \
  --ebs-options EBSEnabled=true,VolumeType=$ebstype,VolumeSize=$ebssize \
  --node-to-node-encryption-options Enabled=true \
  --encryption-at-rest-options Enabled=true \
  --domain-endpoint-options EnforceHTTPS=true,TLSSecurityPolicy=Policy-Min-TLS-1-2-2019-07 \
  --advanced-security-options Enabled=true,InternalUserDatabaseEnabled=true,MasterUserOptions='{MasterUserName=jessica,MasterUserPassword=Aws}' \
  --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":["*"]},"Action":["es:ESHttp*"],"Resource":"arn:aws-cn:es:cn-northwest-1:123456789012:domain/migration-domain/*"}]}' \
  --region $region
```