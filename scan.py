"""Dump all data from dynamodb to a file """

from boto3.dynamodb.conditions import Key, Attr
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FAQ')

response = table.scan(
    #FilterExpression=Attr('ask')
)
items = response['Items']
print(items)

fh = open('dumpdb.txt','w')
for item in items:
    fh.writelines('ask:'+item['ask']+'\n')
    fh.flush()
    print 'ask',item['ask']
    fh.writelines('ans:'+item['ans']+'\n')
    fh.flush()
    print 'ans',item['ans']
    print '============='

