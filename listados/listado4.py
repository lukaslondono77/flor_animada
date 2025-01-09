#Calculo Factoriasl de un numero
'''
este programa determina el factorial de un numero cualquiera.
podemos definir un factorial como: cantida que que resulta de la multiplicacion de un determinado numero natural
por todos los numeros naturales que le antecdeden excluyendo el 0;
se representa como n!'''

def factorial(numero):
    if  numero in [0,1]:
        return 1
    else:
        return numero * factorial(numero - 1)
#convierte el input en un valor numerico entero(numero)
numero = int(input("ingrese un numero: "))
#imprime el factorial. La F nos sirve para presentar
#en pantalla la variable o el resultado de un calculo
#que se encuentra dentro de una etiqueta o cadena
# y encerrado entre parentesis tal es el caso de {factorial(numero)}
print(f"el factorial de {numero} es {factorial(numero)}")

#ejerciocio2
'''
calculo de la sucesion de fibonacci
este programa determina la sucesion de fibonacci,
la cual consta de una seria de numeros naturales que se suman de a 2 a partir de 0 y 1.
se llevaa cabo siempre sumando los ultimos 2 numeros.
los dos numeros que le anteceden al actual son el resultado de sumarlos.
por ejemplo si el numero actual es el 8,podria que los antecesores sean 5 y 3. asi
5+3 seria 8. por ejemplo:0,1,1,2,3,5,8,13,21,34...costituye una sucesion de fibonacci
la formula recursiva fibonacci seria la siguiente:
f(n) = f(n-1) + f(n-2)'''
def fibonacci(numero):
    if numero < 0 or int(numero) != numero:
        return 
    if numero in [0,1]:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

#convierte el input en un valor numerico entero(numero)
numero = int(input("ingrese un numero: "))
print(f"El valor de {numero} es {fibonacci(numero)}")



#ejercicio 3
'''
calculo del maximo comun divisor.
este programa determina el maximo comun divisor (MCD) de dos numeros
el MCD es el factor de division que comparten todos los numeros. Por ejemplo,12,20 y 24
tienen dos factores comunes 2 y 4. 
el mayor es 4, por lo tanto el MCD es 4.
mediante el algoritmo de euclides se puede encontrar dividiendo el numero mayor por el numero menor.
si la division no es exacta entonces podemos tomar el residuo y dividirlo tantas veces sea necesario
hasta llegar a una division sin residuo.
el MCD seria entonces el ultimo numero por el cual se puede diviir sin obtener un residuo'''

def MCD(numero1,numero2):
    if int(numero1) != numero1 and int(numero2) != numero2:
        return 0
    if numero2 == 0:
        return numero1
    else:
        return MCD(numero2,numero1 % numero2)
_numero1 = int(input("ingrese un numero: "))
_numero2 = int(input("ingrese un numero: "))
resultado = MCD(_numero1,_numero2)
if resultado==0:
    print("el MCD es 0")    
else:
    print(f"El MCD de {_numero1} y {_numero2} es {resultado}")
    print(f"es: {MCD(_numero1,_numero2)}")


