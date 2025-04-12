# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for x in range (0,numero+1):
    suma += x

print(f"La suma desde 0 hasta el número ingresado es: {suma}")