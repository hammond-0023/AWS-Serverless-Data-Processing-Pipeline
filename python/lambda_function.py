import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ResultsTable')

def lambda_handler(event, context):
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        # Fetch data from S3, process, and store in DynamoDB
        # (Add actual processing logic here)
        
        
        table.put_item(Item={"id": key, "status": "processed"})
        
    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
