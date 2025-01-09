import os


'''Escriba un programa en python que m,ediante recursividad convierta un numero en decimal a binario'''
def decimalABinario(numero):    
    if numero < 0 or int(numero) != numero:
        return
    elif numero == 0:
        return 0
    else:
        return numero%2 + 10 * decimalABinario(int(numero/2))
numero = int(input("ingrese un numero: "))
print(f"El numero {numero} en binario es:{decimalABinario(numero)}")




'''
escriba el metodo que permita a una lista doblemente enlazada  buscar un determinado nodo,
Agrege esta funcionalidad al codigo del listado 14.11 debe implementrase su ejecucion en el menu '''

def buscarNodo(self, valorNodo):
    if self.cabeza is None:
        print("La lista está vacía")
    else:
        nodoTemp = self.cabeza
        while nodoTemp:
            if nodoTemp.dato == valorNodo:
                print(f"El valor {valorNodo} fue encontrado en la lista")
                return
            nodoTemp = nodoTemp.siguiente
        print(f"El valor {valorNodo} no fue encontrado en la lista")

'''
Eccriba el motodo  que permita a una lista doblemente enlazada eliminar un determinado nodo,
Agrege esta funcionalidad al codigo del listado 14.11 debe implementarse su ejecucion en
 el menu'''
def eliminarNodo(self, posicion):
    if self.cabeza is None:
        print("La lista doblemente enlazada esta vacia")
    else:
        if posicion == 0:
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cola.anterior = None
        elif posicion == 1:
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
        else:
            nodoActual = self.cabeza
            indice = 0
            while indice < posicion - 1:
                nodoActual = nodoActual.siguente
                indice += 1
            nodoActual.siguiente = nodoActual.siguiente.siguiente   
            nodoActual.siguiente.anterior = nodoActual
        print("el nodo fue  exitosamente eliminado")
        os.system("pause")



        '''
        escriba el metodo que permita a una lista circular doblemente enlazada eliminar
        un determinado nodo, pasandole como parametro su valor y no su posicion.
        agrege esta funcionalidad al cidigo del listado
        Debe implementarse el ejecucion en el menu'''
        #elimina un nodo desde una lista circulra simplememnte enlazada
        def eliminarNodo(self, dato):
            nodoActual = self.cabeza
            nodoEliminado = False
            if nodoActual is None:
                nodoEliminado = False
            
            elif nodoActual.dato == dato:
                self.cabeza = nodoActual.siguiente
                self.cabeza.anterior = None
                nodoEliminado = True
            
            elif self.cola.dato == dato:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
                nodoEliminado = True

            else:
                while nodoActual:
                    if nodoActual.dato == dato:
                        nodoActual.anterior.siguiente = nodoActual.siguiente
                        nodoActual.siguiente.anterior = nodoActual.anterior
                        nodoEliminado = True
                        break
                    nodoActual = nodoActual.siguiente