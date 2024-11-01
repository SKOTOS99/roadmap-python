def valueType(value):
    # Diccionario de casos con funciones lambda para cada tipo de entrada
    cases = {
        value.replace('.', '', 1).isdigit() and value.count('.') <= 1: lambda: round(float(value), 2),  # Redondea el valor decimal a dos decimales
        value.isdigit() or (value[0] == '-' and value[1:].isdigit()): lambda: int(value) * 2,
        value.isalpha(): lambda: value.upper(),
    }

    # Selecciona la función correspondiente y ejecuta
    result_function = cases.get(True, lambda: "Entrada no válida")
    return result_function()  # Llama a la función correspondiente

value = input("Ingrese un número o palabra: ")
print(f"El resultado es: {valueType(value)}")

