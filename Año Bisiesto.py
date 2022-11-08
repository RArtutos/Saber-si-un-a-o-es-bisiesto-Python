def comprobador(a):
    if (int(a) % 4 == 0):
        return 1
    else:
        return 0

año = input("Escribe un año para comprobar si es bisiesto: ")


if (comprobador(año) == 1):
    print(año, "es bisiesto")
else:
    print(año, "no es bisiesto")