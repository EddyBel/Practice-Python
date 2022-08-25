import random
import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
#Variables datos
puntajes = [1,2,3,4,5,6,7,8,9,10,11]

def inicio():
    #imprime el titulo
    print("************************************************************************************")
    print("********************************** Black  Jack *************************************")
    print("************************************************************************************")

def repartirBarajaUsuario():
    #Reparte los puntajes jugador 
    barajaUsuario = []
    numero = 0
    while (numero < 2):
        puntajeRandom = random.choice(puntajes)
        barajaUsuario.append(puntajeRandom)
        numero = numero + 1   
    #Imprime los puntajes
    print()
    print ("Tus cartas son")
    print (*barajaUsuario)
    suma = sum(barajaUsuario)
    print ("La suma de tus cartas es " + str(suma) + "/21")
    print()
    #Agregar una carta al jugador
    pregunta = input("Quieres optener una carta mas? ")
    while(pregunta != "si" and pregunta != "no"):
        print("Solo puedes decir si o no")
        print()
        pregunta = input("Quieres optener una carta mas? ")
    while (pregunta == "si"):
        puntajeRandom = random.choice(puntajes)
        barajaUsuario.append(puntajeRandom)
        print()
        print("Tus cartas son ")
        print(*barajaUsuario)
        suma = sum(barajaUsuario)
        print("La suma de tus cartas es " + str(suma) + "/21")
        print()
        pregunta = input("Quieres optener una carta mas? ")
        while(pregunta != "si" and pregunta != "no"):
            print("Solo puedes decir si o no")
            print()
            pregunta = input("Quieres optener una carta mas? ")
        print()
    print()
    return suma

def repartirBarajaDiler ():
    #Repartir puntaje a Diler
    barajaDiler = []
    numero = 0
    while (numero > 2):
        puntajeRandom = random.choice(puntajes)
        barajaDiler.append(puntajeRandom)
        numero = numero + 1
    suma = sum(barajaDiler)
    #Si el puntaje es menor a 17 tomara otro punto
    while (suma < 14):
        puntajeRandom = random.choice(puntajes)
        barajaDiler.append(puntajeRandom)
        suma = sum(barajaDiler)
    #Imprime las cartas de diler
    print()
    print ("Cartas del diler ")
    print(*barajaDiler)
    print()
    print("Suma de puntaje es " + str(suma))
    return suma

#Inicia el juego
while (True):
    #Puntos totales
    partida = 0
    puntosUsuario = 0
    puntosDiler = 0
    inicio()
    print()
    #Se limitan el numero de partidas
    while (partida <= 10):
        #Se reparten los puntos
        Usuario = repartirBarajaUsuario()
        time.sleep(1)
        Diler = repartirBarajaDiler()
        time.sleep(1)
        #Se selleciona ganadores de la partida
        if (Usuario > Diler and Usuario <= 21):
            print()
            print ("Gana Jugador")
            print()
            puntosUsuario = puntosUsuario + 1
        elif (Diler > Usuario and Diler <= 21):
            print()
            print ("Gana Diler")
            print()
            puntosDiler = puntosDiler + 1
        elif (Diler == Usuario):
            print()
            print("Empate")
            print()
            puntosDiler = puntosDiler + 1
            puntosUsuario = puntosUsuario + 1
        elif (Diler >21 and Usuario>21):
            print()
            print ("Puntajes pasados")
            print()
        elif (Usuario > 21 and Usuario > Diler):
            print()
            print("Gana Diler")
            print()
            puntosDiler = puntosDiler + 1
        elif (Diler > 21 and Diler > Usuario):
            print()
            print("Gana Jugador")
            print()
            puntosUsuario = puntosUsuario + 1
        partida = partida + 1
    #Imprime el ganador de puntajes Totales
    if (puntosUsuario > puntosDiler):
        print()
        print()
        print("***********************************")
        print("El juego fue ganado por Jugador!!!")
        print("Partidas ganas Eduardo es " + str(puntosUsuario) + " Partidas ganadas Diler " + str(puntosDiler))
        print("***********************************")
    elif(puntosDiler > puntosUsuario):
        print()
        print()
        print("***********************************")
        print("El juego fue ganado por Diler")
        print("Partidas ganas Eduardo es " + str(puntosUsuario) + " Partidas ganadas Diler " + str(puntosDiler))
        print("***********************************")
    print()
    #Reiniciar juego
    resetear = input("Quieres jugar de nuevo? ")
    while (resetear != "si" and resetear != "no"):
        print("Solo puedes escribir si o no: ")
        resetear = input("Quieres jugar de nuevo?")
    if (resetear == "no"):
        break
    clearConsole()

