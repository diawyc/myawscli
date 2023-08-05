# [Lab 6: Create a launch Template](https://catalog.us-east-1.prod.workshops.aws/workshops/3de93ad5-ebbe-4258-b977-b45cdfe661f1/en-US/application/lab6)

## security group

```
sgname='WP Wordpress SG'
port=80
des='Wordpress server security group'
```
```
groupid=$(aws ec2 create-security-group --group-name $sgname --description $des --vpc-id $vpcid --query 'GroupId' --output text)
echo $groupid
aws ec2 authorize-security-group-ingress \
    --group-id $groupid \
    --protocol tcp \
    --port $port \
    --source-group $sourcesg
```
## make image
```
imageid ='ami-06e0ce9d3339cb039'
num=1
type='t2.micro'
```
```
aws ec2 run-instances \
--image-id $imageid \
--count $num \
--instance-type $type \
--security-group-ids $dbsg $fssg $cachesg\
--subnet-id $appsub1
```



user data edit

```
#!/bin/bash

DB_NAME="wordpress"
DB_USERNAME="wpadmin"
DB_PASSWORD=""
DB_HOST="wordpress-workshop.cluster-ctdnyvvewl6s.eu-west-1.rds.amazonaws.com"

yum update -y

#install apache server 
yum install -y httpd

#install php
amazon-linux-extras enable php7.4
yum clean metadata 
yum install php php-devel
amazon-linux-extras install -y php7.4
systemctl start httpd
systemctl enable httpd

#install wordpress
cd /var/www
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
cp wordpress/wp-config-sample.php wordpress/wp-config.php

#change wp-config with DB details
cp -r wordpress/* /var/www/html/
sed -i "s/database_name_here/$DB_NAME/g" /var/www/html/wp-config.php
sed -i "s/username_here/$DB_USERNAME/g" /var/www/html/wp-config.php
sed -i "s/password_here/$DB_PASSWORD/g" /var/www/html/wp-config.php
sed -i "s/localhost/$DB_HOST/g" /var/www/html/wp-config.php
### keys update

#change httpd.conf file to allowoverride
#  enable .htaccess files in Apache config using sed command
sudo sed -i '/<Directory "\/var\/www\/html">/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/httpd/conf/httpd.conf

# Change OWNER and permission of directory /var/www
chown -R apache /var/www
chgrp -R apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php

systemctl restart httpd
systemctl enable httpd
systemctl start httpd




```


## Launch Template
```
name='wordpress-lt'
ImageId=ami-06e0ce9d3339cb039
instancerole name:workshopec2role
```

```
lt=$(aws ec2 create-launch-template \
    --launch-template-name $name \
    --version-description WebVersion1 \
    --launch-template-data '{"IamInstanceProfile": {"Name": "workshopec2role"},"NetworkInterfaces":[{"DeviceIndex":0,"Groups":["sg-084acd7997e0276f3"]}],"ImageId":"ami-0ad640263352b6473","InstanceType":"t2.small"}' \
    --query 'LaunchTemplate.LaunchTemplateId' --output text)
echo $lt
```
## Auto Scaling
```
name='WebTierAsg'
```
```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name $name \
    --launch-template LaunchTemplateId=$lt \
    --target-group-arns $tgarn\
    --health-check-type ELB \
    --health-check-grace-period 600 \
    --min-size 2 \
    --max-size 2 \
    --vpc-zone-identifier $sub1,$sub2
```

## Get Web LB DNS NAME in webbrowser
```
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,DNSName]' --output table
```

![如图](webpage.png)
