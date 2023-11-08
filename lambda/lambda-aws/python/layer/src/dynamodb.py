import boto3
from typing import Dict


class DynamoConnector:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")

    def get_user_table(self):
        return self.dynamodb.table("user")
