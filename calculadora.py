# Programa que saluda al usuario por su nombre y apellido

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Hola bienvenido a la calculadora " + nombre.strip().lower().capitalize() +
      " " + apellido.strip().lower().capitalize())

numero1 = float(input("Ingrese un numero: "))

numero2 = float(input("Ingrese otro numero: "))

suma = numero1 + numero2

resta = numero1 - numero2

multiplicacion = numero1 * numero2

division = numero1 / numero2

potencia = numero1 ** numero2


# relacion de numeros
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero1} es menor que {numero2}")
else:
    print(f"{numero1} es igual a {numero2}")


class NumeroMagico:
    def _init_(self, valor):
        self.valor = valor  # atributo principal

    def _call_(self, incremento=1):
        """
        Permite que el objeto sea "llamado como función".
        Cada vez que se llame, se incrementa el valor.
        """
        if incremento > 0:
            self.valor += incremento
        else:
            print("⚠ El incremento debe ser positivo.")
        return self.valor

    def _add_(self, otro):
        """
        Suma el valor de este objeto con otro (entero o NumeroMagico).
        """
        if isinstance(otro, NumeroMagico):
            return NumeroMagico(self.valor + otro.valor)
        elif isinstance(otro, (int, float)):
            return NumeroMagico(self.valor + otro)
        else:
            raise TypeError(
                "Solo se puede sumar con int, float o NumeroMagico.")

    def _str_(self):
        """
        Representación en string del objeto.
        """
        return f"NumeroMagico(valor={self.valor})"


print("------La Suma------")
print(f'{numero1} + {numero2} = {suma}')
print("------La Resta------")
print(f'{numero1} - {numero2} = {resta}')
print("------La Multiplicacion------")
print(f'{numero1} * {numero2} = {multiplicacion}')
print("------La Division------")
print(f'{numero1} / {numero2} = {division}')
print("------La Potencia------")
print(f'{numero1} ** {numero2} = {potencia}')

print("---------------------------------------------------------------------------------")

print(f'Gracias {nombre.strip().lower().capitalize()} {apellido.strip().lower().capitalize()} por utilizar la calculadora. ')

