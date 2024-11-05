import collections
import re
from gc import collect
from itertools import count

oracion = input("Ingresa una oracion: ")
expresion = re.sub(r"[^a-zA-Z0-9]", " ", oracion)

lista = list(map(lambda x:  x.lower(),expresion.split(" ")))
lista = [elemento for elemento in lista if elemento.strip()]
print(lista)
diccionario = collections.Counter(lista)


mayores = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)[:2]

# Imprimir la mayor palabra y la segunda mayor
for i, (palabra, frecuencia) in enumerate(mayores, start=1):
    print(f"{i}ª Mayor Palabra: {palabra}, Frecuencia: {frecuencia}")