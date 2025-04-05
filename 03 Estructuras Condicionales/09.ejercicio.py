#9)	Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#●	Menor que 3: "Muy leve" (imperceptible).
#●	Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#●	Mayor o igual que 4	y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#●	Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#●	Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#●	Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Escriba la magnitud del terremoto según la escala de Richter: "))

if magnitud < 3:
    print("El terremoto es clasificado como: Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("El terremoto es clasificado como: Leve")
elif magnitud >= 4 and magnitud < 5:
    print("El terremoto es clasificado como: Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("El terremoto es clasificado como: Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("El terremoto es clasificado como: Muy fuerte")
else:
    print("El terremoto es clasificado como: Extremo")

