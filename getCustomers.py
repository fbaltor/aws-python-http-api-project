import os
import json

import boto3
dynamodb = boto3.resource('dynamodb')


def getCustomers(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_CUSTOMER_TABLE'])

    result = table.scan()

    if (result['Count'] == 0):
        return {
            "statusCode": 404,
        }

    def getProps(item):
        d = {}
        d['name'] = item['primary_key']
        d['email'] = item['email']

        return d
    items = list(map(getProps, result['Items']))

    r = {}
    r['items'] = items
    r['total'] = result['Count']

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(r)
    }

    return response
