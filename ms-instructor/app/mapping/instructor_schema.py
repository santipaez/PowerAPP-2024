from marshmallow import Schema, fields

class InstructorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=False)
    specialty = fields.Str(required=True)
