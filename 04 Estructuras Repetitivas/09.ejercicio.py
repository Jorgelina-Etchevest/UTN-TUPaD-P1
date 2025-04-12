# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
suma = 0
cantidad = 100


for x in range (100, 0, -1):
    cantidad -= 1
    numero = int(input("Ingrese un número entero: "))
    suma += numero
    

promedio = suma/10

print(f"El promedio de los números ingresados es {promedio}")
