import json

print('Loading function')


def lambda_handler(event, context):
    message = str(event)
    #print("Received event: " + json.dumps(event, indent=2))
    #print("value1 = " + event['key1'])
    #print("value2 = " + event['key2'])
    #print("value3 = " + event['key3'])
    #return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

    body = json.loads(event['body'])
    print(body)
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': event['body']
    }

