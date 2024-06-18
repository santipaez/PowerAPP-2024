from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db
from dataclasses import dataclass

@dataclass
class Instructor(db.Model):
    __tablename__ = 'instructors'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String)
    email = db.Column('email', db.String, unique=True)
    password = db.Column('password', db.String)
    specialty = db.Column('specialty', db.String)

    roles = db.relationship("Role", secondary="instructor_roles", back_populates="instructors")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'specialty': self.specialty
        }