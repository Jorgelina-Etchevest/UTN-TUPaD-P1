#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#Definición de funciones 

def celsius_a_fahrenheit(c):
    return 32 + c * 1.8


#Programa principal

grados = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(grados)
print(f"La temperatura en grados Fahrenheit es {fahrenheit}")