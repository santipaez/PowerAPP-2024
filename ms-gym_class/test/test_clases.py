import unittest
from app import create_app, db
from app.models.gym_class import GymClass

class TestGymClasses(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_gym_class_create(self):
        new_class = GymClass(name="Test Clases", instructor="John Doe", duration=60)
        db.session.add(new_class)
        db.session.commit()
        self.assertEqual(new_class.name, "Test Clases")
        self.assertEqual(new_class.instructor, "John Doe")
        self.assertEqual(new_class.duration, "60")


    def test_gym_class_update(self):
        new_class = GymClass(name="Test Clases", instructor="John Doe", duration=60)
        db.session.add(new_class)
        db.session.commit()
        new_class.name = "New Test Clases"
        db.session.commit()
        self.assertEqual(new_class.name, "New Test Clases")

    def test_gym_class_delete(self):
        new_class = GymClass(name="Test Clases", instructor="John Doe", duration=60)
        db.session.add(new_class)
        db.session.commit()
        db.session.delete(new_class)
        db.session.commit()
        self.assertIsNone(db.session.query(GymClass).get(new_class.id))
        

if __name__ == '__main__':
    unittest.main()