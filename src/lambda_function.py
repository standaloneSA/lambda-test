import json
import os

print('Loading function')
print(os.environ)

def lambda_handler(event, context):
    message = str(event)

    body = json.loads(event['body'])
    print(body)
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': event['body']
    }

