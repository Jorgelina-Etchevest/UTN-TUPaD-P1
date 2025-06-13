#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.


def decimal_a_binario(decimal):                             
    if decimal <= 1:                                       
        return str(decimal)
    else:
        resto = decimal % 2                                                         
        entero = decimal // 2
    return decimal_a_binario(entero) + str(resto)                                



print(decimal_a_binario(10))