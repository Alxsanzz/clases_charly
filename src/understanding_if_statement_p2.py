# Costo de boleto en cuanto a edad

"""
age = input("Escribe tu edad: ")
print(age)
age = int(age)

if age <=4:
    cost = 0

if age >4 and age <18:
    cost = 200

if age >=18:
    cost =  500

print(f"Costo: ${cost}")
"""


print(" ")
# Codigo en un solo bloque
"""
if age <=4:
    cost = 0
elif age >4 and age <18:
    cost = 200
elif age >=18 and age <65:
    cost =  500
elif age >= 65:
    cost =  0
else:
    cost = 0

print(f"Costo: ${cost}")
"""
# Codigo para una ruleta de casino

import random

input("Presiona enter para girar la ruleta: ")
number = random.randint(0, 36)

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

if number % 2 == 0:
    print(f"El numero ganador es: {number} y es par")
else:
    print(f"El numero ganador es: {number} y es impar")

if number == 0:
    print("Color: Verde")
elif number in rojos:
    print("Color: Rojo")
else:
    print("Color: Negro")

