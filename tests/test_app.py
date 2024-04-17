
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hola, mundoo!', response.data)

if __name__ == '__main__':
    unittest.main()

# import pytest
# from app import app

# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client

# def test_index(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'Hola, mundoo!' in response.data
