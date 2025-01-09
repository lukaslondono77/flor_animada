
''' Codigo de python
este es el codigo de python  patra el proceso de insercio e insercion de nodos'''


# nodo = Nodo(valorNodo)
# nodo.siguiente = nodo
# self.cabeza = nodo
# self.cola = nodo



# if posicion == 0:
#     if self.cabeza == self.cola:
#         self.cabeza.siguiente = None 
#         self.cabeza = None
#         self.cola = None
#     else:
#         self.cabeza = self.cabeza.siguiente = self.cabeza


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaVinculada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cola:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def insertar_en_posicion(self, posicion, valor):
        if posicion == 0:
            self.insertar_al_inicio(valor)
            return
        
        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        contador = 0

        while actual and contador < posicion - 1:
            actual = actual.siguiente
            contador += 1

        if not actual:
            print("La posición es inválida.")
            return

        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

        if nuevo_nodo.siguiente is None:
            self.cola = nuevo_nodo

    def eliminar_por_posicion(self, posicion):
        if not self.cabeza:  # Si la lista está vacía
            print("La lista está vacía.")
            return

        if posicion == 0:  # Eliminar la cabeza
            if self.cabeza == self.cola:  # Si solo hay un nodo
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza
        contador = 0

        while actual.siguiente and contador < posicion - 1:
            actual = actual.siguiente
            contador += 1

        if not actual.siguiente:
            print("La posición es inválida.")
            return

        if actual.siguiente == self.cola:  # Si es el último nodo
            self.cola = actual

        actual.siguiente = actual.siguiente.siguiente

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")


# Ejemplo de uso:
lista = ListaVinculada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(2)
lista.insertar_al_final(4)
lista.insertar_en_posicion(1, 5)
lista.imprimir_lista()  # Salida esperada: 2 -> 5 -> 3 -> 4 -> None

lista.eliminar_por_posicion(1)
lista.imprimir_lista()  # Salida esperada: 2 -> 3 -> 4 -> None
