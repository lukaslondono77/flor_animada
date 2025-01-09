'''escriba el codigo que permita eliminar todo el arbol binario balanceado del listado
'''
def eliminarArbol(self, raiz):
    raiz.valor = None 
    raiz.izquierda = None
    raiz.derecha = None
    return("el arbol ha sido eliminado")

'''proceda  a  implementar  la  funcionalidad para obtener la ruta mas corta entre  un nodo origen y destino, considerando el arbol binario balanceado del listado  
'''

def busqueCMCcColombia():
    nodos = ["monteria", "barranquilla", "tunja", "cartagena", "bucaramanga", "ibague", "barrancabermeja"]
    init_grafo ={}
    for nodo in nodos:
        init_grafo[nodo] = []
    init_grafo["monteria"]["barranquilla"] = 616
    init_grafo["monteria"]["tunja"] = 500
    init_grafo["barranquilla"]["tunja"] = 300
    init_grafo["barranquilla"]["cartagena"] = 700
    init_grafo["tunja"]["cartagena"] = 300
    init_grafo["tunja"]["bucaramanga"] = 400
    init_grafo["cartagena"]["bucaramanga"] = 300
    init_grafo["bucaramanga"]["ibague"] = 300
    init_grafo["bucaramanga"]["barrancabermeja"] = 400
    init_grafo["ibague"]["barrancabermeja"] = 100
    return init_grafo
    