import unittest
from app.services.user_service import UserService
from app.models.user import User
from app import db, create_app
from flask import current_app

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_app(self):
        self.assertIsNotNone(current_app)
        
    def test_user(self):
        user = User(name="test", email="test@email.com", password="test")
        self.assertEqual(user.email, 'test@email.com')
        
    def test_create_user(self):
        user = User(name="test", email="test@email.com", password="test")
        UserService().register(user)
        self.assertIsNotNone(user)
        
    def test_update_user(self):
        user = User(name="test", email="test@email.com", password="test")
        UserService().register(user)
        db.session.commit()
        user.name = "testmodificado"
        db.session.commit()
        self.assertEqual(user.name, 'testmodificado')
        
    def test_delete_user(self):
        user = User(name="test", email="test@email.com", password="test")
        UserService().register(user)
        db.session.delete(user)
        db.session.commit()
        self.assertTrue(User.query.get(user.id) is None)
        
    def test_find_by_id(self):
        user = User(name="test", email="test@email.com", password="test")
        UserService().register(user)
        found_user = UserService().find_by_id(user.id)
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.id, user.id)
    
    def test_find_by_name(self):
        user = User(name="test", email="test@email.com", password="test")
        UserService().register(user)
        found_user = UserService().find_by_name(user.name)
        self.assertEqual(found_user.name, user.name)
