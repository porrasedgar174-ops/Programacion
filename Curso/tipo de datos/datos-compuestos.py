# Creando una lista (se puede modificar)
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]

# Creando una tupla (no se puede modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

# esta es valido
# lista[3] = "mate"

# esto no es valido
# tupla[3] = "mate"

# Creando un conjunto (set) (no se accede a los elementos por indice, no lamacena datos duplicados)

conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}

# print(conjinto[3]) -> no puede acceder al elemento


# crando diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre': "Soy Dalto",
    'Canal': "Soy Dalto",
    'esta_emocionado': True,
    'altura': 1.84,
    'dato_duplicado': "Soy Dalto"

}

print(diccionario['Canal'])
