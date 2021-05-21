from Mets1_SolNumEc1Var import Met1_Biseccion, Met2_FalsaPosicion, Met3_NewtonRaphson, Met4_Secante
from Mets2_SolSisEcLin import Met1_GaussPivPar, Met2_GaussPivParEsc, Met3_Jacobi, Met4_GaussSeidel
from Mets3_FactLU import Met1_Cholesky

opcion = 1

while opcion != 0:
    print("\nMetodos numericos\n")
    print("1.- Menu de los metodos para aproximar las raices de ecuaciones")
    print("2.- Menu de los metodos para aproximar la solucion a un sistema de ecuaciones lineales")
    print("3.- Menu de los metodos para factorizar matrices")
    print("0.- Salir\n")
    
    # Pide al usuario que elija alguno de los metodos para aproximar raices de ecuaciones
    while True:
        opcion = int(input("Ingrese la opcion que desee: "))
        if opcion > -1 and opcion < 4:
            break

    if opcion == 1:
        # Pide al usuario la funcion
        expr = input("\nIntroduce la funcion en terminos de x: ")

        print("\nMetodos para aproximar las raices de ecuaciones\n")
        print("1.- Metodo de biseccion")
        print("2.- Metodo de falsa posicion")
        print("3.- Metodo de Newton-Raphson")
        print("4.- Metodo de la secante")
        print("0.- Salir\n")

        # Pide al usuario que elija alguno de los metodos
        while True:
            opcion = int(input("Ingrese la opcion que desee: "))
            if opcion > -1 and opcion < 5:
                break

        # Manda a llamar al metodo que el usuario elija
        if opcion == 1:
            Met1_Biseccion.Metodo_Biseccion(expr)
        elif opcion == 2:
            Met2_FalsaPosicion.Metodo_Falsa_Posicion(expr)
        elif opcion == 3:
            Met3_NewtonRaphson.Metodo_Newton_Raphson(expr)
        elif opcion == 4:
            Met4_Secante.Metodo_Secante(expr)

    elif opcion == 2:
        # Pide al usuario la cantidad de ecuaciones
        orden = int(input("\nIngrese la cantidad de ecuaciones: "))

        print("\nMetodos para aproximar la solucion a un sistema de ecuaciones lineales\n")
        print("1.- Metodo de Gauss con pivoteo parcial")
        print("2.- Metodo de Gauss con pivoteo parcial escalonado")
        print("3.- Metodo de Jacobi")
        print("4.- Metodo de Gauss-Seidel")
        print("0.- Salir\n")

        # Pide al usuario que elija alguno de los metodos
        while True:
            opcion = int(input("Ingrese la opcion que desee: "))
            if opcion > -1 and opcion < 5:
                break

        # Manda a llamar al metodo que el usuario elija
        if opcion == 1:
            Met1_GaussPivPar.Metodo_Gauss_PivPar(orden)
        elif opcion == 2:
            Met2_GaussPivParEsc.Metodo_Gauss_PivParEsc(orden)
        elif opcion == 3:
            Met3_Jacobi.Metodo_de_Jacobi(orden)
        elif opcion == 4:
            Met4_GaussSeidel.Metodo_de_GaussSeidel(orden)

    elif opcion == 3:
        # Pide al usuario la cantidad de filas de la matriz
        orden = int(input("\nIngrese la cantidad de ecuaciones: "))

        print("\nMetodos de factorizacion LU\n")
        print("1.- Metodo de Descomposicion de Cholesky")

        # Pide al usuario que elija alguno de los metodos
        while True:
            opcion = int(input("Ingrese la opcion que desee: "))
            if opcion > -1 and opcion < 2:
                break

        # Manda a llamar al metodo que el usuario elija
        if opcion == 1:
            Met1_Cholesky.Metodo_Cholesky(orden)

    while True:
        opcion = int(input("\n\nDesea continuar?\nSi - 1\nNo - 0\n"))
        if opcion > -1 and opcion < 2:
            break