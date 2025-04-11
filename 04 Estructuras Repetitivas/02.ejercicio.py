#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

import math
numero = int(input("Ingrese un número entero positivo o negativo: "))
numero = abs(numero)
digitos = 0

if numero == 0:
    digitos=1
else: 
    while numero != 0:
        numero = math.trunc(numero/10)
        digitos += 1

print(f"El número ingresado contiene {digitos} dígitos") 