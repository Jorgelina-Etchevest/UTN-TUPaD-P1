#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1)
#. Prueba esta función en un algoritmo general.

base = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese la potencia: "))


def potencia(num1, num2):
    if num2 == 0:
        return 1
    elif num1 == 0:
        return 0
    else:
        return num1 * potencia(num1,num2-1)
    

print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")