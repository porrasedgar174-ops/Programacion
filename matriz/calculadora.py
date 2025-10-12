# Calculadora de Matrices 2x2

# Definir matriz A de forma general


a11 = 2
a12 = 3
a21 = 4
a22 = 5

# Definir matriz B de forma general
b11 = 1
b12 = 0
b21 = 2
b22 = 1

# Crear las matrices con las variables
a = [[a11, a12],
     [a21, a22]]

b = [[b11, b12],
     [b21, b22]]

# Funciones


def add(a, b):
    return [[a[0][0]+b[0][0], a[0][1]+b[0][1]],
            [a[1][0]+b[1][0], a[1][1]+b[1][1]]]


def subtract(a, b):
    return [[a[0][0]-b[0][0], a[0][1]-b[0][1]],
            [a[1][0]-b[1][0], a[1][1]-b[1][1]]]


def mult(a, b):
    return [[a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
            [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]]


def mostrar(m):
    print(f"[ {m[0][0]}  {m[0][1]} ]")
    print(f"[ {m[1][0]}  {m[1][1]} ]")


# PROGRAMA
print("=== CALCULADORA DE MATRICES 2x2 ===\n")

print("Matriz A:")
mostrar(a)

print("\nMatriz B:")
mostrar(b)

print("\n--- RESULTADOS ---\n")

print("A + B =")
mostrar(add(a, b))

print("\nA - B =")
mostrar(subtract(a, b))

print("\nA × B =")
mostrar(mult(a, b))
