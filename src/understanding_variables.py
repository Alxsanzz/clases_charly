# Let's try to use variables
message = "This is my first program :), I am very happy"
another_message = "Really, so so so so happy"

print(message)
print(another_message)

print(message,another_message)
print(another_message,message)

message = "Hi boys & girls"
print(message)

"""
    Reglas geneales para nombrar variables en PYTHON

    Los nombres de variables deben nombrarse solo con:

    - Palabras en ingles
    - Letras, numeros, y guión bajo
    - Deben comenzar con na letra o guión bajo, pero no con números
    - No utilizar espacios para separar palabras (uttilizar _)
    - No utilizar palabras reservadas de python o el nombre del
      archivo como nombre de variable
    - Los nombres deben de ser cortos, pero descriptivos
    - Letras minusculas, !!!por ahora!!! 

    Ejemplo:
    correcto: message_1, _message_1
    incorrecto: 1message_1

"""

message = "Hola amigo python"
print(message)

hi = "Hola, mundo(print)"
print(hi)



"""
  Traceback: Es un registro de donde el interprete tuvo problemas al intentar ejecutar codigo

  NameError: Sucede cuando olvidamos establecer el valor de una variable antes de utilizarla o cometimos
  un error ortografico al ingresar el nombre de la variable (typos).
"""

name = "aleXiS coVarrUbiaS 22"
print(name)

ap = print(name.title())

exec("ap")

nam = "Covarrubias"
print(nam.upper())

na = "Sanchez"
print(na.lower())
