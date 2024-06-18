from flask import jsonify, Blueprint, request
import requests
from app.services.gym_class_service import GymClassService
from app.mapping.gym_class_schema import GymClassSchema
from app.models.response_message import ResponseBuilder
from app.mapping.response_schema import ResponseSchema


gym_class = Blueprint('gym_class', __name__)
gym_class_schema = GymClassSchema()
@gym_class.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Gym Class API"}), 200

# find all
@gym_class.route('/find_all', methods=['GET'])
def get_classes():
    service = GymClassService()
    gym_classes = service.find_all()
    return jsonify({"Classes": [gym_class.to_dict() for gym_class in gym_classes]}), 200

#find by id
@gym_class.route('/find/<int:id>', methods=['GET'])
def find(id):
    service = GymClassService()
    find_clasess = service.find_by_id(id)
    if find_clasess is None:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    gym_class_schema = GymClassSchema()
    serialized_data = gym_class_schema.dump(find_clasess)

    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(serialized_data)
    return ResponseSchema().dump(response_builder.build()), 200

#create
@gym_class.route('/add', methods=['POST'])
def create_class():
    service = GymClassService()
    class_data = request.get_json()
    new_class = service.create(class_data)
    return {"message": "Clase creada", "class": GymClassSchema().dump(new_class)}, 201

#update
@gym_class.route('/update/<int:id>', methods=['PUT'])
def update_class(id):
    service = GymClassService()
    class_data = request.json
    updated_class = service.update(class_data, id)
    return {"message": "Clase actualizada", "class": GymClassSchema().dump(updated_class)}, 200

#delete
@gym_class.route('/delete/<int:id>', methods=['DELETE'])
def delete_class(id):
    service = GymClassService()
    service.delete(id)
    return {"message": "Clase eliminada"}, 200
