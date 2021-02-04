import Metodo_de_Biseccion
import Metodo_de_la_Falsa_Posicion
import Metodo_de_Newton_Raphson
import Metodo_de_la_Secante

opcion = 1

while opcion != 0:
    #Pide al usuario la funcion
    expr = input("\nIntroduce la funcion en terminos de x: ")

    print("\nMetdos Numericos\n")
    print("1.- Metodo de biseccion")
    print("2.- Metodo de falsa posicion")
    print("3.- Metodo de Newton-Raphson")
    print("4.- Metodo de la secante")
    print("0.- Salir\n")

    while True:
        opcion = int(input("Ingrese la opcion que desee: "))
        if opcion > -1 and opcion < 5:
            break

    if(opcion == 1):
        Metodo_de_Biseccion.Metodo_Biseccion(expr)
    elif(opcion == 2):
        Metodo_de_la_Falsa_Posicion.Metodo_Falsa_Posicion(expr)
    elif(opcion == 3):
        Metodo_de_Newton_Raphson.Metodo_Newton_Raphson(expr)
    elif(opcion == 4):
        Metodo_de_la_Secante.Metodo_Secante(expr)

    while True:
        opcion = int(input("Desea continuar?\nSi - 1\nNo - 0\n"))
        if opcion > -1 and opcion < 2:
            break