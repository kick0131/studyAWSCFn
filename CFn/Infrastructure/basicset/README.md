## usage

```bash
# ---------------
# 事前準備
# ---------------
# 格納先S3バケット作成
aws cloudformation deploy --stack-name infra-s3 --template-file s3_Bucket.yml --capabilities CAPABILITY_NAMED_IAM --parameter-overrides

# ---------------
# 一括作成
# ---------------
# パッケージ作成
aws cloudformation package --template-file main.yml --s3-bucket <パッケージ用S3バケット> --s3-prefix dev --output-template-file package.yml

# GuardDuty未生成の場合、EnableGuardDutyDetectorはyesを設定
# SnsEndpointEmailは通知先メールアドレスを設定
aws cloudformation deploy --stack-name infra-multistack --template-file package.yml --capabilities CAPABILITY_NAMED_IAM --parameter-overrides EnableGuardDutyDetector=yes SnsEndpointEmail=XXX
```
