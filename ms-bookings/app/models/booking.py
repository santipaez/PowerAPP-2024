from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app import db
from dataclasses import dataclass

@dataclass
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer, ForeignKey('users.id'))
    gym_class_id = db.Column('gym_class_id', db.Integer, ForeignKey('gym_classes.id'))
    booking_date = db.Column('booking_date', db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'gym_class_id': self.gym_class_id,
            'booking_date': self.booking_date
        }