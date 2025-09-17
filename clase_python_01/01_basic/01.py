# # # HELLO WORLD
# # print("Hello, World!")
# # # This is a comment
# # """This is a multi-line comment
# # that spans multiple lines."""


# # Variables
# name = "Sergio"
# surname = "Gonzalo"
# age = 32
# height = 1.75
# uses_glasses = True


# # # Print variables
# # print("Name:", name)
# # print("Surname:", surname)
# # print("Age:", age)  
# # print("Height:", height)

# print(f'My name is {name}, I am {age} years old and my height is {height} meters.')

# print(
#     f'My name is {name}, I am {age} years old '
#     f'and my height is {height} meters.'
# )



# # Inputs
# # name = input('¿Cuál es tu nombre? ')
# # age = input('¿Cuántos años tienes? ')
# print(name)
# print(age)


# # # Types
# # print("Type of name:", type(name))
# # print("Type of age:", type(age))
# # print("Type of height:", type(height))
# # print("Type of uses_glasses:", type(uses_glasses))




### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

