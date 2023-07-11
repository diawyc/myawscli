# AWS Translate
## list all jobs

```
aws translate list-text-translation-jobs
```

## [Batch translation job](https://docs.aws.amazon.com/cli/latest/reference/translate/start-text-translation-job.html)

```
## ='s3://jadoc/excel/'
input='s3://jadoc/ppt/'
filename=''
```

```
aws s3 cp $filename s3://$input/
```
```
aws s3 cp $filename  s3://$input/ --recursive
```

```
output='s3://endoc/'
type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
type='application/vnd.openxmlformats-officedocument.presentationml.presentation'
iamrole='arn:aws:iam::295158943844:role/translateall-DataAccessRole-678VEQ8P4V6U'
scode=ja
tcode=en

```

```
start-text-translation-job \
--input-data-config S3Uri=$input,ContentType=$type \
--output-data-config S3Uri=$output \
--data-access-role-arn $iamrole \
--source-language-code $scode \
--target-language-codes $tcode

```
