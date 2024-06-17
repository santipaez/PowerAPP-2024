import unittest
from app import create_app

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_testing_config(self):
        self.assertTrue(self.app.config['TESTING'])

if __name__ == "__main__":
    unittest.main()
