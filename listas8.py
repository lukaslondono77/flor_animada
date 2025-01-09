from array import*
import os
import time
#arreglos
'''un arreglo es una coleccion de elementos que se encuentran en la misma ubicacion en memoria'''
#declaracion de la lsta (vacia en este caso)
listaCompras = []

def mostrarListaCompras():
    for articulo in listaCompras:
        print(articulo)
    os.system("pause")
def insertarElemento(articulo):
    posi = 0
    if len(listaCompras) == 0:
        listaCompras.insert(0,articulo)
        return
    else:
        for objeto in listaCompras:
            if objeto < articulo:
                posi = posi+1
            else:
                break
                #lo inserta despues de cualquier valor
                #menor a el valor ingresado
        listaCompras.insert(posi,articulo)
def modificarArticulo(valorBuscar,valorNuevo):
    encontrado = False
    posi = 0
    if len(listaCompras)== 0:
        print("No existen elemntos en la lista")
    else:
        for elemento in listaCompras:
            if elemento == valorBuscar:
                listaCompras[posi] = valorNuevo
                encontrado = True
                break
            posi = posi + 1
        if not encontrado:
            print("el elemento no existe en la lista")
        os.system("pause")

def buscarArticulo(articulo):
    encontrado = False
    if len(listaCompras) == 0:
        print("no existen en la lista")
    else:
        for elemento in listaCompras:
            if elemento == articulo:
                print(f"Valor { articulo} encontrado! ")
                encontrado = True
        if not encontrado:
            print("el elemento  no existe en la lista")   
    os.system("pause")

def borrarArticulo(articulo):
    encontrado = False
    if len(listaCompras) == 0:
        print('no existe elementos en la lista ')
    else:
        for elemento in listaCompras:
            if elemento == articulo:
                listaCompras.remove(elemento)
                encontrado = True
                #para retornar el valor:
                #return array.index(value)
        if not encontrado:
            print("el articulo no existe en la lista")
    os.system("pause")
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
opcion = 0
while not salir:
    os.system("cls")
    print("1. insertar elemento en la lista")
    print("2. Modificar elemento en la lista")
    print("3. Eliminar elemento en la lista")
    print("4. Buscar elemento en la lista")
    print("5. Listar elemento en la lista")
    print("6. Salir")
    opcion = validarOpcion()
    if opcion == 1:
        articulo = input("Digite un articulo para la lista: ")
        insertarElemento(articulo)
    elif opcion == 2:
        artBuscar = input("digite  articulo para modificar: ")
        artCambiar = input("digite nombre de nuevo articulo: ")
        modificarArticulo(artBuscar,artCambiar)
    elif opcion == 3:
        articulo = input("Digite un articulo para eliminar la lista: ")
        borrarArticulo(articulo)
    elif opcion == 4:
        articulo = input("digite articulo a buscar: ")
        buscarArticulo(articulo)
    elif opcion == 5:
        mostrarListaCompras()
    elif opcion == 6:
        salir = True
    else:
        print("introduce una opcion entre 1 y 6")

print("Fin del programa")



   
    
    

    




    





