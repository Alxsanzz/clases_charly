# Listas de números
"""
    Las listas de números son una colección de elementos que pueden ser manipulados y utilizados en programas de Python.
    Pueden contener números enteros, flotantes o incluso otros tipos de datos.
"""

# Metodo build in range() para crear una lista de números

for value in range(1, 6):
    print(value)    

# Crear una lista de números utilizando list() y range()
numbers = list(range(0, 10))
print(numbers)

# Lista de numero pares
even_numbers = list(range(0, 11, 2))
print(even_numbers)

# Lista de números impares
#odd_numbers = list(range(1, 11, 3))
#print(odd_numbers)

tabla_del_5 = list(range(5, 51, 5))
print(tabla_del_5)
