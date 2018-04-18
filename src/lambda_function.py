import json
import os
import boto3

targetArn = "arn:aws:sns:us-east-1:125387665580:matt_only_sms"

print('Loading function')

def lambda_handler(event, context):
    message = str(event)

    body = json.loads(event['body'])
    sns = boto3.client('sns')
    try:
      response = sns.publish(TopicArn = targetArn, Message=event['body'])
      return {
          'statusCode': 200,
          'headers': { 'Content-Type': 'application/json' },
          'body': event['body']
      }
    except Exception as err:
      return {
        'statusCode': 400,
        'headers': { 'Content-Type': 'application/json' },
        'body': 'Failed'
      }

