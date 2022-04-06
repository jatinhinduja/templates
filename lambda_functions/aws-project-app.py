"""
aws-project-app

The function to populate the table availability
"""

import json
import boto3
from datetime import date, timedelta

def lambda_handler(event, context):
    list_of_date = []
    today = date.today()
    
    for delta in range(31):
        current_date = today + timedelta(days=delta)
        date_dict = {"date": str(current_date), "room_101": "1", "room_102": "1", "room_103": "1", "room_104": "1",
            "room_105": "1", "room_201": "1", "room_202": "1", "room_203": "1", "room_204": "1", "room_205": "1"}
        list_of_date.append(date_dict)
        
    response = json.dumps(list_of_date, sort_keys=True, indent=2)
    result = json.loads(response)
    
    dynamo = boto3.resource('dynamodb')
    availability_table = dynamo.Table('availability')
    
    with availability_table.batch_writer() as writer:
        for item in result:
            writer.put_item(item)   
    return {
        'statusCode': 200,
        'body': json.dumps("Data inserted into dynamodb")
    }
