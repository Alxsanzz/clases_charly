# Agregando elementos a una lista
motorcycles = ["honda", "mortalica", "yamaha"]
print(motorcycles)
motorcycles.append("kawasaki")
print(motorcycles)

"""
    El metodo append ayuda a crear listas facilmente 
    de manera dinamica
"""

motorcycles_2 = [] # Lista vacia
print(motorcycles_2)
motorcycles_2.append("honda")
motorcycles_2.append("yamaha")
motorcycles_2.append("ducati")
print(motorcycles_2)

motorcycles_2.insert(1,"" )
print(motorcycles_2)


list = ["ola", "adios", "hola"]
print(list)
print("     ")
deleted_list = list.pop()
print(f"tu elemento borrado fue {deleted_list}")

suma = 4 + 4
print(f"tu numero es {suma}")
