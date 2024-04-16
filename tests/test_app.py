
import unittest

# Importa el módulo que deseas probar
from app import MiClase

class TestMiClase(unittest.TestCase):
    def test_algo(self):
        # Crea una instancia de MiClase y realiza tus pruebas
        objeto = MiClase()
        resultado = objeto.algo()
        self.assertEqual(resultado, esperado)




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
