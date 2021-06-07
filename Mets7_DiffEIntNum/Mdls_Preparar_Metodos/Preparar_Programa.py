"""Modulo que contiene las funciones necesarias para preparar los modulos que contiene los metodos de derivacion e integracion numerica"""

from sage.all import *
import sys
import numpy as np

def LLenar_Matriz_Datos(nombreArchTxt):
    """Funcion que lee un archivo de texto, extrae los datos ingresados y los almacena en una matriz para aplicar las formulas de derivacion o integracion"""
    try:
        archDts = open(f"{nombreArchTxt}.txt", "r")
    except:
        print("\nNo es posible abrir el archivo")
        print("Crea un archivo de texto e ingresa los datos ahí, guardalo con el formato 'txt' y vuelve a correr el programa\n")
        sys.exit(1)

    dts = ""
    # Bucle que recorre todo el archivo
    for parr in archDts:
        # Guarda en la variable 'dts' la cadena de texto con los datos que hay en el archivo de texto en formato 'str'
        dts += parr

    # Separa los datos delimitados por espacios
    dts = dts.split(' ')

    # Crea una matriz para almacenar los datos extraidos del archivo de texto
    matDts = np.empty((len(dts), 2), dtype = 'f')

    cont = 0
    # Bucle que recorre la lista con todos los datos ingresados por el usuario en el archivo de texto para separarlos
    for dato in dts:
        # Variables auxiliares que son los indices de los caracteres que se usan para delimitar los datos y separarlos
        indParentesis1 = dato.find("(")
        indParentesis2 = dato.find(")")
        indComa = dato.find(",")
        
        # Trata de convertir los datos en formato 'double' y los almacena en 'matDts'
        try:
            matDts[cont, 0] = float(dato[(indParentesis1 + 1):indComa])
            matDts[cont, 1] = float(dato[(indComa + 1):indParentesis2])
        except:
            print("\nAlguno de los datos no se ha podido convertir en un formato compatible que pueda usar el programa")
            print("Debe ingresar numeros para poder continuar\n")
            sys.exit(1)
        cont += 1

    # Cierra el archivo
    archDts.close()

    # Regresa la matriz con los datos extraidos desde el archivo de texto
    return matDts

def FormulasDer(matriz):
    """Funcion que pedira al usuario elegir que formula de derivacion numerica aplicar"""
    # Pide al usuario que lija una de las siguientes opciones
    print("\n1.- Diferencias finitas hacia adelante")
    print("2.- Diferencias finitas hacia atras")
    print("3.- Diferencias finitas centradas")
    # Crea la lista que contendra los valores que ingrese el usuario para aplicar las formulas de derivacion numerica
    lista = []

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 4:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Ingresa la opcion elegida por el usuario en la lista 'lista'
    lista.append(op)

    np.set_printoptions(precision = 6, suppress = True)

    # Imprime los datos
    print("\nLos datos ingresados son los siguientes:\n")
    # Bucle que recorre la matriz que contiene los datos y los imprime de manera enumerada para que el usuario elija los datos que desee utilizar
    for elem in range(matriz.shape[0]):
        print((elem + 1), end = "   -   ")
        print(matriz[elem, :])

    # Pide al usuario elegir que datos elegir cuantos datos elegir
    while True:
        try:
            op = int(input("\nCuantos valores desea usar (3 o 5)? "))
            if op == 3 or op == 5:
                break
            elif op > matriz.shape[0]:
                print(f"\nNo es posible usar {op} valores porque solo se han ingresado {matriz.shape[0]} valores de entrada")
                print("Agregue mas datos al archivo de texto y vuelve a correr el programa\n")
                sys.exit(1)
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Ingresa la opcion elegida por el usuario en la lista 'lista'
    lista.append(op)

    # Lista auxiliar para pedir al usuario el valor inicial
    listaAux = ["inferior", "superior", "centrado"]
    while True:
        try:
            op = int(input(f"Ingresa el dato {listaAux[lista[0] - 1]} que desee usar: "))
            if op > 0 and op < (matriz.shape[0] + 1):
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    op -= 1  # Resta uno porque se usara para indexar la fila de 'matriz'

    # Pide al usuario que ingrese un valor para 'h' positivo
    while True:
        try:
            h = float(input("\nIngrese un valor para 'h': "))
            if h > 0 and h % (matriz[1, 0] - matriz[0, 0]):
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    # Ingresa el valor de 'h' ingresado por el usuario en la lista 'lista'
    lista.append(h)

    # Divide el valor de 'h' ingresado por el usuario entre la diferencia entre los primeros valores de 'x' de 'matriz'
    h /= abs(matriz[1, 0] - matriz[0, 0])

    # Condicional que recorre el indice en caso de que se elija usar las formulas hacia atras y centradas
    if lista[0] == 2 and lista[1] == 3:  # Caso en el que se desea usar la formula hacia atras y 3 valores
        indiceIn = int(2 * round(h))

    elif lista[0] == 3 and lista[1] == 3:  # Caso en el que se desea usar la formula centrada y 3 valores
        indiceIn = int(round(h))

    elif lista[0] == 2 and lista[1] == 5:  # Caso en el que se desea usar la formula hacia atras y 5 valores
        indiceIn = int(4 * round(h))

    elif lista[0] == 3 and lista[1] == 5:  # Caso en el que se desea usar la fomrula centrada y 5 valores
        indiceIn = int(2 * round(h))

    else:  # Casos en el que se desea usar la formula hacia adelante
        # Para poder indexar el valor inferior
        indiceIn = op

    if lista[0] == 2 or lista[0] == 3:  # Casos en el que se desea usar la formula hacia atras o centrada
        # Para poder indexar el valor inferior
        indiceIn = op - indiceIn

    # Si el valor de 'indiceIn' es negativo significa que que no se pueden indexar mas valores anteriores
    if indiceIn < 0 or (indiceIn + ((lista[1] - 1) * round(h))) >= matriz.shape[0]:  # Si el valor de 'indiceIn' no puede indexar el valor superior
        print("\nAlgo ha salido mal!!!")
        print("Revise su entrada\n")
        sys.exit(1)

    # Crea el vector auxiliar que contendra los valores que se usaran en las formulas de diferenciacion numerica
    vectAux = np.empty((lista[1], 2), dtype = 'f')

    # Bucle que llenara el vector 'vectAux'
    for ind in range(lista[1]):
        vectAux[ind] = matriz[int(indiceIn + (round(h) * ind)), :]

    # Regresa el vector con los datos que se usaran en la formula, la lista con los valores [formula, cantidad de valores, el valor de h] y
    return(vectAux, lista, matriz[op, 0])  # el punto que se esta calculando de la derivada