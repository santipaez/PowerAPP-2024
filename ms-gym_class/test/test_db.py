import unittest
import psycopg2
import os
from dotenv import load_dotenv

class TestDatabase(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        try:
            self.connection = psycopg2.connect(
                host='postgresql.powerapp.localhost',
                port=5432,
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASS'),
                database=os.getenv('DB_NAME_USER')
            )
            self.cursor = self.connection.cursor()
            self.connection.autocommit = False
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def tearDown(self):
        self.connection.rollback()
        self.cursor.close()
        self.connection.close()

    def test_database_connection(self):
        print("\n--- Testing the Database Connection ---")
        self.assertIsNotNone(self.connection)

if __name__ == "__main__":
    unittest.main()