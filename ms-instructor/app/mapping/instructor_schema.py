from marshmallow import validate, fields, Schema

class InstructorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=5, max=120))
    email = fields.Email(required=True, validate=validate.Length(min=5, max=120))
    password = fields.String(required=True, validate=validate.Length(min=8, max=120), load_only=True)
    specialty = fields.Str(required=True)
