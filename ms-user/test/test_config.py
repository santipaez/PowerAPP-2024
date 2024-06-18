import unittest
from app.config.config import DevelopmentConfig, ProductionConfig, factory

class TestConfig(unittest.TestCase):

    def test_development_config(self):
        config = DevelopmentConfig()
        self.assertTrue(config.TESTING)
        self.assertTrue(config.DEBUG)
        self.assertEqual(config.FLASK_ENV, 'development')
        self.assertTrue(config.SQLALCHEMY_TRACK_MODIFICATIONS)

    def test_production_config(self):
        config = ProductionConfig()
        self.assertFalse(config.TESTING)
        self.assertFalse(config.DEBUG)
        self.assertEqual(config.FLASK_ENV, 'production')
        self.assertFalse(config.SQLALCHEMY_RECORD_QUERIES)

    def test_factory(self):
        self.assertEqual(factory('development'), DevelopmentConfig)
        self.assertEqual(factory('production'), ProductionConfig)

if __name__ == '__main__':
    unittest.main()