## Create a stacksets in Organization Service Managed
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
orgunits=
regions=
```
```
aws cloudformation create-stack-set \
    --stack-set-name $stacksetname\
    --template-body file://$stacksettemplate \
    --permission-model SERVICE_MANAGED \
    --auto-deployment Enabled=true,RetainStacksOnAccountRemoval=true
    --parameters \
    ParameterKey=InstallOverrideListBucket,ParameterValue=$s3name  \
    ParameterKey=DelegatedAdministratorAccountId,ParameterValue=$accid \
    ParameterKey=AutomationRunPatchBaselineRunbook,ParameterValue=$runbookname \
    --capabilities CAPABILITY_IAM \
    --region=$region
```
```
aws cloudformation create-stack-instances \
    --stack-set-name $stacksetname\
    --deployment-targets OrganizationalUnitIds=$orgunits \
    --regions $regions \
    --region=$region

```
