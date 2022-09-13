## create Threatlist
```
for region in $regions; do

aws guardduty create-threat-intel-set \

    --detector-id $(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)  \

    --name $threatset \

    --format TXT \

    --location $tiurl\

    --activate --region=$region

done
```

## update Threatlist
```
for region in $regions; do
did=$(aws guardduty list-detectors --output text --query 'DetectorIds' --region=$region)
tid=$(aws guardduty list-threat-intel-sets \
--detector-id=$(aws guardduty list-detectors --output text --query 'DetectorIds' \
--region=$region)  --region=$region --output text --query 'ThreatIntelSetIds' )
aws guardduty update-threat-intel-set --detector-id=$did --threat-intel-set-id=$tid --activate --region=$region
echo $region
done
```
