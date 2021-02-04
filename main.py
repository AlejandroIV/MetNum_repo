import Metodo_de_Biseccion
import Metodo_de_la_Falsa_Posicion
import Metodo_de_Newton_Raphson
import Metodo_de_la_Secante
import Metodo_de_Cholesky

opcion = 1

while opcion != 0:
    print("\nMetodos numericos\n")
    print("1.- Metodo de Descomposicion de Cholesky")
    print("2.- Menu de los metodos para aproximar las raices de ecuaciones")
    print("0.- Salir\n")
    
    # Pide al usuario que elija alguno de los metodos para aproximar raices de ecuaciones
    while True:
        opcion = int(input("Ingrese la opcion que desee: "))
        if opcion > -1 and opcion < 3:
            break

    if opcion == 1:
        orden = int(input("\nIngrese el orden de la matriz: "))
        Metodo_de_Cholesky.Metodo_Cholesky(orden)

    else:
        #Pide al usuario la funcion
        expr = input("\nIntroduce la funcion en terminos de x: ")

        print("\nMetodos para aproximar las raices de ecuaciones\n")
        print("1.- Metodo de biseccion")
        print("2.- Metodo de falsa posicion")
        print("3.- Metodo de Newton-Raphson")
        print("4.- Metodo de la secante")
        print("0.- Salir\n")

        # Pide al usuario que elija alguno de los metodos para aproximar raices de ecuaciones
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
        opcion = int(input("\n\nDesea continuar?\nSi - 1\nNo - 0\n"))
        if opcion > -1 and opcion < 2:
            break