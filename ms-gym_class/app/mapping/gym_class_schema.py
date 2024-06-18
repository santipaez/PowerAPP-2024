from app.models.gym_class import GymClass
from marshmallow import Schema, fields, post_load

class GymClassSchema(Schema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()

    @post_load
    def make_gymclass(self, data, **kwargs):
        return GymClass(**data)