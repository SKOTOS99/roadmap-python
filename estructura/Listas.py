from functools import reduce


def getPromedio(lista):
    return reduce((lambda x, y: x+y), lista)/len(lista)

def getMax(lista):
    return max(lista)

def getMin(lista):
    return min(lista)

def getOrderByAsc(lista):
    return sorted(lista, reverse = False)

def getOrderByDesc(lista):
    return sorted(lista, reverse=True)

lista = input("Ingrese una serie de nuemero: ")

separados = list(map(lambda x: int(x), lista.split(",")))

print(f"Tu lista: {separados}")
print(f"Pomedio en lista: {getPromedio(separados)}")
print(f"Maximo: {getMax(separados)}")
print(f"Minimo: {getMin(separados)}")
print(f"Oder by DESC: {getOrderByDesc(separados)}")
print(f"Oder by ASC: {getOrderByAsc(separados)}")