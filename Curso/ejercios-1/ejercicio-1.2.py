
# Le pedimos al ususario que nos diga uan frase(o varias)
frase = input(
    "Escribe una frase y te calculamos tardarias si tuvieras que decrila: ")

#  Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabbras_separadas = frase.split(" ")

# Usamos len() para ver la cantidad de palabras que hay en la lista
cantidad_de_palabras = len(palabbras_separadas)

# En caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Mucho texto")


# Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(
    f'Dalto lo diria en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos')
