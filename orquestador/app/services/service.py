from app.services import UserService ,InstructorService 
from app.saga import SagaBuilder, SagaError

def funcionalidad(self) -> None:
    user = UserService()
    instructor = InstructorService()
    try:
        SagaBuilder.create() \
            .action(lambda:user.get_data(), lambda:user.get_compensation()) \
            .action(lambda:instructor.get_data(), lambda:instructor.get_compensation()) \
            .build().execute()
    except SagaError as e:
        print(e)
