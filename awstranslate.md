# AWS Translate
## list all jobs

```
aws translate list-text-translation-jobs
```
文件夹名字是excel/ppt,上传里边所有的文件
```
aws s3 cp $filename $input --recursive
```

## [Batch translation job](https://docs.aws.amazon.com/cli/latest/reference/translate/start-text-translation-job.html)


### excel
```
input='s3://jadoc/excel/'
filename='Desktop/excel'
jobname='exceljob'
type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
```

### ppt

```
input='s3://jadoc/ppt/'
filename='Desktop/ppt'
type='application/vnd.openxmlformats-officedocument.presentationml.presentation'
jobname='pptjob'
```
### word
```
input='s3://jadoc/word/'
filename='Desktop/word'
type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
jobname='wordjob'
```
### html
```
input='s3://jadoc/html/'
filename='Desktop/html'
type='text/html'
jobname='htmljob'
```

### translate job
```
output='s3://endoc/'
localfolder=en
iamrole='arn:aws:iam::295158943844:role/translateall-DataAccessRole-678VEQ8P4V6U'
scode=ja
tcode=en

```
```
aws translate start-text-translation-job --job-name $jobname \
--input-data-config S3Uri=$input,ContentType=$type \
--output-data-config S3Uri=$output \
--data-access-role-arn $iamrole \
--source-language-code $scode \
--target-language-codes $tcode

```
### download files


```
aws s3 sync $output $localfolder
```
