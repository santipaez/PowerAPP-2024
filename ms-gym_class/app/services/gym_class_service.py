from app.models.gym_class import GymClass
from app.repositories import GymClassRepository
from app import db


class GymClassService:
    def __init__(self) -> None:
        self.__repo = GymClassRepository()
    
    def find_all(self):
        return self.__repo.find_all()

    def find_by_id(self, id):
        return self.__repo.find_by_id(id)

    def create(self, class_data: dict) -> GymClass:
        gym_class = GymClass(**class_data)
        return self.__repo.create(gym_class)

    def update(self, id, class_data):
        return self.__repo.update(id, class_data)

    def delete(self, id):
        return self.__repo.delete(id)