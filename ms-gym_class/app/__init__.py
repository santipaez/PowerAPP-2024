from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from app.config import config
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

cache = Cache()
ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)
    
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)

    ma.init_app(app)
    f.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.resources import gym_class
    
    app.register_blueprint(gym_class, url_prefix='/classes')
    
    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300,
                            'CACHE_REDIS_HOST': os.getenv('REDIS_HOST'), 'CACHE_REDIS_PORT': os.getenv('REDIS_PORT'),
                            'CACHE_REDIS_DB': os.getenv('REDIS_DBNAME'), 'CACHE_REDIS_PASSWORD': os.getenv('REDIS_PASSWORD'),
                            'CACHE_KEY_PREFIX':'product_'})

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
