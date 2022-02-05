# CFn

## First setup
1. craete APIkey
    ```bash
    aws configure <unique name>
    ```
    after execute, write on `.aws/configure` and `.aws/credential`

    - (確認) AWSプロファイル一覧
    ```bash
    aws configure list-profiles
    ```

### use VsCode
- add setting.json
    ```bash
    "yaml.customTags": [
        "!Ref",
        "!Sub scalar",
        "!Sub sequence",
        "!Join sequence",
        "!FindInMap sequence",
        "!GetAtt scalar",
        "!GetAtt sequence",
        "!Base64 mapping",
        "!GetAZs",
        "!Select scalar",
        "!Select sequence",
        "!Split sequence",
        "!ImportValue",
        "!Condition",
        "!Equals sequence",
        "!And",
        "!If",
        "!Not",
        "!Or"
    ],
    ```

### use MFA
★ToDo

## Guidelines
- 環境依存値はSystems Parameterを使用し、親スタックから子スタックを呼び出す形式とする
    1. 親スタック起動
        - Systems Parameterを設定
        - 子スタックの呼び出し
    1. 子スタック起動
        - INPUTパラメータは全てSystems Parameterを使用する

## Subnet

| subnet | 用途 | 備考 |
|-- |-- |-- |
| 10.1.0.0/24| メインPublic | |
| 10.1.2.0/24| メインPrivate | |
| 10.1.10.0/24| jupyterコンテナ | |


## AWS CLI
```bash
# スタック一覧
aws cloudformation list-stacks --profile <profile name>

# チェンジセット削除
aws cloudformation delete-change-set --change-set-name <change set name> --stack-name <stack name> --profile <profile name>
```

## 参考サイト
[[公式] 動的な参照を使用してテンプレート値を指定する](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/dynamic-references.html)
