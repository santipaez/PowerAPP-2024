from flask import jsonify, Blueprint, request
from app.services.booking_service import BookingService
from app.models.response_message import ResponseBuilder
from app.mapping.response_schema import ResponseSchema


booking = Blueprint('booking', __name__)
booking_schema = BookingService()


@booking.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Gym Class API"}), 200

# find all
@booking.route('/find_all', methods=['GET'])
def get_classes():
    service = BookingService()
    find_booking = service.find_all()
    return jsonify({"booking": [booking.to_dict() for booking in find_booking]}), 200

#find by id
@booking.route('/find/<int:id>', methods=['GET'])
def find(id):
    service = BookingService()
    find_id = service.find_by_id(id)
    if find_id is None:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    booking_schema = BookingService()
    serialized_data = booking_schema.dump(find_id)

    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(serialized_data)
    return ResponseSchema().dump(response_builder.build()), 200