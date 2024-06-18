from app.models import Instructor
from app.repositories.instructor_repository import InstructorRepository
from werkzeug.security import check_password_hash
from sqlalchemy.orm.exc import NoResultFound
from app import cache
from app.services.security_service import SecurityService



class InstructorService():
    def __init__(self) -> None:
        self.__repo = InstructorRepository()

   # @cache.memoize(timeout=40)                                   #probamos este cache de objetos luego
    def find_by_id(self, id) -> Instructor:
        return self.__repo.find_by_id(id)

    
    #@cache.memoize(timeout=40)
    def find_all (self) -> list[Instructor]:
        return self.__repo.find_all()


    def register(self, entity: Instructor) -> Instructor:
        entity.password = SecurityService.generate_hash(entity.password)
        return InstructorRepository().create(entity)
     
    
    def update (self, id: int, entity: Instructor) -> Instructor:
        if 'password' in entity:
            entity['password'] = SecurityService.generate_hash(entity['password'])
        return self.__repo.update(id, entity)
    
    
    def delete (self, entity: Instructor) -> bool:
        return self.__repo.delete(entity)


    #@cache.memoize(timeout=40)
    def find_by_name (self, name: str) -> Instructor:
        return self.__repo.find_by_name(name)

    
    #@cache.memoize(timeout=40)
    def find_by_email (self, email: str) -> Instructor:
        return self.__repo.find_by_email(email)

    
    #@cache.memoize(timeout=40)
    def check_password(self, user: Instructor, password: str) -> bool:
        return check_password_hash(user.password, password)

    
    #@cache.memoize(timeout=40)
    def check_auth(self, email, password):
        try:
            user = self.find_by_email(email)
        except NoResultFound:
            return False
        return self.check_password(user, password)
    
     
