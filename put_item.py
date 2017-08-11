"""Put item to dynamodb"""
#http://boto3.readthedocs.io/en/latest/guide/dynamodb.html

def read_json(file_name):
    """Return the pathname of the KOS root directory."""
    import json
    with open(file_name) as json_data:
        d = json.load(json_data)
        for data in d["items"]:
            yield data 



def main():
    """Main function"""    
    import boto3
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table('FAQ')
    items = read_json('content.json') 
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(item)
    print 'Done'        


if __name__ == "__main__":
    main()



     