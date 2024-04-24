import unittest

from data_base import buscar_datos
from data_base import database


class TestBusqueda(unittest.TestCase):
    def test_ordenado(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,"1")

    def test_no_ordenado(self):
        resultado = buscar_datos("Anci","Elio", **database)
        self.assertEqual(resultado,"2")

    def test_ordenado_extra(self):
        resultado = buscar_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", **database)
        self.assertEqual(resultado,"3")

    def test_mezclado(self):
        resultado = buscar_datos("Elias", "Pablo", "Ruiz", **database)
        self.assertEqual(resultado,None)

    def test_no_existente(self):
        resultado = buscar_datos("Aguante", "Boca", **database)
        self.assertEqual(resultado,None)

    def test_agregado_uno(self):
        resultado = buscar_datos("Anci", "Diego", "Elio", **database)
        self.assertEqual(resultado,None)

    def test_yo(self):
        resultado = buscar_datos("Nicolas","Guillermo","Ventin","Elaskar", **database)
        self.assertEqual(resultado,"4")


if __name__ == '__main__':
    unittest.main()