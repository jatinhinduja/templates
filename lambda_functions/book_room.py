"""
book_room

Function performing the read/write operations of the API Resource /booking [POST]
"""

import boto3
from datetime import datetime
import time


DATE_FORMAT = "%Y-%m-%d"
dynamodb = boto3.resource('dynamodb')

def to_time(epoch):
    import datetime 
    date_time = datetime.datetime.fromtimestamp( epoch ) 
    return date_time

def lambda_handler(event, context):
    #TODO implement
    response=None
    r_table = dynamodb.Table('rooms')
    r_dynamodata=r_table.scan()['Items']
    valid_rooms=[]
    for i in r_dynamodata:
        if i['room_type']==event['room_type']:
            valid_rooms.append(i)
    print(valid_rooms)
    
    a = datetime.strptime(event['date_from'], DATE_FORMAT)
    b = datetime.strptime(event['date_to'], DATE_FORMAT)
    delta = b - a
    difference_dates = delta.days
    print(difference_dates)
    
    a_table = dynamodb.Table('availability')
    a_dynamodata=a_table.scan()['Items']
    a_list=[]
    start = event['date_from']
    end = event['date_to']
    while(start!=end):
        for day in a_dynamodata:
            if start==day['date']:
                a_list.append(day)
        start = to_time(datetime.strptime(start, DATE_FORMAT).timestamp()+86400)
        start = start.strftime(DATE_FORMAT)
        print(start)
    print(a_list)
    
    for room in valid_rooms:
        flag=room
        for day in a_list:
            print(day) 
            string_q='room_'+str(room['room_id'])
            print(string_q)
            if day[string_q]==1:
                flag=0
                break
        if(flag!=0):
            response=room['room_id'],difference_dates*int(room['price']),event['date_from'],event['date_to']
    
    if(response):
        data_json={
            'room_id': response[0],
            'bill': str(response[1]),
            'date_from': response[2],
            'date_to': response[3]
        }
        table = dynamodb.Table('temp')
        res = table.put_item(Item = data_json)
        time.sleep(3)
    
    return {
        'statusCode': 200,
        'body': data_json
    }