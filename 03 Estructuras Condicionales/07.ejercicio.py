#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase o palabra: ")

ultimo_caracter= frase[-1].lower()

if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u":
    print(frase + "!")
else:
    print(frase)
