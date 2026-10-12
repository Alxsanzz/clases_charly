players = ["Piter", "Mercado", "ratilina", "charly"]
print("Lista original: ", players)

# Slicing
print(players [2:4])

"""
    El slicing me permite trabajar con un gurpo de strings especifico
    el resultado seria "un slice"
"""

print(players[0:2])
print(players[0:])
print(players[0:1])

students = ["Piter", "Mercado", "ratilina", "charly"]
for student in students[2:4]:
    print(f"El estudiante {student}, va a pasar la materia")

print(students)
