
from io import StringIO

class Aritmetics:

    def sumar(self,a,b):
        return a + b

    def restar(self,a,b):
        return a - b

    def multiplicacion(self,a,b):
        return a * b

    def divisiones(self,a,b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b

    def printResultado(self,a,b):
        _file_str = None
        _file_str = StringIO()
        _file_str.write(f"suma: {self.sumar(a,b)}\n")
        _file_str.write(f"resta: {self.restar(a, b)}\n")
        _file_str.write(f"multiplicacion: {self.multiplicacion(a, b)}\n")
        _file_str.write(f"division: {self.divisiones(a, b)}\n")
        return _file_str.getvalue()

a = int(input("ingresa el primero nuemro: "))
b = int(input("ingresa el segundo numero: "))
operaciones = Aritmetics()
print(operaciones.printResultado(a,b))
