import unittest
from fundamentos.Aritmetics import Aritmetics

class TestAritmetics(unittest.TestCase):

    def setUp(self):
        self.aritmetics = Aritmetics()  # Crear una instancia para reutilizar en cada prueba

    def test_sumas(self):
        self.assertEqual(self.aritmetics.sumar( 5, 5), 10)
    def test_restas(self):
        self.assertEqual(self.aritmetics.restar( 10,5), 5)
    def test_multiplicacion(self):
        self.assertEqual(self.aritmetics.multiplicacion( 10,5), 50)
    def test_diviciones(self):
        self.assertEqual(self.aritmetics.divisiones( 10,5), 2)
    def test_divisionCero(self):
        with self.assertRaises(ZeroDivisionError):
            self.aritmetics.divisiones( 10, 0)
    def test_print(self):
        self.assertEqual(self.aritmetics.printResultado(10,5),  "suma: 15\nresta: 5\nmultiplicacion: 50\ndivision: 2")