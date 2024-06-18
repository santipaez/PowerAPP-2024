from app import db
from flask import jsonify, Blueprint, request
from app.models.instructor import Instructor
from app.services.instructor_service import InstructorService
from app.mapping.response_schema import ResponseSchema
from app.mapping.instructor_schema import InstructorSchema
from app.models.response_message import ResponseBuilder


instructor = Blueprint('instructor', __name__)
instructor_schema = InstructorSchema()

# find all
@instructor.route('/find_all', methods=['GET'])
def get_instructors():
    service = InstructorService()
    response_builder = ResponseBuilder()
    instructors = service.find_all()
    response_builder.add_message("Instructores encontrados")\
        .add_status_code(200)\
        .add_data([instructor.to_dict() for instructor in instructors])
    return ResponseSchema().dump(response_builder.build()), 200

#find by id
@instructor.route('/find/<int:id>', methods=['GET'])
def get_instructor_by_id(id):
    service = InstructorService()
    response_builder = ResponseBuilder()
    instructor = service.find_by_id(id)
    response_builder.add_message("Instructor encontrado")\
        .add_status_code(200)\
        .add_data(instructor.to_dict() if instructor else None)
    return ResponseSchema().dump(response_builder.build()), 200

#update
@instructor.route('/update/<int:id>', methods=['PUT'])
def update_instructor(id):
    service = InstructorService()
    instructor_data = request.json
    updated_instructor = service.update(id, instructor_data)
    return {"message": "Instructor actualizado", "instructor": InstructorSchema().dump(updated_instructor)}, 200

#delete
@instructor.route('/delete/<int:id>', methods=['DELETE'])
def delete_instructor(id):
    service = InstructorService()
    service.delete(id)
    return {"message": "Instructor eliminado"}, 200

#create class
@instructor.route('/create_class/<int:id>', methods=['POST'])
def create_class(id):
    service = GymClassService()
    class_data = request.get_json()
    class_data['instructor_id'] = id
    new_class = service.create(class_data)
    return {"message": "Clase creada", "class": GymClassSchema().dump(new_class)}, 201

#update class
@instructor.route('/update_class/<int:id>', methods=['PUT'])
def update_class(id):
    service = GymClassService()
    class_data = request.json
    updated_class = service.update(class_data, id)
    return {"message": "Clase actualizada", "class": GymClassSchema().dump(updated_class)}, 200

#delete class
@instructor.route('/delete_class/<int:id>', methods=['DELETE'])
def delete_class(id):
    service = GymClassService()
    service.delete(id)
    return {"message": "Clase eliminada"}, 200
