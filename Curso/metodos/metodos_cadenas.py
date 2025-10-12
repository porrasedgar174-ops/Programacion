cadena1 = "hola,soy,Dalton"

cadena2 = "bienvenido maquinola"


# convierte a mayuculas
mayusc = cadena1.upper()


# convierte a minusculas
minusc = cadena1.lower()


# convierte primera letra en mayuculas
primera_letra_mayusc = cadena1.capitalize()


# buscamos una cdena en otra cadena, si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("a")


# buscamos una cadena en otra cadena, si no hay coincidencia devuelve una excepcion
busqueda_index = cadena1.index("a")


# si es numerico devuelve true, sino devolvemos false
es_numerico = cadena1.isnumeric()

# si es alfa numerico devolvemos true,  sino devolvemos false
es_alfanumerico = cadena1.isalpha()


# contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")


# contamos cauantos carateres tiene una cadena
contar_carateres = len(cadena1)


# verificamos si un cadena empieza con otra cadena dada, si es asi devuelve true
empieza_com = cadena1.startswith("Hola")


# verificamos si un cadena termina con otra cadena dada, si es asi devuelve true
termina_com = cadena1.endswith("n")


# si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(",", " ")
cadena_nueva2 = cadena_nueva.capitalize()


# separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada[2])
