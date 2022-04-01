import boto3 

iam=boto3.client('iam')
response=iam.list_users()
for item in response['Users']:
    print(item['UserName'])
print()

s3=boto3.client('s3')
response=s3.list_buckets()
for item in response['Buckets']:
    print(item['Name'])
print()

iam=boto3.resource('iam')
response=iam.users.all()
for i in response:
    print(i.name)
print()

root=boto3.session.Session(profile_name="Tryingtroyl")
sts=root.client('sts')
response=sts.get_caller_identity()
print(response)

ec2=boto3.client(service_name='ec2',region_name='ap-south-1')
response=ec2.describe_instances()['Reservations']
print(response)

        