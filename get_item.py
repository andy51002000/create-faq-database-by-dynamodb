"""Get particular item from dynamodb """
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FAQ')
response = table.get_item(
    Key={
        'ask': 'FaQToChangeKeyboardLayout',
        'type':'none'
        
    }
)
item = response['Item']
print(item)