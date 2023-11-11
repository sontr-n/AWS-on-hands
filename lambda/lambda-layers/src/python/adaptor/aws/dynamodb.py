from dto.aws.dynamodb import *


def instance():
    import sys
    import boto3

    self = sys.modules[__name__]
    credentials = boto3.Session().get_credentials()

    self.dynamodb = boto3.client(
        "dynamodb",
        aws_access_key_id=credentials.access_key,
        aws_secret_access_key=credentials.secret_key,
        aws_session_token=credentials.token,
    )

    return self


def get_item(param: GetItemParam) -> GetItemResponse:
    response = dynamodb.get_item(TableName=param.table, Key=param.body)
    return GetItemResponse(response=response["Item"])


def put_item(param: PutItemParam) -> PutItemResponse:
    response = dynamodb.put_item(TableName=param.table, Item=param.item)
    return PutItemResponse(response=response)


def update_item(param: UpdateItemParam) -> UpdateItemResponse:
    response = dynamodb.update_item(
        TableName=param.table,
        Key=param.key,
        UpdateExpression=param.update_expression,
        ExpressionAttributeValues=param.expression_attr_values,
    )
    return UpdateItemResponse(response=response)


def scan_item(param: ScanItemParam) -> ScanItemResponse:
    kwargs = {"TableName": param.table}
    if param.index_name:
        kwargs["IndexName"] = param.index_name
    if param.exclusive_start_key:
        kwargs["ExclusiveStartKey"] = param.exclusive_start_key

    response = dynamodb.scan(**kwargs)

    return ScanItemResponse(response=response)
