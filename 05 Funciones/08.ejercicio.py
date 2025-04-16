#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#Definición de funciones

def calcular_imc(p, a):
    return round(p/(a**2),2)


#Programa principal

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = calcular_imc(peso,altura)
print(f"El índice de masa corporal es: {imc}")