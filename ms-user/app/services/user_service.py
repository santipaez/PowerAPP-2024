from app.models import User
from app.repositories.user_repository import UserRepository
from app.services.security_service import SecurityService
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash
from tenacity import retry, stop_after_attempt, stop_after_delay

class UserService():

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))            
    def __init__(self) -> None:
        self.__repo = UserRepository()
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def execute(self, model):
        self.register(model.name, model.email, model.password)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def find_by_id(self, id) -> User:
        return self.__repo.find_by_id(id)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def find_all (self) -> list[User]:
        return self.__repo.find_all()

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def register(self, entity: User) -> User:
        entity.password = SecurityService.generate_hash(entity.password)
        return UserRepository().create(entity)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def update (self, id: int, entity: User) -> User:
        if 'password' in entity:
            entity['password'] = SecurityService.generate_hash(entity['password'])
        return self.__repo.update(id, entity)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def delete (self, entity: User) -> bool:
        return self.__repo.delete(entity)

    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def find_by_name (self, name: str) -> User:
        return self.__repo.find_by_name(name)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def find_by_email (self, email: str) -> User:
        return self.__repo.find_by_email(email)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def check_password(self, user: User, password: str) -> bool:
        return check_password_hash(user.password, password)
    
    @retry(stop=(stop_after_delay(5) | stop_after_attempt(5)))
    def check_auth(self, email, password):
        try:
            user = self.find_by_email(email)
        except NoResultFound:
            return False
        return self.check_password(user, password)
