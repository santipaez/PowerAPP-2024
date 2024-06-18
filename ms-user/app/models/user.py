from dataclasses import dataclass
from app import db

@dataclass
class User(db.Model):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String)
    email = db.Column('email', db.String, unique=True)
    password = db.Column('password', db.String)
    
    roles = db.relationship("Role", secondary="user_roles", back_populates="users")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }