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




"""
    STRINGS
    
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples
    '' o de dobles comillas "" es considerado un string. 
    
    Ejemplos:
        "Esto es un string"
        'Esto también es un string'
        'Le dije a un amigo, "Python" es mi lenguage favorito'
        "El lenguaje 'Python' lleva el nombre por Monty Python y no por la serpiente"
"""
name = "clase de proGRamación"
print(name)

print(name.title())

"""
    Un método es una acción que python
    puede realizar en un fragmento de datos
    o sobre una variable. 
    El punto . después de la variable
    seguida del método title() dice
    que se tiene que ejecutar el 
    método title de la variable name.

    Todos lo métodos van seguidos de
    paréntesis porque en ocasiones 
    necesitan información adicional
    para funcionar, lo cual iriía
    dentro del paréntesis. En esta ocasión
    el método .title() no requiere información
    extra para ejecutarse.
    """


name = "aleXiS coVarrUbiaS 22"
print(name)

ap = print(name.title())

ak = exec("ap")

exec("ak")

nam = "Covarrubias"
print(nam.upper())

na = "Sanchez"
print(na.lower())

  