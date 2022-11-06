import os


def clear():
    # Limpiar la pantalla segun el sistema
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def ParOImpar():
    while True:
        clear()
        # Pregunta el numero a calcular
        while True:
            number = input("Ingresa un numero: ")
            try:
                number = float(number)
                break
            except:
                print("\nNo es un numero\n")

        # Calcular el modulo del numero y si es 0 significa que es un numero par
        if number % 2 == 0:
            print("\nEl numero {} es par!! \n".format(number))
        else:
            print("\nEl numero {} es impar!! \n".format(number))
        # Preguntar si quieres continuar en el programa
        question = input("Quieres salir del programa? S/N ")
        # Si es S se corta el proceso
        if question == "S" or question == "s":
            break


def OldFunction():
    while (True):
        # Ingresa numero
        numero = float(input("Ingresa un numero "))
        # Se divide en dos
        operacion = numero/2
        # Localiza un punto
        posicion = str(operacion).find(".")
        # Si despues del punto encuentra un 0 es par si no es impar
        if str(operacion)[posicion + 1] == "0":
            print("El numero " + str(numero) + " Es par!!")
        else:
            print("El numero " + str(numero) + " Es impar!!")
        # Ingresar otro numero
        pregunta = input("Quieres ingresar otro numero?")
        while pregunta != "si" and pregunta != "no":
            print("solo escribe si o no")
            pregunta = input("Quieres ingresar otro numero? ")
        if pregunta == "no":
            break


if __name__ == "__main__":
    ParOImpar()
