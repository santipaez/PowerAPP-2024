from app.services import UserService, InstructorService, GymClassService
from app.saga import SagaBuilder, SagaError

def funcionalidad(self) -> None:
    user = UserService()
    instructor = InstructorService()
    gym_class = GymClassService()
    try:
        SagaBuilder.create() \
            .action(lambda:user.get_data(), lambda:user.get_compensation()) \
            .action(lambda:instructor.get_data(), lambda:instructor.get_compensation()) \
            .action(lambda:gym_class.get_data(), lambda:gym_class.get_compensation()) \
            .build().execute()
    except SagaError as e:
        print(e)
