import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'HOLA MUNDO CRUEL', response.data)  # Corregir cadena esperada

if __name__ == '__main__':
    unittest.main()

