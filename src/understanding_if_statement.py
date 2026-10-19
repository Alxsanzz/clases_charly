cars = ["Audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)



# El Condicional es el corazón de un if

# Para determinar igualdad (==)
# Condicional True
print("\nCondicional True")
truck = "Ford"
print(truck == "Ford")
print(truck == "ford".title())

# Condicional Falso
print("\nCondicional Falso")
print(truck == "cheyenne")
print(truck == "ford")


# Condicional != para determinar desigualdad
print("\nCondicional de Desigualdad")
print(truck != "tacoma") # True
print(truck != "Ford") # False


# Comparaciones numericas
print("\nComparaciones Numericas")
age = 18
print(age == 18) # True
print(age == 19) # False
print(age == "18") # False

print("   ")
#answer = input(f"¿Numero? {67/5}")
#if answer ==  67:
#    print("sixseven")
#else:
#    print("buuuu")



"""
age = 20
print(age < 30) # True
print(age <= 20) # True
print(age > 21) # False
print(age >= 21) # False

"""


respuesta = input("¿Numero? (67/66):")

if respuesta.lower() == "67":
    print("sixsemennn")
else:
    print("buuuu")


