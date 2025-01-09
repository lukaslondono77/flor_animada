import os

# Clase que define un nodo del árbol
class nodoArbol:
    def __init__(self, dato, hijos=None):
        self.dato = dato
        self.hijos = hijos if hijos is not None else []

    # Método para mostrar el árbol de manera estructurada
    def __str__(self, nivel=0):
        cad = "  " * nivel + str(self.dato) + "\n"  # Se agrega indentación para los niveles
        for hijo in self.hijos:
            cad += hijo.__str__(nivel + 1)  # Llamada recursiva con aumento de nivel
        return cad

    # Inserta un nodo como hijo
    def insertarHijo(self, nodoArbol):
        self.hijos.append(nodoArbol)

# Crear el nodo raíz `raizBebidas`
raizBebidas = nodoArbol("Bebidas")
# Crear nodos independientes `bCaliente` y `bFria`
bCaliente = nodoArbol('Caliente')
bFria = nodoArbol('Fria')
# Agregar los nodos como hijos de `raizBebidas`
raizBebidas.insertarHijo(bCaliente)
raizBebidas.insertarHijo(bFria)

# Crear nodos `cafe`, `te` y `jugo`
cafe = nodoArbol('Cafe')
te = nodoArbol('Te')
jugo = nodoArbol('Jugo')
# Agregar nodos hijos a `bCaliente` y `bFria`
bCaliente.insertarHijo(cafe)
bCaliente.insertarHijo(te)
bFria.insertarHijo(jugo)

# Crear nodo raíz `raizComidas`
raizComidas = nodoArbol("Comidas")
# Crear nodos `cTrad` y `cFran`
cTrad = nodoArbol('Tradicionales')
cFran = nodoArbol('Francesa')
# Agregar nodos hijos a `raizComidas`
raizComidas.insertarHijo(cTrad)
raizComidas.insertarHijo(cFran)

# Crear nodos `papasFritas` y `galloPinto`
papasFritas = nodoArbol('Papas Fritas')
galloPinto = nodoArbol('Gallo Pinto')
# Agregar nodos hijos a `cFran` y `cTrad`
cFran.insertarHijo(papasFritas)
cTrad.insertarHijo(galloPinto)

# Limpiar pantalla (en Windows usa 'cls', en Mac/Linux usa 'clear')
os.system("clear")

# Mostrar los datos desde las raíces
print("***** Comidas ofrecidas *****")
print(raizComidas)
print("***** Bebidas ofrecidas *****")
print(raizBebidas)
