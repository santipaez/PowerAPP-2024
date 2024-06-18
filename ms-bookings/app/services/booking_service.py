from app.models.booking import Booking
from app.repositories.booking_repository import BookingRepository

class BookingService:
    def __init__(self):
        self.__repo = BookingRepository()

    def find_by_id(self, id) -> Booking:
        return self.__repo.find_by_id(id)
    
    def find_all(self, user_id):
        return self.__repo.find_all(user_id)

    def add(self, entity: Booking) -> Booking:
        return self.__repo.create(entity)

    def update(self, id: int, entity: Booking) -> Booking:
        return self.__repo.update(id, entity)

    def delete(self, entity: Booking) -> bool:
        return self.__repo.delete(entity)

    def find_by_user_id(self, user_id: int) -> list[Booking]:
        return self.__repo.find_by_user_id(user_id)