#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

#Definicion de funciones

def segundos_a_horas(s):
    return round((s / 3600),2)


#Programa principal

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"La cantidad de horas correspondientes a {segundos} segundos es: {horas} horas")