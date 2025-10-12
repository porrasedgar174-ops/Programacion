# Promedio duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5


# Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5


# Diferencias ed duracion

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max / 10)
diferencia_con_promedios = 100 - (dalto_curso / otros_cursos_promedio * 100)


# Calculamos el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = 100 - (otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

# Mostrando las diferencias de duracion (ejercicio A)
print("---------------------------")
print("El curso de Dalto dura:")
print(f' - Un {diferencia_con_min}% menos que el mas rapido')
print(f' - Un {diferencia_con_max}% menos que los lentos')
print(f' - Un {diferencia_con_promedios}% menos que los cursos promedios')
print("---------------------------")

# Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de timepo vacio')
print("---------------------------")


# Mostrando diferencias  si los cursos duran 10 horas
print(
    f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(
    f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curo')
print("---------------------------")
