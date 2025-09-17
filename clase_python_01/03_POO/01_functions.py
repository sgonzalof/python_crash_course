###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

# from os import system
# if system("clear") != 0: system("cls")

#  """ 
#  Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

#  """

# Ejemplo de una función para imprimir algo en consola
def saludar():
  print("¡Hola!")

print("\n\n\n")
# Ejemplo de una función con parámetro
def saludar_a(nombre):
  print(f"¡Hola {nombre}!")

saludar_a("midudev")
saludar_a("madeval")
saludar_a("pheralb")
saludar_a("felixicaza")
saludar_a("Carmen Ansio")
print("\n\n\n")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)
# print("\n\n\n")


# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))
# print("\n\n\n")


# Argumentos por posición
def describir_persona(nombre: str, edad: int, ciudad: str):
  print(f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}")

# parámetros son posicionales
describir_persona(1, 25, 3)
describir_persona("Sergio", 32, "Oviedo")
describir_persona("Oviedo", "Sergio", 39)

# # Argumentos por clave
# # parámetros nombrados
# describir_persona(ciudad="Oviedo", nombre="Sergio", edad=32)
# print("\n\n\n")

# # Argumentos de longitud de variable (*args):
# def sumar_numeros(*args):
#   suma = 0
#   for numero in args:
#     suma += numero
#   return suma

# print(sumar_numeros(1, 2, 3, 4, 5))
# print(sumar_numeros(1, 2))
# print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))
# print("\n\n\n")


# # Argumentos de clave-valor variable (**kwargs):
# def mostrar_informacion_de(**kwargs):
#   for clave, valor in kwargs.items():
#     print(f"{clave}: {valor}")



# ### Lambdas ###

# sum_two_values = lambda first_value, second_value: first_value + second_value
# print(sum_two_values(2, 4))

# multiply_values = lambda first_value, second_value: first_value * second_value - 3
# print(multiply_values(2, 4))

# def sum_three_values(value):
#     return lambda first_value, second_value: first_value + second_value + value

# print(sum_three_values(5)(2, 4))

# mostrar_informacion_de(nombre="Sergio", edad=32, sexo="hombre")
# print("\n")
# mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
# print("\n")
# mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
# print("\n")
# mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)
# print("\n\n\n")
# # Ejercicios
# # Volver a los ejercicios anteriores
# # y convertirlos en funciones
# # e intentar utilizar todos los casos y conceptos
# # que hemos visto hasta ahora