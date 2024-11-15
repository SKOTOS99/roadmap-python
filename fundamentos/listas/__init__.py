from functools import reduce
from io import StringIO


class Listas:

    def suma_numeros(self, numeros):
        return reduce((lambda x,y: x+y), numeros)

    def media_numeros(self, numeros):
        return reduce((lambda x,y: x+y), numeros)/len(numeros)

    def filtra_pares(self, numeros):
        return list(filter((lambda x: x % 2 == 0), numeros))

    def ordena_desc(self, numeros):
        return sorted(numeros, reverse=True)

    def printResultado(self,numeros):
        _file_str = None
        _file_str = StringIO()
        _file_str.write(f"suma: {self.suma_numeros(numeros)}\n")
        _file_str.write(f"media: {self.media_numeros(numeros)}\n")
        _file_str.write(f"pares: {self.filtra_pares(numeros)}\n")
        _file_str.write(f"orden desc: {self.ordena_desc(numeros)}\n")
        return _file_str.getvalue()

numeros = [10, 23, 5, 8, 19, 2]

x = Listas()
print(x.printResultado(numeros))


