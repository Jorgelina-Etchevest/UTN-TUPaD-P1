#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
pares=0
impares=0
positivos=0
negativos=0


for x in range (1, 101):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 ==0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"La cantidad de números pares es {pares}, la cantidad de números impares es {impares}, la cantidad de números positivos ingresados es {positivos} y la cantidad de números negativos es {negativos}")


