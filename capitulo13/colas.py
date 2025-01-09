#Colas en Python
#Cola: FIFO
#Pila: LIFO
# de pilas estan las operaciones Vacia (empty())
#Tamaño (size())
#Tope (top())/peek()
#Insertar (push())
import os
from collections import deque

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to pause the program
def pause():
    input("Presione Enter para continuar...")

class Cola:
    def __init__(self):
        self.cola = deque()

    def estaVacia(self):
        # Corrected to check if the deque is empty
        return len(self.cola) == 0

    def agregarAtras(self, dato):
        print(f"Agregando {dato} a la cola")
        self.cola.append(dato)
        print()
        pause()

    def agregarFrente(self, dato):
        print(f"Agregando {dato} al frente o 'front' ")
        # Using appendleft to add to the front of the deque
        self.cola.appendleft(dato)
        print()
        pause()

    def descolar(self):
        # Using popleft to remove from the front of the deque
        return self.cola.popleft()

def validarOpcion():
    
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Ingrese una opcion del menu: "))
            correcto = True
        except ValueError:
            print("Error, Ingrese un valor valido")
    return num

# Main program logic starts here, outside the class definition
salir = False
cola = Cola()

while not salir:
    clear_screen()
    print("\n***** Operaciones sobre una cola *****")
    print("1. Insertar un paciente en la cola")
    print("2. Descolar un paciente de la cola")
    print("3. Mostrar los pacientes de la cola")
    print("4. Salir")
    opcion = validarOpcion()

    if opcion == 1:
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        dato = f"{nombre} ({edad} años)"
        if edad >= 55:
            # Adding patients aged 55 or older to the front
            cola.agregarFrente(dato)
        else:
            # Adding younger patients to the back
            cola.agregarAtras(dato)
    elif opcion == 2:
        if cola.estaVacia():
            print("La cola está vacía")
            pause()
        else:
            print(f"El paciente {cola.descolar()} fue atendido")
            print()
            pause()
    elif opcion == 3:
        # Displaying the list of patients in the queue
        print("Pacientes en la cola:")
        for paciente in list(cola.cola):
            print(paciente)
        print()
        pause()
    elif opcion == 4:
        salir = True
    else:
        print("Introduce un valor entre 1 y 4")
        pause()

print("Fin del programa")


