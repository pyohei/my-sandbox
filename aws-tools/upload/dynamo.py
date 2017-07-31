"""Upload data to DynamoDB."""


import boto3
import random


dynamo = boto3.resource('dynamodb')
table = dynamo.Table('sandbox-naming')
# print table.creation_date_time
for n in range(10):
    random.seed()
    insert_int = random.randint(0, 999999)
    table.put_item(
        Item={
            'myname': str(insert_int)
        }
    )

it = table.get_item(
    Key={
        'myname': '777'
    }
)
print it
