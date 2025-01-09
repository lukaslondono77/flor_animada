import os
import json

class Grafo:
    def __init__(self, artistas):
        self.artistas = artistas
        # Create the dictionary grafo_dicc
        self.grafo_dicc = {}
        for inicio, final in self.artistas:
            if inicio in self.grafo_dicc:
                self.grafo_dicc[inicio].append(final)
            else:
                self.grafo_dicc[inicio] = [final]
        print(json.dumps(self.grafo_dicc, sort_keys=False, indent=4))

    def getRuta(self, inicio, final, ruta=[]):
        ruta = ruta + [inicio]
        if inicio == final:
            return [ruta]
        if inicio not in self.grafo_dicc:
            return []
        caminos = []
        for nodo in self.grafo_dicc[inicio]:
            if nodo not in ruta:
                nueva_ruta = self.getRuta(nodo, final, ruta)
                for c in nueva_ruta:
                    caminos.append(c)
        return caminos

    def getRutaCorta(self, inicio, final, ruta=[]):
        ruta = ruta + [inicio]
        if inicio == final:
            return ruta
        if inicio not in self.grafo_dicc:
            return None
        ruta_corta = None
        for nodo in self.grafo_dicc[inicio]:
            if nodo not in ruta:
                r_corta = self.getRutaCorta(nodo, final, ruta)
                if r_corta:
                    if ruta_corta is None or len(r_corta) < len(ruta_corta):
                        ruta_corta = r_corta
        return ruta_corta
    
    def mostrarResultado(self):
        print(self.grafo_dicc)


def consultar():
    rutas = [
        ("La Cruz", "Upala"),
        ("La Cruz", "Liberia"),
        ("Liberia", "Santa Cruz"),
        ("Liberia", "Puntarenas"),
        ("Upala", "San Carlos"),
        ("Upala", "Alajuela"),
        ("San Carlos", "San Jose"),
        ("Puntarenas", "San Carlos"),
        ("Santa Cruz", "Nicoya"),
        ("Nicoya", "Hojancha"),
        ("Alajuela", "San Jose"),
    ]
    os.system("cls" if os.name == "nt" else "clear")  # Cross-platform screen clearing
    _rutas = Grafo(rutas)
    inicio = input("Digite el inicio de la ruta: ")
    destino = input("Digite el destino de la ruta: ")
    print()
    print(f"Las rutas posibles entre {inicio} y {destino} son:\n{_rutas.getRuta(inicio, destino)}")
    print()
    print(f"La ruta más corta entre {inicio} y {destino} es:\n{_rutas.getRutaCorta(inicio, destino)}")
    print()
    os.system("pause" if os.name == "nt" else "read -p 'Presione Enter para continuar...'")

def validarOpcion():
        
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("seleccione una opcion del menu: "))
            correcto = True
        except ValueError:
            print("Error, introduce un valor valido: ")
    return num
salir = False
while (not salir):
    os.system("cls")
    print("***Operaciones sobre un grafo y menos Paradas***")
    print("1. Buscar Rutas y ruta mas corta")
    print("2. Salir")
    opcion = validarOpcion()
    if opcion == 1:
        consultar()
    elif opcion == 2:
        salir = True
    else:
        print("introduce una opcion entre 1 y 2")
print("Fin del programa")
