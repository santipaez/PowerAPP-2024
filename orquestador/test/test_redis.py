import unittest
import redis
import os
import time
from dotenv import load_dotenv

class TestRedis(unittest.TestCase):
    #Hay que revisar que todo funcione correctamente, es un test piloto
    def setUp(self):
        load_dotenv()
        self.redis = redis.Redis(host="redis.powerapp.localhost", port=6379, db=0, password=os.getenv('REDIS_PASSWORD'))
        self.redis.flushdb()

    def tearDown(self):
        self.redis.flushdb()

    def test_redis_connection(self):
        print("\n--- Testing the Redis Connection ---")
        self.assertIsNotNone(self.redis)

if __name__ == '_main_':
    unittest.main()