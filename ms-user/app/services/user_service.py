from app.models import User
from app.repositories.user_repository import UserRepository
from app.services.security_service import SecurityService
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash

class UserService():
    def __init__(self) -> None:
        self.__repo = UserRepository()
        
    def execute(self, model):
        self.register(model.name, model.email, model.password)
    
    def find_by_id(self, id) -> User:
        return self.__repo.find_by_id(id)
    
    def find_all (self) -> list[User]:
        return self.__repo.find_all()

    def register(self, entity: User) -> User:
        entity.password = SecurityService.generate_hash(entity.password)
        return UserRepository().create(entity)
    
    def update (self, id: int, entity: User) -> User:
        if 'password' in entity:
            entity['password'] = SecurityService.generate_hash(entity['password'])
        return self.__repo.update(id, entity)
    
    def delete (self, entity: User) -> bool:
        return self.__repo.delete(entity)

    def find_by_name (self, name: str) -> User:
        return self.__repo.find_by_name(name)
    
    def find_by_email (self, email: str) -> User:
        return self.__repo.find_by_email(email)
    
    def check_password(self, user: User, password: str) -> bool:
        return check_password_hash(user.password, password)
    
    def check_auth(self, email, password):
        try:
            user = self.find_by_email(email)
        except NoResultFound:
            return False
        return self.check_password(user, password)
