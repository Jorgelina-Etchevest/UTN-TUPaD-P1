# Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else "La pila está vacía" 

    def esta_vacia(self):
        return len(self.elementos) == 0 

    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else "La pila está vacía"
    
def parentesis_balanceados(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in "({[":
            pila.apilar(caracter)
        elif caracter in ")}]":
            if pila.esta_vacia():
                return False  # hay un cierre sin apertura
            tope = pila.desapilar()
            if pares[caracter] != tope:
                return False  # el tipo de paréntesis no coincide
    return pila.esta_vacia()


print(parentesis_balanceados("(){}[]"))  
print(parentesis_balanceados("{[()]}"))        
print(parentesis_balanceados("({[})"))         
print(parentesis_balanceados("((()))"))        
print(parentesis_balanceados("((())")) 

