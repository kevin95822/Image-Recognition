import json
import boto3

def lambda_handler(event, context):
    rekognition = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket= "imagerecognitionbucket2021", Key="texas-tiger-24.jpg")
    response = rekognition.detect_labels(Image={"S3Object" : {"Bucket" : "imagerecognitionbucket2021", "Name" : "texas-tiger-24.jpg"}})
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
