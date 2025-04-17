#Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente. 

import math
class Circulo:
    def __init__(self, radio):      #atributos
        self.radio = radio

    def calcular_area(self):               #método
      return round(math.pi * (self.radio**2),2)
    
    def calcular_perimetro(self):
       return round((2 * math.pi * self.radio), 2)

radio = Circulo(8)
print(radio.calcular_area()) 
print(radio.calcular_perimetro())