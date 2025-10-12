

# Creando ina lista con list()
lista = list(["Hola", "Dalto", 34])


# Devuelve la cantidad de elemnteos de la lista
cantidad_de_elementos = len(lista)


# Agregando elementos a una lista
lista.append(123)


# Agragando un elemneto a la lista en un indice especifico
lista.insert(0, "entonces")


# Agregando varios elementos a la lista
lista.extend([256, "si", 15, 86, 500])


# Eliminando un elemnto de la lista por su indice (posicion)
lista.pop(0)
lista.pop(1)
lista.pop(0)

# # el -1 elimina el ultimo elemento de la lista y el -2 el penultimo, y asi sucesivamente
lista.pop(-4)


# # Removineod un elemnto de la lista por su valor
lista.remove(500)


# Eliminando todos los elementos de la lista
# lista.clear()

# Ordena la lista de menor a mayor ( si se usa el parametro reverse=True invierter el orden) no funciona con textp
lista.sort()
lista.sort(reverse=True)


# Invirtiendo los elementos de una lista
lista.reverse()


# Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(15)

print(elemento_encontrado)
