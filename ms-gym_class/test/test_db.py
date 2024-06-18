import unittest
from app import create_app, db
from sqlalchemy import text

class DatabaseTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_connection(self):
        result = db.session.query(text("'Hello World'")).one()
        self.assertEqual(result[0], 'Hello World')

if __name__ == "__main__":
    unittest.main()