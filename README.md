# CFn
## All View
- Route53
    - CloudFront
        - S3 (frontend app backet)
        - API Gateway
- S3 (CloudFront logbacket)
- Cognito
- IAM policy

## Prepare
1. Install AWS CLI
1. Configure AWS 

    `aws config`

## Usage
### execute order
1. Cognito
1. CloudFront
1. S3AttachOAI

[Option]
- Route53Record
- AllowAppGwLog

### Command
Execute AWS CLI from Windows
```
aws cloudformation create-stack --template-body file://.\FrontendInfraCognito.yml --cli-input-json file://.\Input_Cognito.json --profile <MyAWSProfile> --no-verify
```

## Explanation
---
### FrontendInfraAllowAppGwLog.yml
Attach log policy to allow API Gateway logging.
- IAM (for apigateway)

| input key | example |
| --- | --- |
| ApiGwResourceId | wqk6a1w8o5 |

---
### FrontendInfraCloudFront.yml
Create basic frontend infrastructure AWS services.
- CloudFront
    - access to S3(static frontend application)
    - access to API Gateway

| input key | example |
| --- | --- |
| FrontendS3Backet | \<backetname>.s3.amazonaws.com |
| BackEndDomainName | \<apigw domain>.amazonaws.com |

---
### FrontendInfraCognito.yml
Create Cognito userpool.
- Cognito

| input key | example |
| --- | --- |
| MyUserPoolName | sample-pool |
| MyAppClientName | app-client |

---
### FrontendInfraRoute53Record.yml
Add Route53 record set.
- Route53 Record (CloudFront alias record)

| input key | example |
| --- | --- |
| MyHostedZoneId | Z01807202MZSSEFT3Y2ZL |
| Route53BaseDomainName | sample.com |
| Route53SubDomainName | app |

---
### FrontendInfraS3AttachOAI.yml
Add Cloudfront Origin Access Identity to S3 Backet policy.
- BacketPolicy (for frontend S3)

| input key | example |
| --- | --- |
| MyOAIDistributionID |  |
| AttachOAIS3Backet | \<backetname> |

---

# SAM
## All View
- API Gateway
    - Lambda
- IAM

## Usage
change current directory
`cd SAM`

### Command
Execute AWS CLI from Windows

create stack-template
```
aws cloudformation package --template-file BackendLambda.yml --output-template-file BackendLambda-output.yml --s3-bucket <OutputResourceBacket> --profile <MyAWSProfile>
```

deploy
```
aws cloudformation deploy --template-file BackendLambda-output.yml --stack-name sample-backend --capabilities CAPABILITY_NAMED_IAM --profile <MyAWSProfile>
```
