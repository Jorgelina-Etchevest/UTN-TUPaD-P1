#Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

#Definición de funciones

def calcular_area_circulo(r):       #dan por sentado que r es un número. 
    return  math.pi* r ** 2

def calcular_perimetro(r):   
    return 2* math.pi * r

#Programa general

import math

radio = float(input("Ingrese el radio: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro(radio)
print(f"El área del circulo es {area} y el perímetro es {perimetro}")