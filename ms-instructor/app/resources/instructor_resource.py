import requests
from flask import jsonify, Blueprint, request
from app.services.instructor_service import InstructorService
from app.mapping.instructor_schema import InstructorSchema

instructor = Blueprint('instructor', __name__)
instructor_schema = InstructorSchema()

# find all
@instructor.route('/find_all', methods=['GET'])
def index():
    service = InstructorService()
    instructors = service.find_all()
    return jsonify({"instructors": [instructor.to_dict() for instructor in instructors]}), 200

#find by id
@instructor.route('/find/<int:id>', methods=['GET'])
def find(id):
    service = InstructorService()
    instructor = service.find_by_id(id)
    if instructor is None:
        return jsonify({"message": "Instructor no encontrado"}), 404

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
