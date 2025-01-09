#Colas y pilas en python
#Cola: FIFO
#Pila: LIFO
# de pilas estan las operaciones Vacia (empty())
#Tamaño (size())
#Tope (top())/peek()
#Insertar (push())
import os

class Nodo:
    def __init__(self, dato):    
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, dato):
        print(f"Agregando {dato} en el tope de la pila")
        if self.cima is None:
            self.cima = Nodo(dato)
            return
        nuevoNodo = Nodo(dato)
        nuevoNodo.siguiente = self.cima
        self.cima = nuevoNodo
    
    def desapilar(self):
        if self.cima is None:
            print("No existen elementos en la pila para desapilar")
            return
        print(f"Desapilando {self.cima.dato}")
        self.cima = self.cima.siguiente

    def mostrar(self):
        print("\nLista de los datos que están en la pila:")
        nodoActual = self.cima
        cadena = ""
        vez = 0
        while nodoActual is not None:
            if vez == 0:
                cadena += nodoActual.dato + " <-- cima de la pila\n"
                vez = 1
            else:
                cadena += nodoActual.dato + "\n"
            nodoActual = nodoActual.siguiente
        print(cadena)

def validarOpcion():
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Ingrese una opción del menú: "))
            correcto = True
        except ValueError:
            print("Ingrese un valor válido")
    return num

# Bloque principal del programa
if __name__ == "__main__":
    pila = Pila()
    salir = False
    while not salir:
        print("\n***** Operaciones sobre una pila *****")
        print("1. Insertar un elemento en la pila")
        print("2. Desapilar un elemento de la pila")
        print("3. Mostrar los elementos de la pila")
        print("4. Salir")
        opcion = validarOpcion()
        
        if opcion == 1:
            valor = input("Ingrese el valor a insertar en la pila: ")
            pila.apilar(valor)
        elif opcion == 2:
            pila.desapilar()
        elif opcion == 3:
            pila.mostrar()
        elif opcion == 4:
            salir = True
        else:
            print("Introduce un valor entre 1 y 4")
    
    print("Fin del programa")
