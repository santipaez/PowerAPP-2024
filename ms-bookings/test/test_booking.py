import unittest
from app.models import Instructor  # Importa el modelo Instructor desde app.models
from app import create_app, db

class TestInstructor(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_instructor(self):
        instructor = Instructor()  # Cambia Instructor por instructor
        instructor.email = "test@gmail.com"
        self.assertEqual(instructor.email, "test@gmail.com")
    
    def test_create_instructor(self):
        instructor = self._create_instructor()  # Cambia Instructor por instructor
        self.assertEqual(instructor.id, 1)

    def _create_instructor(self):
        instructor = Instructor()  # Cambia Instructor por instructor
        instructor.email = "test@gmail.com"
        instructor.name = "alvaro"
        instructor.password = "123"
        instructor.specialty = "test"
        db.session.add(instructor)
        db.session.commit()
        return instructor
    
if __name__ == '__main__':
    unittest.main()
