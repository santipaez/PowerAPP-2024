from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services import InstructorService
from app.models import Instructor
from app.mapping.instructor_schema import InstructorSchema

auth_instructor = Blueprint('auth_instructor', __name__)
instructor_service = InstructorService()
instructor_schema = InstructorSchema()

@auth_instructor.route('/register', methods=['POST'])
def register():
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    specialty = request.json.get("specialty", None)

    if instructor_service.find_by_email(email):
        return jsonify({"error": "Email already exists"}), 400

    new_instructor = Instructor(name=name, email=email, password=password, specialty=specialty)
    new_instructor_create = instructor_service.register(new_instructor)
    return jsonify(instructor_schema.dump(new_instructor_create)), 201

@auth_instructor.route('/login', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    service = InstructorService()
    
    if service.check_auth(email, password):
        instructor = service.find_by_email(email)
        return jsonify({"id": instructor.id, "Sesion iniciada correctamente:": instructor.name}), 200
    else:
        return jsonify({"error": "Email or password invalid"}), 401
