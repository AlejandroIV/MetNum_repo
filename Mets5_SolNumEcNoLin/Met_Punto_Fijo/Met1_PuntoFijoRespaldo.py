"""Modulo que contiene el Metodo de Newton Modificado para la solucion de sistemas de ecuaciones no lineales"""

from sage.all import *
import sys
import numpy as np
import Preparar_Programa

def Metodo_Punto_Fijo(tolerancia, limite, nombre):
    """Funcion que llevara a cabo el Metodo del Punto Fijo"""
    # Primero llena un vector columna con las funciones contenidas en el documento de texto
    vectFun = Preparar_Programa.Llenar_Vector_Funciones(nombre)
    # Despues crea un vector de flotantes que contendra los valores de las variables dados por el usuario   
    vectSol = np.array([ 1.5,])

    # Se usa para considerar una presicion de 6
    np.set_printoptions(precision = 6, suppress = True)

    # Calcula la norma de 'vectSol'
    norma1 = np.linalg.norm(vectSol)

    # Crea la matriz que contendra los valores obtenidos en cada iteracion para poder imprimirlos
    matIter = np.copy(vectSol)
    matIter = np.append(matIter, 0)

    print('-' * (15 * vectSol.shape[0]))
    print((' ' * 5) + 'x' + (' ' * 4), sep = '', end = '')
    print((' ' * 6) + 'error')

    contIt = 0
    # Bucle que se repetira hasta que el error sea menor o igual al permitido
    while True:
        cont = 0
        # Bucle que recorrera todas las funciones contenidas en 'vectFun' y las evaluara
        while cont < np.size(vectSol):
            vectSol[cont] = vectFun[cont, 0].subs(x = vectSol[0], )
            cont += 1

        contIt += 1

        # Ingresa el vector 'vectSol' en una nueva columna de la matriz 'matIter'
        matIter = np.append(matIter, vectSol)

        # Calcula la norma de 'vectSol'
        norma2 = np.linalg.norm(vectSol)

        # Calcula el error aproximado porcentual y almacena el resultado en la variable 'errorAproxPorcen'
        errorAproxPorcen = ((norma2 - norma1) / norma2) * 100

        matIter = np.append(matIter, abs(errorAproxPorcen))

        if abs(errorAproxPorcen) < tolerancia:
            break

        if contIt == limite:
            matIter = np.reshape(matIter, ((contIt + 1), (vectSol.shape[0] + 1)))
            print("-" * (15 * vectSol.shape[0]))
            # Se imprimen los resultados por cada iteracion
            print(matIter)
            print("-" * (15 * vectSol.shape[0]))
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no se ha determinado el resultado y se detiene la ejecucion del programa
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado un posible resultado")
            print("Pruebe con otros valores a las variables iniciales\n\n")
            sys.exit(1)

        # Se copia el valor de 'normaX2' en la variable 'normaX1' para que en la siguiente iteracion se considere la norma que se acaba de calcular
        norma1 = norma2

    matIter = np.reshape(matIter, ((contIt + 1), (vectSol.shape[0] + 1)))

    print("-" * (15 * vectSol.shape[0]))
    # Se imprimen los resultados por cada iteracion
    print(matIter)
    print("-" * (15 * vectSol.shape[0]))
    print("\nSe contaron ", contIt, "iteraciones\n")

    # Regresa la solucion aproximada
    return vectSol

def Pto_Fij(FNombre):
    error = float(input("Ingresa la tolerancia: "))
    lim = float(input("Ingresa el limite de iteraciones: "))
    print(Metodo_Punto_Fijo(error, lim, FNombre))

if __name__ == "__main__":
    error = float(input("Ingresa la tolerancia: "))
    lim = float(input("Ingresa el limite de iteraciones: "))
    FNombre = input("Ingresa el nombre del archivo: ")
    print(Metodo_Punto_Fijo(error, lim, FNombre))