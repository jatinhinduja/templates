"""
book_room_details

Function performing the read/write operations of the API Resource /booking_details [GET]
"""

import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bill_table = dynamodb.Table('temp')
    bill=bill_table.scan()['Items']
    print(bill)
    dynamo=boto3.client('dynamodb')
    
    if len(bill)>0:
        api_response=bill[0]
        response = dynamo.delete_item(
            TableName='temp',
            Key={
                "date_from": {"S": bill[0]['date_from']}
            }
        )
    else:
        api_response=None
    return {
        'statusCode': 200,
        'body': api_response
    }
