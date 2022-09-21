## Create a stacksets in Organization Service Managed
https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack-set.html
### Set Parameter
```
region=us-east-1
accid=295158943844
stacksetname=SSMAutomationrole
stacksettemplate=automationExecutionRole.yaml
s3name=
runbookname=
```
### from a local file
```
rootid=
regions=
```
```
aws cloudformation create-stack-set \
    --stack-set-name $stacksetname\
    --template-body file://$stacksettemplate \
    --permission-model SERVICE_MANAGED \
    --auto-deployment Enabled=true,RetainStacksOnAccountRemoval=true \
    --parameters \
    ParameterKey=InstallOverrideListBucket,ParameterValue=$s3name  \
    ParameterKey=DelegatedAdministratorAccountId,ParameterValue=$accid \
    ParameterKey=AutomationRunPatchBaselineRunbook,ParameterValue=$runbookname \
    --capabilities CAPABILITY_NAMED_IAM \
    --region=$region
```
to all accounts with one region
```
aws cloudformation create-stack-instances \
    --stack-set-name $stacksetname\
    --deployment-targets OrganizationalUnitIds=$rootid --regions $region \            
    --region=$region
```
### Delete stacks
```
aws cloudformation delete-stack-instances \
    --stack-set-name $stacksetname\
    --deployment-targets OrganizationalUnitIds=$rootid --regions us-east-1 eu-west-2 \
    --region=$region --no-retain-stacks
```
