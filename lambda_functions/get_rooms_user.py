"""
get_rooms_user

Function performing the read/write operations of the API Resource /home [GET]
"""

import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamo = boto3.resource('dynamodb')
    data = dynamo.Table('rooms')
    dynamodata=str(data.scan()['Items'])
    print(dynamodata)
    print("The type of object is: ", type(dynamodata))
    return {
        'statusCode': 200,
        'body': dynamodata
    }
