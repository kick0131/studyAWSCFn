## usage
必要に応じて`--profile`オプションを使用する
```bash
# cloudtrail

# cloudwatch
aws cloudformation deploy --template-file cloudwatch.yml --stack-name sample-cloudwatch --parameter-overrides LambdaArn=<arn> SnsArn=<topic arn> S3Bucket=<bucket name>

# sns
aws cloudformation deploy --template-file sns.yml --stack-name sample-sns
```
