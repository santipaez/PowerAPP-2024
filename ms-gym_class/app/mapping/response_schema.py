from app.models import response_message
from marshmallow import validate, Schema, fields

class ResponseSchema(Schema):
    message = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    status_code = fields.Int(required=True)
    data = fields.Dict(required=False)
