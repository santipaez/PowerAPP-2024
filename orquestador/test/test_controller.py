import unittest
from app import create_app
from app.services import UserService, InstructorService
from app.services.atomic_process import AtomicProcess

class ControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.user = UserService()
        self.instructor = InstructorService()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_atomic_process(self):
        atomic_process = AtomicProcess()
        response = atomic_process.execute()
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()