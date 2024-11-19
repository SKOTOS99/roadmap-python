import unittest

from fundamentos.listas import Listas, numeros


class TestListas(unittest.TestCase):

    def setUp(self):
        self.listas = Listas()
        numeros = [10, 23, 5, 8, 19, 2]

    def test_suma_numeros(self):
        self.assertEqual(self.listas.suma_numeros(numeros), 67)

    def test_media(self):
        self.assertEqual(self.listas.media_numeros(numeros), 11.166666666666666)

    def test_pares(self):
        self.assertListEqual(self.listas.filtra_pares(numeros),[10, 8, 2],"el resultado debe ser [10, 8, 2]")

    def test_ordenamiento(self):
        self.assertListEqual(self.listas.ordena_desc(numeros), [23, 19, 10, 8, 5, 2], "el resultado debe ser [23, 19, 10, 8, 5, 2]")

    def test_print(self):
        self.assertEqual(self.listas.printResultado(numeros), "suma: 67\nmedia: 11.166666666666666\npares: [10, 8, 2]\norden desc: [23, 19, 10, 8, 5, 2]")