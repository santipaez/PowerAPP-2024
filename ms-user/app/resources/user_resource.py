from flask import jsonify, Blueprint, requests, request
from app.services.user_service import UserService
from app.mapping.user_schema import UserSchema
from app.mapping.response_schema import ResponseSchema
from app.models.response_message import ResponseBuilder

user = Blueprint('user', __name__)
user_schema = UserSchema()

# home
@user.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the user home!"}), 200

# find all users
@user.route('/find_all', methods=['GET'])
def index():
    service = UserService()
    users = service.find_all()
    return jsonify({"users": [user.to_dict() for user in users]}), 200

#find user
@user.route('/find/<int:id>', methods=['GET'])
def find(id):
    service = UserService()
    user = service.find_by_id(id)
    if user is None:
        return jsonify({"message": "Usuario no encontrado"}), 404

    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(UserSchema().dump(user))
    return ResponseSchema().dump(response_builder.build()), 200

#delete user
@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    service = UserService()
    service.delete(id)
    return {"message": "Usuario eliminado"}, 200

#update user
@user.route('/update/<int:id>', methods=['PUT'])
def update(id):
    service = UserService()
    user_data = request.json
    service.update(id, user_data)
    return {"message": "Usuario actualizado"}, 200

# get all classes
@user.route('/get_classes', methods=['GET'])
def get_all_classes():
    response = requests.get('http://ms-gymclass.powerapp.localhost/find_all')
    classes = response.json()
    return {"classes": classes}, 200

#book class
@user.route('/book_class/<int:user_id>/<int:gym_class_id>', methods=['POST'])
def book_gym_class(user_id, gym_class_id):
    booking_service = BookingService()
    command = BookGymClassCommand(booking_service, user_id, gym_class_id)
    command.execute()
    return {"message": "Clase de gimnasio reservada"}, 200

#book cancel
@user.route('/book_cancel/<int:booking_id>', methods=['DELETE'])
def cancel_gym_class(booking_id):
    booking_service = BookingService()
    command = CancelGymClassCommand(booking_service, booking_id)
    command.execute()
    return {"message": "Reserva de clase de gimnasio cancelada"}, 200

#get all bookings
@user.route('/get_bookings/<int:user_id>', methods=['GET'])
def get_user_bookings(user_id):
    booking_service = BookingService()
    bookings = booking_service.find_all(user_id)
    return {"bookings": [booking.to_dict() for booking in bookings]}, 200