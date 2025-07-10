### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Sergio",
                 "Apellido": "Gonzalo",
                 "Edad": 32,
                  1: "Python"}

my_dict = {
    "Nombre": "Sergio",
    "Apellido": "Gonzalo",
    "Edad": 32,
    "Lenguajes": {"Python", "Java", "Kotlin", "C#"},
    1: 1.75
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
print("\033[92m \n\nBúsqueda")
print(f"my_dict: {my_dict}\033[0m'")

print(my_dict[1])
print(my_dict["Nombre"])
print("Sgonzalof" in my_dict)
print("Apellido" in my_dict)


# Inserción
print("\033[92m \n\Inserción")
print(f"my_dict: {my_dict}\033[0m'")
my_dict["Ciudad"] = "Oviedo"
print(my_dict)


# Actualización
print("\033[92m \n\Actualización")
print(f"my_dict: {my_dict}\033[0m'")
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación
print("\033[92m \n\Eliminación")
print(f"my_dict: {my_dict}\033[0m'")
del my_dict["Calle"]
print(my_dict)

# Otras operaciones
print("\033[92m \n\Otras operaciones")
print(f"my_dict: {my_dict}\033[0m'")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
