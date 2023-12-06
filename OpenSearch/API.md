# console API

## create a index and input data
```
PUT test-gb-result/_doc/1
{
   "campaignId":"ZZ18010001002",
   "VIN车辆识别码":"LHGGK5754F20891762"
}
```
## create custom snapshot repository

## bulk create doc for index

```
POST /_bulk
{ "create" : { "_index" : "veggies", "_id" : "1"  } }
{"campaignId": "ZZ18010001001","sessionID": "ZZ18010001001","VIN车辆识别码": "LVHTG6877H5000035" }
{ "create" : { "_index" : "veggies", "_id" : "2" } }
{"campaignId": "ZZ18010001002","sessionID": "ZZ18010001002","VIN车辆识别码": "LVHTG6877H5000047"}
{ "create" : { "_index" : "veggies", "_id" : "3" } }
{"campaignId": "ZZ18010001003","sessionID": "ZZ18010001003","VIN车辆识别码": "LVHTG6877H5000057"}
{ "create" : { "_index" : "veggies"} }
{"campaignId": "ZZ18010001004","sessionID": "ZZ18010001004","VIN车辆识别码": "LVHTG6877H5000125"}
{ "create" : { "_index" : "veggies"} }
{"campaignId": "ZZ18010001001","sessionID": "ZZ18010001001","VIN车辆识别码": "LVHTG6877H5000037"}
```

## create a snapshot
```
PUT _snapshot/dr-snapshot-repo/4
```
```
GET _snapshot/dr-snapshot-repo/_all

```
```
GET _snapshot/_status
```
