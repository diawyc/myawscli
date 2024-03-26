## install on my mac
```
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac_arm64/session-manager-plugin.pkg" -o "session-manager-plugin.pkg"
```

```
sudo installer -pkg session-manager-plugin.pkg -target /
sudo ln -s /usr/local/sessionmanagerplugin/bin/session-manager-plugin /usr/local/bin/session-manager-plugin
```


```
session-manager-plugin
```
```
aws ssm start-session --target $id --region=$region
```
## create three vpc endpoint
```
service='com.amazonaws.cn-north-1.ssm'
type='Interface'
vpcid='vpc-003715ce49b2f6846'
subnet='subnet-0331e3311fa8b7cfe'
10.0.0.0/16
sg='sg-036b311429333a646'

```
```
aws ec2 create-vpc-endpoint \
    --service-name $service \
    --vpc-endpoint-type $type \
    --vpc-id $vpcid \
    --subnet-ids $subnet --region=$region
```
