from flask import jsonify, Blueprint, request
import requests, os
from pathlib import Path
from app.services.user_service import UserService
from app.mapping.user_schema import UserSchema
from app.mapping.response_schema import ResponseSchema
from app.models.response_message import ResponseBuilder
from dotenv import load_dotenv

user = Blueprint('user', __name__)
user_schema = UserSchema()
basedir = os.path.abspath(Path(__file__).parents[3])
load_dotenv(os.path.join(basedir, '.env'))
GYMCLASS_SERVICE_URL = os.getenv('GYMCLASS_SERVICE_URL')
BOOKINGS_SERVICE_URL = os.getenv('BOOKINGS_SERVICE_URL')

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
    url = f'{GYMCLASS_SERVICE_URL}find_all'
    response = requests.get(url)
    return response.json()

#book class
def book_gym_class(user_id, gym_class_id):
    url = f'{BOOKINGS_SERVICE_URL}book_class/{user_id}/{gym_class_id}'
    booking_data = {'user_id': user_id, 'gym_class_id': gym_class_id}
    response = requests.post(url, json=booking_data)
    return response.json()

#book cancel
@user.route('/book_cancel/<int:booking_id>', methods=['DELETE'])
def cancel_gym_class(booking_id):
    url = f'{BOOKINGS_SERVICE_URL}book_cancel/{booking_id}'
    response = requests.delete(url)
    return response.json()

#get all bookings
@user.route('/get_bookings/<int:user_id>', methods=['GET'])
def get_user_bookings(user_id):
    url = f'{BOOKINGS_SERVICE_URL}get_bookings/{user_id}'
    response = requests.get(url)
    return response.json()