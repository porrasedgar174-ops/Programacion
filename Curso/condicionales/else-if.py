ingreso_mensual = 15000
gasto_mensual = 16000


# if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual >= 5000:
        print("ahora si estas bien")
    else:
        print("estas gastando mucho")

elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")

else:
    print("eres pobre")


goles = 60
goles_contra = 40

if goles > 12:
    if goles - goles_contra < 0:
        print("Van perdinedo detro el torneo")
    elif goles - goles_contra <= 10:
        print("estan bien")
    else:
        print("son goleadores")
