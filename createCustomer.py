import json
import logging
import os
import time
import uuid
import boto3


dynamodb = boto3.resource('dynamodb')

def createCustomer(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['DYNAMODB_CUSTOMER_TABLE'])

    item = {
        'primary_key': data['name'],
        'email': data['email']
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 201,
    }

    return response
