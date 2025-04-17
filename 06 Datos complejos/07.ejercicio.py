#Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: 
#Agregar clientes (encolar). 
#Atender clientes (desencolar). 
#Mostrar el siguiente cliente en la fila. 

from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        self.elementos.append(elemento) 

    def desencolar(self):
        return self.elementos.popleft() if not self.esta_vacia() else "La cola está vacía"  

    def esta_vacia(self):
        return len(self.elementos) == 0  

    def ver_frente(self):
        return self.elementos[0] if not self.esta_vacia() else "La cola está vacía"


cola = Cola()
cola.encolar("Turno 1")
cola.encolar("Turno 2")
cola.encolar("Turno 3")
print(cola.desencolar()) 