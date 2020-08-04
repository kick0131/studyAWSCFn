import json


def lambda_handler(event, context):
    print('hello')

    jsonobj = {}
    jsonobj['test'] = 'hoge'

    result = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(jsonobj)}

    return result
