#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

posicion = int(input("Ingrese el número para calcular la serie de Fibonacci:  "))

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1)+fibonacci(posicion-2)
    
serie = [fibonacci(i) for i in range(posicion + 1)]

print(f"La serie de Fibonacci hasta la posición {posicion} es: {serie}")