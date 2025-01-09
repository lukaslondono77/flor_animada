import os

# clase nodo que permitirá almacenar el dato y los punteros de los nodos anteriores y siguientes
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

# constructor de la clase ListaCircularEnlazadaSimple inicializando
# el frente y la copia de la lista en nulo (None en Python) mediante el constructor __init__
class ListaCircularEnlazadaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # define un método que permitirá iterar a través de la lista hasta alcanzar que el nodo siguiente apunte
    # a la cabeza de la lista. Para visualizar los datos basta con la siguiente instrucción:
    # : print([nodo.dato for nodo in ListaCircularEnlazadaSimple])
    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente
            if nodo == self.cola.siguiente:
                break

    # creación de la lista circular simplemente enlazada por primera vez
    # (inicializada) solamente con el valor del inicio y cabeza
    # (frente) y la cola (fila) que apunten al nodo recién ingresado
    def crearLista(self, valorNodo):
        nodo = Nodo(valorNodo)
        nodo.siguiente = nodo
        self.cabeza = nodo
        self.cola = nodo
        print("La lista ha sido creada")
        os.system("pause")

    # una vez creada la lista se pueden insertar datos, los datos del nodo
    # considerando su orden de entrada a la lista
    def insertarNodo(self, dato, posicion):
        if self.cabeza is None:
            return "La lista está vacía"
        else:
            nuevoNodo = Nodo(dato)
            if posicion == 0:
                nuevoNodo.siguiente = self.cabeza
                self.cabeza = nuevoNodo
                self.cola.siguiente = self.cabeza
            elif posicion == 1:
                nuevoNodo.siguiente = self.cola.siguiente
                self.cola.siguiente = nuevoNodo
                self.cola = nuevoNodo
            else:
                nodoTemp = self.cabeza
                indice = 0
                while indice < posicion - 1:
                    nodoTemp = nodoTemp.siguiente
                    indice += 1
                nodoProximo = nodoTemp.siguiente
                nodoTemp.siguiente = nuevoNodo
                nuevoNodo.siguiente = nodoProximo
                if nodoTemp == self.cola:
                    self.cola = nuevoNodo
            return "El dato fue exitosamente insertado!!!"

    # recorrido de nodos en lista circular enlazada simple
    def recorrido(self):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            nodoActual = self.cabeza
            listado = ""
            print("Contenido de la lista circular simplemente enlazada:")
            while True:
                listado += str(nodoActual.dato) + " -> "
                nodoActual = nodoActual.siguiente
                # si el nodo actual redirecciona el puntero que apunta
                # a la lista, que en este caso sería al frente de la lista
                # terminando de recorrer todos los nodos
                if nodoActual == self.cabeza:
                    print(listado)
                    break
        os.system("pause")

    # se elimina un nodo desde una lista circular simplemente enlazada
    def eliminarNodo(self, posicion):
        if self.cabeza is None:
            print("La lista circular simplemente enlazada está vacía")
        else:
            if posicion == 0:
                if self.cabeza == self.cola:
                    self.cabeza.siguiente = None
                    self.cabeza = None
                    self.cola = None
                else:
                    self.cabeza = self.cabeza.siguiente
                    self.cola.siguiente = self.cabeza
            elif posicion == 1:
                if self.cabeza == self.cola:
                    self.cabeza.siguiente = None
                    self.cabeza = None
                    self.cola = None
                else:
                    nodo = self.cabeza
                    while nodo is not None:
                        if nodo.siguiente == self.cola:
                            break
                        nodo = nodo.siguiente
                    nodo.siguiente = self.cabeza
                    self.cola = nodo
            else:
                nodoTemp = self.cabeza
                index = 0
                while index < posicion - 1:
                    nodoTemp = nodoTemp.siguiente
                    index += 1
                nodoProximo = nodoTemp.siguiente
                nodoTemp.siguiente = nodoProximo.siguiente

    # búsqueda de un nodo en una lista circular enlazada simple
    def buscarNodo(self, valorNodo):
        if self.cabeza is None:
            print("No hay ningún elemento en la lista")
        else:
            nodoTemp = self.cabeza
            while True:
                if nodoTemp.dato == valorNodo:
                    return "Encontrado Valor: " + str(nodoTemp.dato)
                nodoTemp = nodoTemp.siguiente
                if nodoTemp == self.cabeza:
                    break
            return "El valor " + str(valorNodo) + " no existe en la lista"

    # eliminar toda la lista circular enlazada simple
    def eliminarLista(self):
        self.cabeza = None
        if self.cola:
            self.cola.siguiente = None
        self.cola = None

# función para validar la opción seleccionada por el usuario
def validarOpcion():
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Seleccione una opción del menú: "))
            correcto = True
        except ValueError:
            print("Error, introduce un valor válido.")
    return num

# flujo principal del programa
salir = False
vez = 0
lista = ListaCircularEnlazadaSimple()
opcion = 0

while not salir:
    os.system("cls")  # En Mac/Linux, reemplazar "cls" con "clear"
    print("1. Insertar elemento en la lista")
    print("2. Eliminar elemento en la lista")
    print("3. Buscar elemento en la lista")
    print("4. Mostrar elementos en la lista")
    print("5. Eliminar toda la lista")
    print("6. Salir")
    
    opcion = validarOpcion()
    
    if opcion == 1:
        pais = input("Digite un país para la lista: ")
        if vez == 0:
            lista.crearLista(pais)
            vez = 1
        else:
            print("¿Dónde desea insertar el nodo?")
            posi = int(input("0 = inicio, 1 = al final, 2 = después del nodo: "))
            lista.insertarNodo(pais, posi)
    
    elif opcion == 2:
        print("Seleccione la posición del nodo para eliminar:")
        posicion = int(input("0 = inicio, 1 = final, 2 = otra posición: "))
        lista.eliminarNodo(posicion)
    
    elif opcion == 3:
        numero = input("Digite el país a buscar: ")
        print(lista.buscarNodo(numero))
        print()
        os.system("pause")  # En Mac/Linux, reemplazar con "read -p 'Presiona Enter para continuar...'"
    
    elif opcion == 4:
        lista.recorrido()
    
    elif opcion == 5:
        lista.eliminarLista()
        print("Lista eliminada.")
    
    elif opcion == 6:
        salir = True
    
    else:
        print("Introduce una opción entre 1 y 6")

print("Fin del programa")
