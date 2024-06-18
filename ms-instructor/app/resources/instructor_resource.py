from app import db
import requests
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
def create_class(instructor_id, class_data):
    url = f"http://ms-gymclass.powerapp.localhost/add/{instructor_id}"
    response = requests.post(url, json=class_data)
    return response.json()

#update class
def update_class(class_id, class_data):
    url = f"http://ms-gymclass.powerapp.localhost/update/{class_id}"
    response = requests.put(url, json=class_data)
    return response.json()

#delete class
def delete_class(class_id):
    url = f"http://ms-gymclass.powerapp.localhost/delete/{class_id}"
    response = requests.delete(url)
    return response.json()
