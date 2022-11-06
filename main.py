from tabulate import tabulate
from scripts.ParImpar import ParOImpar
from scripts.BlackJack import BlackJack
import os
# import BlackJack

# Lista de programas disponibles
programsList = [[0, "BlackJack"],
                [1, "Par o Impar"]]


def clear():
    # Limpiar la pantalla segun el sistema
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def validationSelect(input):
    # Validar que este en las opciones la elejida
    # Recorre la lista de programas
    for i in programsList:
        if input == i[0]:
            return True
    return False


def runPrograms(option):
    # Ejecuta el programa segun la opcion seleccionada
    clear()
    if option == 0:
        BlackJack()
    elif option == 1:
        ParOImpar()


def printTablePrograms():
    # Mostrar en forma de tabla todos los programas disponibles
    print(tabulate(programsList,
                   headers=["INDEX", "PROGRAM"],
                   tablefmt='fancy_grid',
                   stralign='center',
                   floatfmt='.0f'), end='\n')

    print("\n Preciona cualquier otra tecla para salir \n")


if __name__ == "__main__":

    while True:

        # Muestra la tabla
        printTablePrograms()

        # Seleccionar el programa que se ejecutara
        while True:
            selectProgram = int(input("Que programa probaras? "))
            if validationSelect(selectProgram):
                break
            else:
                exit()

        # Ejecuta el programa
        runPrograms(selectProgram)
