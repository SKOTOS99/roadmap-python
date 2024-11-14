from datetime import datetime

def isMayor(age):
    return "es mayor de edad" if int(age) > 18 else "no es mayor de edad"

def caculeYearsOld(age):
    date = datetime.now()
    year = date.strftime('%Y')
    return  int(year) - int(age)

name = input("como se llama: ")
age = input("ingrese su edad: ")
print(f"{name} tu año de nancimiento es:{caculeYearsOld(age)} ")
print(isMayor(age))

