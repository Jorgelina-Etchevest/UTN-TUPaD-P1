#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Definición de funciones

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")   #return es opcional en las funciones de python



#Programa principal 

numero = int(input("Ingrese un número del 1 al 10: "))
print(tabla_multiplicar(numero))