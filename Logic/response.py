import json

def response(statusCode, body):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'}

    return {
        'statusCode': statusCode,
        'headers': headers,
        'isBase64Encoded' : True,
        'body' : json.dumps(body)
    }
