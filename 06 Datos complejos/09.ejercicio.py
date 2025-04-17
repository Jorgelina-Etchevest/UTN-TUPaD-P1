#Dada una lista enlazada, implementa una función para invertirla. 

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente   
            actual.siguiente = anterior    
            anterior = actual              
            actual = siguiente            

        self.cabeza = anterior

lista = ListaEnlazada()
lista.insertar(30)
lista.insertar(20)
lista.insertar(10)

#Lista original
print("La lista original: ")
lista.mostrar()

# lista invertida
print("La lista invertida: ")
lista.invertir()
lista.mostrar()