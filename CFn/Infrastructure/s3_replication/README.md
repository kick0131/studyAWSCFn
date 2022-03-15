## description
以下のS3バケットを作成する

- シンプルなS3バケット
- S3に書き込んだバケットは別リーションのバックアップ用S3バケットにレプリケーション
- バックアップ用S3バケットは一定期間後にGlacierに移動(費用削減)

```bash
# 先にバックアップ用のS3バケットを作成(別リージョン指定が必要)
aws cloudformation deploy --stack-name s3-backup --template-file s3_Bucket_buckup.yml --parameter-overrides Service=hoge Stage=dev --region ap-northeast-3

# バックアップ用S3バケット名を指定してS3バケット作成
aws cloudformation deploy --stack-name s3-app --template-file s3_Bucket.yml --capabilities CAPABILITY_NAMED_IAM --parameter-overrides Service=hoge Stage=dev BackupBucketName=XXX
```
