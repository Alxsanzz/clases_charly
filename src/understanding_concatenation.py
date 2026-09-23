# combinación o concatención de strings
first_name = "alexis"
last_name = "sanz"
full_name = first_name + " " + last_name
print(full_name.title())
print(full_name.upper())
print(full_name.lower())

print("hola".title() ,first_name.title() + " " + last_name.title())


# Whitespace
"""
    Whitespace se refiere a cualquier caracter que no se imprime, es decir, un espacio ( ),
    tabuladores (\t) y finales de línea (\n).

    Los whitespaces se utilizan comunmente para 
    orfanuzar las salidas de texto a usuario de tal manera que sea mas a igable de leer
    o ver para los usuarios.
"""

print("python")
print("\tpython")
print("\t\tpython")
print("lenguajes:\n\tpython\nC\nJavaScript")

# Concatenación de strings utilizando F-strings

famous_person = "Ratilina"
message = f" {famous_person.upper()} una vez dijo: Python is love"
print(message)
