#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

#Desarrollo de funciones

def calcular_promedio(a,b,c):
    return round((a+b+c)/3, 2)


#Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1,num2,num3)
print(f"El promedio es {promedio}")