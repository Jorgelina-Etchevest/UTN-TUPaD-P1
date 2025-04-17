#Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar 
#los valores almacenados. 

class Nodo:
    def __init__(self, dato):
        self.dato = dato  
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
        print("None")


lista = ListaEnlazada()
lista.insertar(30)
lista.insertar(20)
lista.insertar(10)
lista.mostrar() 