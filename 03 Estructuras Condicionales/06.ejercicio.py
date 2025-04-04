#Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

media= mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)


if media > mediana and mediana > moda:
    print("En este conjunto de números aleatorios existe un sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("En este conjunto de números aleatorios existe un sesgo negativo o a la izquierda")
elif media==mediana and mediana==moda:
    print("Este conjunto de datos no posee sesgo, pues su media, su mediana y su moda son iguales.")
else:
    print("Este conjunto de números aleatorios requiere un análisis más detallado")
