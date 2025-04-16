#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#Definición de funciones

def operaciones_básicas(a,b):
    return [ a+b , a-b , a * b , a/b]

#Programa principal

num1= float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

cuentas = operaciones_básicas(num1,num2)
print(cuentas)