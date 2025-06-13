#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(numero):
    if numero < 0:
        return "Ingrese un número positivo."
    elif numero >= 0 and numero < 10:
        return numero
    else:
        ultimo = numero % 10
        suma = ultimo + suma_digitos(numero//10)
    return suma

print(suma_digitos(15))