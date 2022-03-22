```bash
# dynamoDB
aws cloudformation deploy --template-file dynamodb.yml --stack-name sample-dynamo --profile <MyAWSProfile>

# EventBridge
aws cloudformation deploy --template-file eventBridge_forLambda.yml --stack-name sample-eventbridge --parameter-overrides LambdaArn=<Lambda ARN> CronExpression="cron(0/2 * * * ? *)" --profile <MyAWSProfile>
```