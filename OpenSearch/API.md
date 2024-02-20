# console API
## update role mapping
```
PUT _plugins/_security/api/rolesmapping/security_manager
{
  "backend_roles" : [ ],
  "hosts" : [  ],
  "users" : ["user1",
      "user2" ]
}
```
## clear a role mapping
```

PUT _plugins/_security/api/rolesmapping/manage_snapshots
{
  "backend_roles" : [ ],
  "hosts" : [  ],
  "users" : [ ]
}

```
## create a user
https://opensearch.org/docs/latest/security/access-control/api/#get-user

```
GET _plugins/_security/api/internalusers/jessica
```
这个role不好使
```
PUT _plugins/_security/api/internalusers/<username>
{
  "hash": "",
  "opendistro_security_roles": ["security_manager"],
  "backend_roles": [],
    "attributes": {
      "company": "ghac"
    }
}
```

## create a role
```
PUT _plugins/_security/api/roles/lambda-role
{
  "cluster_permissions": [
    "indices:data/write/bulk*"
  ],
  "index_permissions": [{
    "index_patterns": [
      "gb*","db*","error*"
    ],
    "dls": "",
    "fls": [],
    "masked_fields": [],
    "allowed_actions": [
      "create_index","data_access"]
  }],
  "tenant_permissions": []
```
## create a index and input data
```
PUT test-gb-result/_doc/1
{
   "campaignId":"ZZ18010001002",
   "VIN车辆识别码":"LHGGK5754F20891762"
}
```
## create new index with custome shards
```
PUT sample-data-1-1
{
  "settings": {
  "index": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
  }
}
```
## create custom snapshot repository

## bulk create doc for index

```
POST /_bulk
{ "create" : { "_index" : "test", "_id" : "1" ,"_shards":2  } }
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
```
POST /_bulk
{ "create" : { "_index" : "veggies", "_id" : "1"  } }
{"datetimeCreated": "2024/01/11 10:23:35" }
{ "create" : { "_index" : "veggies", "_id" : "2" } }
{"datetimeCreated": "2024/01/11 10:23:35" }
{ "create" : { "_index" : "veggies", "_id" : "3" } }
{"campaignId": "ZZ18010001003","sessionID": "ZZ18010001003","VIN车辆识别码": "LVHTG6877H5000057"}
{ "create" : { "_index" : "veggies"} }
{"campaignId": "ZZ18010001004","sessionID": "ZZ18010001004","VIN车辆识别码": "LVHTG6877H5000125"}
{ "create" : { "_index" : "veggies"} }
{"campaignId": "ZZ18010001001","sessionID": "ZZ18010001001","VIN车辆识别码": "LVHTG6877H5000037"}
```
```
"_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        }
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
## 创建一个自动的SM policy
```
POST _plugins/_sm/policies/dr-auto-snapshot
{
        
        "description": "auto snapshot for dr recovery",
        "creation": {
          "schedule": {
            "cron": {
              "expression": "0 20 * * *",
              "timezone": "Asia/Singapore"
            }
          }
        },
        "deletion": {
          "schedule": {
            "cron": {
              "expression": "0 20 * * *",
              "timezone": "Asia/Singapore"
            }
          },
          "condition": {
            "min_count": 1,
            "max_count": 400
          }
        },
        "snapshot_config": {
          "indices": "*",
          "ignore_unavailable": true,
          "repository": "dr-snapshot-repo",
          "partial": true
        }

}
```
## 查看SM policy内容
```
GET _plugins/_sm/policies
```
