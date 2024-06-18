import unittest
from app import create_app, db
from sqlalchemy import text

class DbTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_db_connection(self):
        connection = db.session.query(text("'Hola Mundo'")).one()
        self.assertEqual(connection[0], 'Hola Mundo')