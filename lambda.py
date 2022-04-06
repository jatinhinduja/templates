"""
Python script containing all lamda functions used in the project
"""

def aws_project_app():
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




def get_rooms_user():
    """
    get_rooms_user

    Function performing the read/write operations of the API Resource /home [GET]
    """

    import json
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



def get_rooms_admin():
    """
    get_rooms_admin

    Function performing the read/write operations of the API Resource /admin [GET]
    """

    import json
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


def book_room():
    """
    book_room

    Function performing the read/write operations of the API Resource /booking [POST]
    """

    import json
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


def book_room_details():
    """
    book_room_details

    Function performing the read/write operations of the API Resource /booking_details [GET]
    """

    import json
    import boto3
    import time
    
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
