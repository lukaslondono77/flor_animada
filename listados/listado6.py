#programa que implemeta operaciones sobre matrices usando la libreria numpy
from array import*
#ventas de ACME LTDA
#semana 1- 120000, 13000, 210000, 205678,245000
#semana 2- 98000, 110000, 167000, 198600, 199000
#semana 3- 110000, 90000, 90000, 70000, 60000
#semana 4- 90000, 90000, 90000, 90000, 90000
#semana 5- 13000, 93000, 199000, 13000, 13000
import numpy as nm
arregloVentas = nm.array([[120000, 13000, 210000, 205678,245000],
                          [98000, 110000, 167000, 198600, 199000],
                          [110000, 90000, 90000, 70000, 60000],
                          [90000, 90000, 90000, 90000, 90000],
                          [13000, 93000, 199000, 13000, 13000]])

def buscarElemento(array, fila, columna):
    if fila>= len(array) or columna >= len(array[0]):
        print("Indice de la fila y columna son incorrectos")
    else:
        print(f"Dato en la fila:{fila} columna: {columna} {array[fila][columna]}")
print("Datos del arreglo de ventas")
print(arregloVentas)
#insercion de datos en una matriz hay dos opciones: la primera es 
#mediante la adicion de columna y la sengunda es mediante la adicion de filas
#en este caso insertamos en la fila 1, a partir de la columna 0
nuevoArreglo = nm.insert(arregloVentas, 1, [13000, 93000, 199000, 13000, 13000], axis=0)
print("datos del arreglo copiado con insert")
print(nuevoArreglo)
#se agrega con append una nueva fila
nuevoArreglo = nm.append(arregloVentas, [[13000, 93000, 199000, 13000, 13000]], axis=0)
print("datos del arreglo copiado con append")
print(nuevoArreglo)
buscarElemento(nuevoArreglo,2,2)
#sumar los dos arreglos
arreglo1 = nm.array([[5,6,9,12,14],
                    [15,5,6,19,20],
                    [13,12,30,10,47]])
arreglo2 = nm.array([[17,12,6,5,12],
                     [4,12,2,22,33],
                     [13,7,1,11,18]])
sumaArreglo = nm.add(arreglo1, arreglo2)
print("Suma de arreglos")
print(sumaArreglo)
restaArreglo = nm.subtract(arreglo1, arreglo2)
print("Resta de arreglos")
print(restaArreglo)
multiplicacionArreglo = nm.multiply(arreglo1, arreglo2)
print("Multiplicacion de arreglos")
print(multiplicacionArreglo)
multiArreglo = nm.dot(arreglo1, 2)
print("Multiplicacion de elementos de un arreglo por X 2")
print(multiArreglo)
divisionArreglo = nm.divide(arreglo1, arreglo2)
print("Division de arreglos")
print(divisionArreglo)
modArreglo = nm.mod(arreglo1, 2)
print("Division y residuo de un arreglo")
print(modArreglo)
#camniar los signos de un arreglo
signoArreglo = nm.negative(arreglo2)
print("Cambio de signo de un arreglo2")
print(signoArreglo)
#para obtene la raiz cuadrada de un elemento
raizVector = nm.rint(nm.sqrt(arreglo1))
print("Raiz cuadrada redondeada de cada elemento del arreglo1")
print(arreglo1)
print(raizVector)