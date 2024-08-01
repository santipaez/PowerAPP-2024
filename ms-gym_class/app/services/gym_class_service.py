from app.models.gym_class import GymClass
from app.repositories import GymClassRepository
from app import cache
from tenacity import retry, stop_after_delay, stop_after_attempt

class GymClassService:

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    @cache.memoize(timeout=40)
    def __init__(self) -> None:
        self.__repo = GymClassRepository()
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    @cache.memoize(timeout=40)
    def find_all(self):
        return self.__repo.find_all()

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    @cache.memoize(timeout=40)
    def find_by_id(self, id):
        return self.__repo.find_by_id(id)

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    @cache.memoize(timeout=40)
    def create(self, class_data: dict) -> GymClass:
        gym_class = GymClass(**class_data)
        return self.__repo.create(gym_class)

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    @cache.memoize(timeout=40)
    def update(self, id, class_data):
        return self.__repo.update(id, class_data)

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    @cache.memoize(timeout=40)
    def delete(self, id):
        return self.__repo.delete(id)