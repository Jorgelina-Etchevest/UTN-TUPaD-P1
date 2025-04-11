# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

num_aleatorio = random.randint(0,10)
print(num_aleatorio)
num_ingresado=int(input("Ingrese un número entero entre 0 y 9: "))
intentos = 1

while num_ingresado != num_aleatorio:
    intentos += 1
    print("No has acertado, intenta nuevamente!")
    num_ingresado=int(input("Ingrese un nuevo número entero entre 0 y 9: "))

print(f"Adivinar el número te llevo {intentos} intento/s")