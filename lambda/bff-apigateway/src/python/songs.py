import boto3


def list_songs(event, context):
    _lambda = boto3.client('lambda')
    _lambda.invoke()

    return {"statusCode": 200, "body": "ok"}
