from marshmallow import Schema, fields

class BookingSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Nested('UserSchema', many=True, exclude=('bookings',))
    gym_class_id = fields.Nested('GymClassSchema', many=True, exclude=('bookings',))
    booking_date = fields.DateTime(required=True)