# Securityhub
From this blog, 
https://aws.amazon.com/blogs/mt/automate-vulnerability-management-and-remediation-in-aws-using-amazon-inspector-and-aws-systems-manager-part-1/
Step 1: Create Security Hub custom actions for resolving Amazon Inspector Findings
I change the manual work part to create custom action buttons into below CLI command. 
Easier to copy and paste
## create custom action
-----------------------------------------------------------------------
## Set parameter参数设置
region为securityhub指定的聚合aggregated region
```
region='eu-west-2'
buttonnames=('Rem-Inspector-NoRBT' 'Rem-Inspector-RBT')
actionids=('InspectorRemNoRBT' 'InspectorRemRBT')
```

## CLI command 
```
for ((i=1; i<=${#buttonnames[@]}; i++));do
arn=$(aws securityhub create-action-target \
    --name $buttonnames[$i]\
    --description $buttonnames[$i] \
    --id $actionids[$i] --region=$region  --output text --query 'ActionTargetArn')
echo $arn
arnlist[i]=$arn
done
echo $arnlist
```


