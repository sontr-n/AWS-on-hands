import related


@related.immutable
class PutItemParam(object):
    item = related.SequenceField(object)
    table = related.StringField()


@related.immutable
class PutItemResponse(object):
    response = related.SequenceField(object)


@related.immutable
class GetItemParam(object):
    body = related.SequenceField(object)
    table = related.StringField()


@related.immutable
class GetItemResponse(object):
    response = related.SequenceField(object)


@related.immutable
class UpdateItemParam(object):
    table = related.StringField()
    key = related.SequenceField(object)
    update_expression = related.StringField()
    expression_attr_values = related.SequenceField(object)


@related.immutable
class UpdateItemResponse(object):
    response = related.SequenceField(object)


@related.immutable
class ScanItemParam(object):
    table = related.StringField()
    index_name = related.StringField(required=False)
    limit = related.IntegerField(default=10)
    exclusive_start_key = related.SequenceField(object, required=False)


@related.immutable
class ScanItemResponse(object):
    response = related.ChildField(object)