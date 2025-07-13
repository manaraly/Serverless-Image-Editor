import boto3
import json

s3 = boto3.client('s3')
bucket_name = 'original-images-manar'

def lambda_handler(event, context):
    filename = event['queryStringParameters']['filename']
    
    response = s3.generate_presigned_post(
        Bucket=bucket_name,
        Key=f"original/{filename}",
        ExpiresIn=300
    )
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(response)
    }