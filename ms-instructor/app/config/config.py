import os

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_URL')}/{os.environ.get('DB_NAME')}"

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_URL')}/{os.environ.get('DB_NAME')}"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app]