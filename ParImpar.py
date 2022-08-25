while (True):
    #Ingresa numero
    numero = float(input("Ingresa un numero "))
    #Se divide en dos 
    operacion = numero/2
    #Localiza un punto
    posicion = str(operacion).find(".")
    #Si despues del punto encuentra un 0 es par si no es impar 
    if str(operacion)[posicion + 1] == "0":
        print("El numero " + str(numero) + " Es par!!")
    else:
        print("El numero " + str(numero) + " Es impar!!")
    #Ingresar otro numero
    pregunta = input("Quieres ingresar otro numero? ")
    while pregunta != "si" and pregunta != "no":
        print("solo escribe si o no")
        pregunta = input("Quieres ingresar otro numero? ")
    if pregunta == "no":
        break