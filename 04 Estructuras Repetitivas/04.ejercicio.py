# Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

numero = int(input("Ingrese un número entero o 0 para salir: "))
suma = 0

while numero !=0:
    suma += numero
    numero = int(input("Ingrese otro número entero o 0 para salir: "))
print(f"La suma acumulada es: {suma}")