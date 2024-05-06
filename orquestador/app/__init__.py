from flask import Flask
from flask_restful import Api
from .resources.home import Home
from .services.user_service import UserService
from .services.instructor_service import InstructorService

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    user_service = UserService()
    instructor_service = InstructorService()

    api.add_resource(Home, '/', resource_class_args=(user_service, instructor_service))

    return app
