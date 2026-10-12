"""
    TUPLAS

    Las tuplas son listas de elementos que no cambian de tamaño
    Son listas inmutables

    Se utilizan las parentesis () para definir una tupla

    Ejemplo:

        Si tenemos un rectangulo (largo, ancho) que siempre sera del mismo tamaño
        podemos asegurar que sus dimensiones no cambuaran

"""

dimensions = (200, 50)
print("Tupla original", dimensions)



# Lista
#dimensions_2 = [200, 50]
#print("Metodos y atributos de las listas", dir(dimensions_2))


# String
#name = "Alexis"
#print("Metodos y atributos de los strings", dir(name))


# Modificar los atributos de una lista
names = ["Alexis", "Fatima", "Adhemar", "Charly"]
print(names)
names[0] = "ratilina"
names[1] = "ratilina"
names[2] = "ratilina"
print(names)


# Looping troght a tuple

for dimension in dimensions:
    print(dimension)

""" 
    Para cambiar los datos de una tupla, debemos reasignar valores en linea de codigo

"""

dimensions = (500, 1000, 20)
print("Tupla re-definida", dimensions)

print(    )
# Tipos de datos boleanos
answer = True
print(answer)
print(dir(answer))
