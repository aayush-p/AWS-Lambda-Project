import boto3
import json
from io import BytesIO

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    string_io = BytesIO()
    s3_client.download_fileobj('resourceswikimedia', 'Agile/Agile_Atlassian.txt', string_io)
    v = event["queryStringParameters"]["resource"]
    #text
    return respond(None, str(string_io.getvalue()))
    
    
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
