from adaptor.aws import dynamodb as dynamodb_instance
from dto.aws.dynamodb import *
import json

dynamodb_instance.instance()
table_name = "SongsTable"


def list_songs(event, context) -> dict:
    scan_item_param = ScanItemParam(table=table_name, **event)
    res = dynamodb_instance.scan_item(scan_item_param).response

    return {"statusCode": 200, "body": res["Items"]}


def add_song(event, context) -> dict:
    put_item_param = PutItemParam(table=table_name, item=event)
    dynamodb_instance.put_item(put_item_param)

    return {"statusCode: 200"}
