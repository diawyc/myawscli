# [Batch translation job](https://docs.aws.amazon.com/cli/latest/reference/translate/start-text-translation-job.html))

```
source='s3://jadoc/excel/'
input='s3://jadoc/ppt/'
dest='s3://endoc/'
iamrole='arn:aws:iam::295158943844:role/translateall-DataAccessRole-678VEQ8P4V6U'
scode=ja
tcode=en
```

```
start-text-translation-job \
--input-data-config <value> \
--output-data-config <value> \
--data-access-role-arn $iamrole \
--source-language-code $scode \
--target-language-codes $tcode

```
