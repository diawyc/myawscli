## Create a stacksets in Organization
### Set Parameter
```
region=us-east-1
accid=
stacksetname=SSMAutomationrole
template=automationExecutionRole.yaml
s3name=
runbookname=
```
### from a local file
```
aws cloudformation create-stack-set \
    --stack-set-name $stacksetname\
    --template-body file://$template \
    --parameters \
    ParameterKey=InstallOverrideListBucket,ParameterValue=$s3name  \
    ParameterKey=DelegatedAdministratorAccountId,ParameterValue=$accid \
    ParameterKey=AutomationRunPatchBaselineRunbook,ParameterValue=$runbookname \
    --capabilities CAPABILITY_IAM \
    --region=$region
```
