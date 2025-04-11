#Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
suma = 0

if numero_uno >= numero_dos:
    print("El primer número debe ser inferior al segundo")
else:
    while (numero_uno + 1) < numero_dos:
        numero_uno += 1
        suma = suma + numero_uno
    print(f"La suma de los valores comprendidos entre los dos números ingresados es {suma}")



