from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services import UserService
from app.models import User
from app.mapping.user_schema import UserSchema

auth_user = Blueprint('auth_user', __name__)
user_service = UserService()
user_schema = UserSchema()

@auth_user.route('/register', methods=['POST'])
def register():
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if user_service.find_by_email(email):
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(name=name, email=email, password=password)
    new_user_create = user_service.register(new_user)
    return jsonify(user_schema.dump(new_user_create)), 201

@auth_user.route('/login', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    service = UserService()
    
    if service.check_auth(email, password):
        user = service.find_by_email(email)
        list_roles = [role.email for role in user.roles]
        
        access_token = create_access_token(user_schema.dump(user), additional_claims={"roles": list_roles})
        return jsonify({"id": user.id, "Sesion iniciada correctamente:": user.name}), 200
    else:
        return jsonify({"error": "Email or password invalid"}), 401
