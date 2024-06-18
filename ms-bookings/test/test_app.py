import unittest
from app import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_create_app(self):
        self.assertIsNotNone(self.app)

if __name__ == "__main__":
    unittest.main()
    