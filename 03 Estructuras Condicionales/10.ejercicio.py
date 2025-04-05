#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio se encuentra (N/S)?: ")
mes = int(input("Escriba en números el mes del año: "))
dia = int(input("Escriba el día: "))

estacion = ""

if hemisferio == "N" or hemisferio == "n":
    if (mes == 3 and dia >= 21) or (mes== 4) or (mes== 5) or (mes == 6 and dia < 21):
        estacion = "primavera"
    elif (mes == 6 and dia >= 21) or (mes== 7) or (mes== 8) or (mes == 9 and dia < 21):
        estacion = "verano"
    elif (mes == 9 and dia >= 21) or (mes== 10) or (mes== 11) or (mes == 12 and dia < 21):
        estacion = "otoño"
    elif (mes == 12 and dia >= 21) or (mes== 1) or (mes== 2) or (mes == 3 and dia < 21):
        estacion = "invierno"
    else:
        print("Coloque una fecha válida")
elif hemisferio == "S" or hemisferio == "s":
    if (mes == 3 and dia >= 21) or (mes== 4) or (mes== 5) or (mes == 6 and dia < 21):
        estacion = "otoño"
    elif (mes == 6 and dia >= 21) or (mes== 7) or (mes== 8) or (mes == 9 and dia < 21):
        estacion = "invierno"
    elif (mes == 9 and dia >= 21) or (mes== 10) or (mes== 11) or (mes == 12 and dia < 21):
        estacion = "primavera"
    elif (mes == 12 and dia >= 21) or (mes== 1) or (mes== 2) or (mes == 3 and dia < 21):
        estacion = "verano"
    else:
        print("Coloque una fecha válida")
else:
    print("Ingrese S/N para el hemisferio")        


if estacion != "":
    print("Según el hemisferio y la fecha, la estación es: " + estacion)