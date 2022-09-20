## Create a stacksets in Organization
### Set Parameter
```
region=us-east-1
adminid=
stacksetname=SSMAutomationrole
template=automationExecutionRole.yaml

```
### from a local file
```
aws cloudformation create-stack-set \
    --stack-set-name $stacksetname\
    --template-body file://$template \
    --region=$region
```
