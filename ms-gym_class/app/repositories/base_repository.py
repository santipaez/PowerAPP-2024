from app.repositories.CRUD import Read, Update, Create, Delete
from app import db


class BaseRepository(Create, Read, Update, Delete):
    def __init__(self, model):
        self.model = model
    
    def find_all(self):
        return db.session.query(self.model).all()
        
    def find_by_id(self, id):
        return db.session.query(self.model).filter(self.model.id == id).one_or_none()

    def create(self, entity: db.Model):
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id: int):
        try:
            id = int(id)
        except ValueError:
            raise ValueError("Invalid ID")
        
        existing_entity = db.session.query(self.model).get(id)
        if existing_entity is not None:
            db.session.delete(existing_entity)
            db.session.commit()
            return {"message": "Deleted"}
        else:
            return  {"message": "Not found"}