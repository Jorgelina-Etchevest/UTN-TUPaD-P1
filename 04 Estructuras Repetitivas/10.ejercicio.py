#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
import math
digito  = 0
inverso = 0

numero = int(input("Ingrese un número: "))

while numero != 0:
    digito = numero % 10
    numero = math.trunc(numero/10)
    inverso = inverso * 10 + digito

print(f"El inverso del número ingresado es: {inverso}")