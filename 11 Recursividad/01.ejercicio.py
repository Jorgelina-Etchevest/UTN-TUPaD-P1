#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

num = int(input("Ingrese el número del que desea el factorial: "))

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(f"El número factorial del número que usted ingresó es: ",factorial(num))

