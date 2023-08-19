# AWS Translate


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
文件夹名字是excel/ppt,上传里边所有的文件
```
aws s3 cp $filename $input --recursive
```
### translate job
```
output='s3://endoc/'
localfolder=en
iamrole='arn:aws:iam::295158943844:role/service-role/AmazonTranslateServiceRole-awstranslate'
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

## list all jobs

```
aws translate list-text-translation-jobs --filter JobName=$jobname
```
### download files


```
aws s3 sync $output $localfolder
```
### delete input folder
```
aws s3 rm $input --recursive
aws s3 rm $output --recursive
```

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "translate.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
