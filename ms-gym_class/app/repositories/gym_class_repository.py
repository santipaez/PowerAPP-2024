from app.models.gym_class import GymClass
from app.repositories.base_repository import BaseRepository
from app import db

class GymClassRepository(BaseRepository):
    def __init__(self):
        super().__init__(GymClass)
        self.model = GymClass
    
    def find_all(self):
        return super().find_all()
        
    def find_by_id(self, id) -> GymClass:
        return super().find_by_id(id)

    def create(self, class_data: GymClass) -> GymClass:
        return super().create(class_data)
    
    def update(self, class_data: dict, id: int):
        try:
            existing_entity = db.session.query(self.model).get(id)
            if existing_entity is not None:
                for key, value in class_data.items():
                    setattr(existing_entity, key, value)
                db.session.commit()
                return existing_entity
            else:
                return {"message": "Not found"}
        except Exception as e:
            db.session.rollback()
            raise e