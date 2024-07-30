from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.database import FULL_URL_DB
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_caching import Cache
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

cache = Cache()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = 'super-secret'
    
    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from app.resources import instructor
    from app.resources.auth_instructor import auth_instructor
    app.register_blueprint(instructor, url_prefix='/instructor')
    app.register_blueprint(auth_instructor, url_prefix='/auth_instructor')
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300, 
                            'CACHE_REDIS_HOST': os.getenv('REDIS_HOST'), 'CACHE_REDIS_PORT': os.getenv('REDIS_PORT'), 
                            'CACHE_REDIS_DB': os.getenv('REDIS_DBNAME'), 'CACHE_REDIS_PASSWORD': os.getenv('REDIS_PASSWORD'), 
                            'CACHE_KEY_PREFIX': 'product_'})
    
    return app