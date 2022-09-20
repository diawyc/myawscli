# Securityhub

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


