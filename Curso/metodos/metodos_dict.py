
diccionario = {
    "nombre": 'lucas',
    "apelldio": 'dalto',
    "dinero": 10000,

}

# Devuelve las claves (tambien sirve para ietrar)
# Nos devuelve un objeto dict_item
claves = diccionario.keys()


# Obteniendo un elemento con get() (no me lanza una excepcion y si no encunetra nada el programa conitnua)
valor_de_dinero_ = diccionario.get("dinero")


# Eliminando todo del diccionario
# diccionario.clear()


# Eliminando un elemento del diccionario
diccionario.pop("nombre")


# Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
