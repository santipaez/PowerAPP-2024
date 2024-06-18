from app import db
from dataclasses import dataclass
from sqlalchemy import Column

@dataclass
class GymClass(db.Model):
    __tablename__ = 'gym_classes'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    name = Column(db.String(100))
    duration = Column(db.String(100))
    instructor = Column(db.String(100))

    def __init__(self, name, duration, instructor):
        self.name = name
        self.duration = duration
        self.instructor = instructor
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "instructor": self.instructor
        }