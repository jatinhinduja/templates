HOTEL ROOM BOOKING APPLICATION

SITE: http://for-practice-inkwell.s3-website.ap-south-1.amazonaws.com


Description:

A serverless, static website hosted on AWS Simple Storage Service (S3) to facilitate the booking of rooms for a hotel
using user provided data.


Services Used:

    - Amazon Services:
        - S3
        - DynamoDB
        - API Gateway
        - Lambda (Python)
        - Cloudwatch (For monitoring)
        - IAM (For access control)
    - AWS CLI
    - boto3
    - HTML
    - Basic Javascript
    - Postman (To monitor APIs)


Operations:

    - For the user:
        - A user can access the website to input data, specifically the check-in date, the check-out date and the category 
          of rooms he/she wishes to stay in.
        - The user would then be returned the cost, and the details of his/her stay if the room is available.
    
    - For the hotel admin:
        - The admin can access the website to know about the room availability for the next 31 days for all the rooms.


Pre-requisites to run:

The user can run the site accessed by "http://for-practice-inkwell.s3-website.ap-south-1.amazonaws.com" using any
web browser.


Structure (For developers):

    - Database:
      The database is hosted on three serverless DynamoDB tables:
        - rooms : This table contains the prices, room numbers and categories of rooms.
        - availability : A calendar table that shows the availability of each room for the next month.
        - temp : A table with only one record at a time, the bill details of the customer.

    - Front-end:
        - index.html : The home page that shows details of the rooms.
        - booking.html : The booking page with the form.
        - booking_details.html : The details of the bill should be visible on this page.
        - show_room_details.html : The HTML page for the admin that shows the availability table.

    - APIs:
        - https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/home [GET]
          This GET API fetches the date from the table "rooms" and returns it to index.html.

        - https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking [POST]
          The POST request that sends the user form data to AWS Lambda for processing.

        - https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking_details [GET]
          The API to get the bill details from table temp.

        - https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/admin [GET]
          This API gets the admin table availability to render it to show_room_details.html.

    - Lambda:
      All the lambda functions can be referred to in the "lambda.py" file.

    - S3:
      The bucket named "for-practice-inkwell" hosts and stores the project.


Contact for additional information:

    - XXXX@gmail.com
    - XXXX@gmail.com


Thank you!

