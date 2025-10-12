# class mi_primera_clase():
#     """
#     Esta clase no hace nada
#     """
#     pass


# class mi_primera_clase():

#     """
#     Esta clase no hace nada

#     """

#     def __init__(self, name: str, age: int):
#         self.nombre = name
#         self.edad = age
#         if self.edad >= 20:
#             self.mayor = "no pasa"


# instancia1 = mi_primera_clase("Pedrito", 21)
# instancia2 = mi_primera_clase("Edgar", 23)

# print(instancia1.nombre)
# print(instancia1.edad)
# print(instancia2.nombre)
# print(instancia2.edad)


class vector():
    """
    Implementación de un vector
    """

    def __init___(self, x: float, y: float, z: float = None):
        self.x = x
        self.y = y
        if not z:
            self.z = z
            self.Espacio = True
        else:
            self.Espacio = False
        self.modulo = abs(self)  # define el valor absoluto

    def __str___(self):
        if self.Espacio:
            # : es para abrir la configuracion del dato
            respuesta = f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
        else:
            # :.2f me dice que coja dos decimales del valor float
            respuesta = f"({self.x:.2f}, {self.y:.2f})"
        return (respuesta)

    def __abs__(self):
        if self.Espacio:
            return (pow(self.x**2+self.y**2+self.z**2, 0.5))
        else:
            return (pow(self.x**2+self.y**2, 0.5))

    def __add__(self, other):
        coordenadaX = self.x + other.x
        coordenadaY = self.y + other.y
        coordenadaZ = self.z + other.z
        # no necesariamente tiene que ser una suma.
        # self.x es el vector que estamos trabajando
        return (vector(self.x + other.x, self.y + other.y, self.z + other.z))


v1 = vector(2, 3, 1)
v2 = vector(4, 5, 6)
print(v1)
print(v2)

v1 = vector(2, 3, 1)
v2 = vector(4, 5, 6)
print(v1+v2)
print(abs(v1+v2))
