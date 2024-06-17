from app.models.booking import Booking
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class InstructorRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.model = Booking
    
    def create(self, entity: Booking) -> Booking:
        return super().create(entity)
    
    def find_all(self):
        return super().find_all()
    
    def find_by_id(self, id) -> Booking:
        return super().find_by_id(id)
    
    def find_by_name(self, name) -> Booking:
        return db.session.query(self.model).filter(self.model.name == name).one_or_none()
    
    def find_by_email(self, email) -> Booking:
        return db.session.query(self.model).filter(self.model.email == email).one_or_none()

    def update(self, id: int, new_data: dict) -> Booking:
        return super().update(id, **new_data)

    def delete(self, id: int):
        return super().delete(id)