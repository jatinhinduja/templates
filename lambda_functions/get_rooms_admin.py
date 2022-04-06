"""
get_rooms_admin

Function performing the read/write operations of the API Resource /admin [GET]
"""

import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamo = boto3.resource('dynamodb')
    data = dynamo.Table('availability')
    dynamodata=str(data.scan()['Items'])
    print(dynamodata)
    print("The type of object is: ", type(dynamodata))
    return {
        'statusCode': 200,
        'body': dynamodata
    }