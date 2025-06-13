#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero < 0:
        return "Ingrese un número positivo"
    elif numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            contador_actual = 1
        else:
            contador_actual = 0
        return contador_actual + contar_digito(numero // 10, digito)

print(contar_digito(1234322, 8))