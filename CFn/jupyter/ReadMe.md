# jupyter on Fargate

## 構成

```
  +--------------------------+
  | VPC                      |
  |  +---------------------+ |
  |  | Subnet              | |
  |  |  +---------------+  | |
  |  |  | AWS Fargate   |  | |
  |  |  |               |  | |
  |  |  | +----------+  |  | |
  |  |  | | ECS Task |  |  | |
  |  |  | | (jupyter)|  |  | |
  |  |  | +----------+  |  | |
  |  |  | +----------+  |  | |
  |  |  | | .note    |  |  | |
  |  |  | +----------+  |  | |
  |  |  +-----^---------+  | |
  |  |        |            | |
  |  |        | volume mount |
  |  |  +---------------+  | |
  |  |  | AWS EFS       |  | |
  |  |  | +----------+  |  | |
  |  |  | | .note    |  |  | |
  |  |  | +----------+  |  | |
  |  |  +---------------+  | |
  |  +---------------------+ |
  +--------------------------+
```

## Create on template
- Subnet
- Security Group
- ECS Task
- ECS Service
- EFS
- IAM Role
- IAM Policy

## Not create on template
- VPC

## Usage
- packageコマンドで指定するS3バケットは一時的なものなので、作成すれば何でもよい。
- 上書き時はymlファイルを修正し、package,deployの順に実行しなおす
```bash
# S3にパッケージ情報を作成
aws cloudformation package --template-file jupyter_root.yml --s3-bucket some-cfn-package --s3-prefix jupyter --output-template-file package.yml --profile <profile name>

# デプロイ
aws cloudformation deploy --template-file package.yml --stack-name jupytersample --no-fail-on-empty-changeset --capabilities CAPABILITY_NAMED_IAM --profile <profile name>

# 削除
aws cloudformation delete-stack --stack-name jupytersample --profile <profile name>
```

| option | desctiption |
| -- | -- |
| --s3-prefix | packageコマンド時のS3バケットを指定 |
| | |
| --no-fail-on-empty-changeset | チェンジセットが無い場合も終了コードが0になる |


## 必要なSecurityGtoup定義
- FargateからのEFSへのアクセス許可(EFS側に定義)

## 必要なIAM定義
- ECS実行ポリシー(ECS側に定義)
- EFS操作ポリシー(ECS側に定義)
