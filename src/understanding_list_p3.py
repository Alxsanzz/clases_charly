"""
print("\ntel dia de hoy aprendere a trabajar cn listas\n".upper())

magicians = ["harry", "ron", "hermione", "snape", "voldemort"]
print(magicians)
print("     ")

print("imprimir a la mala")
print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4])

print("    ")
# ciclo for
print("imrprimir con un for")
for magician in magicians:
    print(magician, end= " ")
print("    ")

print("    ")
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo")
    print(f"No puedo esperar para ver el siguiente hechizo {magician.title()}")
print("Gracias a todos, ese fue un gran espectaculo")

"""
"""
    La identación es muy importante en Python, ya que indica qué código pertenece a qué bloque. 
    En este caso, el código dentro del bucle for está indentado para mostrar que pertenece al bucle.
"""

# No olvidemos identar - Traceback identatiónError
#magicians = ["alice", "david", "caroline"]
#for magician in magicians:
# print(magician) # Identation Error

# Error de logica
#for magician in magicians:
#    print(magician) 
#print(f"No puedo esperar para ver el siguiente hechizo {magician.title()}")

# Identación inncecesaria
#messsage = "Hello Python world!"
#    print(messsage) # IndentationError: unexpected indent


# NO olvidar los dos puntos
#for magician in magicians
#    print(magician) # SyntaxError: expected ':'
