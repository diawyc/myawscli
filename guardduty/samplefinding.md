#create sample finding

https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateSampleFindings.html

```
region=cn-north-1
```
## create all samples
```
aws guardduty create-sample-findings \
    --detector-id  $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)
```
## create chosen ones
```
aws guardduty create-sample-findings \
    --detector-id  $(aws guardduty list-detectors --output text --query 'DetectorIds'  --region=$region)  \
    --finding-types \
	Persistence:IAMUser/AnomalousBehavior \
	PrivilegeEscalation:IAMUser/AnomalousBehavior \
	InitialAccess:IAMUser/AnomalousBehavior \
  --region=$region
  ```
加上双引号更准确
```
aws guardduty create-sample-findings \
    --detector-id  $(aws guardduty list-detectors --output text --query 'DetectorIds'  --region=$region)  \
    --finding-types \
        "Backdoor:EC2/C&CActivity.B"\
        "Impact:EC2/MaliciousDomainRequest.Reputation" \  
        "Impact:EC2/MaliciousDomainRequest.Reputation" \
  --region=$region
```
