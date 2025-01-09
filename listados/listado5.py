#arreglos
'''un arreglo es una coleccion de elementos que se encuentran en la misma ubicacion en memoria'''
from array import*
import os
import time
#para decalrar arreglos de tipo 'i' entero, 'f' float,'d' double
#si deaseamos un arreglo de tipo float seria:arreglo2 = array('f',[])
arreglo = array('i',[])#declara un vector de tipo entero('i')

def mostrarArreglo():
    print(f"Los valores contenidos son: ")
    for elemento in arreglo:
        #le asignamos a print el end="" para que no se agregue un salto de linea y se muestre en la misma linea
        print(elemento,end=" ")
        #al finalizar de imprimir la linea que agregue el salto 
        print()
        #para realizar una pausa en la visualizacion de datos
        os.system("pause")

def insertarElemento(valor):
    posi = 0
    if len(arreglo)==0:
        arreglo.insert(0,valor)
        return
    else:
        for elemento in arreglo:
            if elemento < valor:
                posi = posi+1
            #lo inserta despues de cualquier valor
             #menor a el valor ingresado
            arreglo.insert(posi,valor)

def buscarElemento(valor):
    encontrado = False
    if len(arreglo)== 0:
        print('no existen  los elementos en el arreglo')
    else:
        for elemento in arreglo:
            if elemento == valor:
                print(f"Valor {valor}encontrado!" )
                encontrado = True
                #para retornar el valor
                #return arreglo.index(value)
            if not encontrado:
                print("no existe el elemnto en el arreglo")
    os.system("pause")

def borrarElemento(valor):
    encontrado = False
    if len(arreglo) == 0:
        print("No existen elemnetos en el arreglo")
    else:
        for elemento in arreglo:
            if elemento == valor:
                arreglo.remove(elemento)
                encontrado = True
                #para retornar el valor
                #return arreglo.index(value)
        if not encontrado:
            print("no existe el elemnto en el arreglo")
    os.system("pause")

def modificarElemento(valorBuscar,valorNuevo):
    encontrado = False
    posi = 0
    if len(arreglo) == 0:
        print("No existen elementos en el arreglo")
    else:
        for elemento in arreglo:
            if elemento == valorBuscar:
                arreglo[posi] = valorNuevo
                encontrado = True
                break
            posi = posi + 1
        if not encontrado:
            print("el elemento no existe en el arreglo")
            os.system("pause")

def validarOpcion():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("ingrese una opcion: "))
            correcto = True
        except ValueError:
            print("ingrese un numero entero")    

    return num
salir = False
opcion = 0
while (not salir):
    os.system("cls")
    print("1. insertar  un elemento en el arreglo")
    print("2. Modificar un elemto del arreglo")
    print("3. Eliminar un elemnto del arreglo")
    print("4. Buscar un elemnto del arreglo")
    print("5. Listar un elemnto del arreglo")
    print("6. Salir")
    opcion = validarOpcion()
    if opcion == 1:
        numero = int(input("ingrese un entero a incluir"))
        insertarElemento(numero)
    elif opcion == 2:
        numero1 = int(input("digite valor a modificar"))
        numero2 = int(input("digite el nuevo valor"))
        modificarElemento(numero1,numero2)
    elif opcion == 3:
        numero = int(input("digite un valor a buscar y eliminar"))
        borrarElemento(numero)
    elif opcion == 4:
        numero = int(input("digite un valor a buscar"))
        buscarElemento(numero)
    elif opcion == 5:
        mostrarArreglo()
    elif opcion == 6:
        salir = True
    else:
        print("introduce un valor entre 1 y 6")
print("fin del programa")
                #para retornar el valor
                #return arreg


   