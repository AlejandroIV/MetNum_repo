"""Modulo que contiene el Metodo de Jacobi"""

import numpy as np
import sys

def Jacobi(orden, tolerancia, limite, A, x):
    """Funcion que llevara a cabo el Metodo de Jacobi"""
    # Manda a llamar a la funcion para hacer el intercambio de los renglones necesarios, de tal manera que la matriz resultante sea una matriz diagonal dominante
    A = MatDiagDom.Matriz_Diagonal_Dominante(A)

    # Bucle anidado que modifica la matriz A para poder aplicar el metodo de Jacobi
    for fil in range(A.shape[0]):
        denominador = A[fil, fil]
        for col in range(A.shape[1]):
            # Condicional para cambiar la componente de la diagonal por cero
            if col == fil:
                A[fil, col] = 0
            else:
                if (col + 1) == A.shape[1]:
                    A[fil, col] /= denominador
                else:
                    A[fil, col] /= -denominador

    T = np.copy(A[:, :orden])

    c = np.copy(A[:, orden:])

    # Sentencias para calcular la norma de 'x'
    normaX1 = np.linalg.norm(x)

    cont = 0

    # Crea la matriz que contendra los valores obtenidos en cada iteracion para poder imprimirlos
    matIter = np.copy(x)
    matIter = np.append(matIter, 0)
    print("-" * (15 * x.shape[0]))
    for cantElem in range(x.shape[0]):
        print("    x", (cantElem + 1), "    ", sep = "", end = "")
    print("   error")

    # Bucle que se repetira hasta que el error sea menor o igual al permitido o hasta que se llegue al limite de iteraciones
    while True:
        # Multiplica la matriz 'T' por el vector 'x' y le suma el vector 'c'
        x = np.matmul(T, np.reshape(x, (orden, 1))) + np.reshape(c, (orden, 1))

        cont += 1

        # Ingresa el vector 'x' en una nueva fila de la matriz 'matIter'
        matIter = np.append(matIter, x)

        # Sentencias para calcular la norma de 'x'
        normaX2 = np.linalg.norm(x)

        # Calcula el error aproximado porcentual y almacena el resultado en la variable 'errorAproxPorcen'
        errorAproxPorcen = ((normaX2 - normaX1) / normaX2) * 100

        matIter = np.append(matIter, abs(errorAproxPorcen))

        if abs(errorAproxPorcen) < tolerancia:
            break

        if cont == limite:
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no se ha determinado el resultado y se detiene la ejecucion del programa
            print("-" * (15 * x.shape[0]))
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado un posible resultado")
            print("Pruebe con otro vector inicial\n\n")
            sys.exit(1)

        # Se copia el valor de 'normaX2' en la variable 'normaX1' para que en la siguiente iteracion se considere la norma que se acaba de calcular
        normaX1 = normaX2

    matIter = np.reshape(matIter, ((cont + 1), (x.shape[0] + 1)))
    np.set_printoptions(precision = 6, suppress = True)

    print("-" * (15 * x.shape[0]))
    # Se imprimen los resultados por cada iteracion
    print(matIter)
    print("-" * (15 * x.shape[0]))
    print("\nSe contaron ", cont, "iteraciones\n")

    return x

def Metodo_de_Jacobi(orden):
    # Crea una matriz sin valores asignados para almacenar numeros de tipo 'float'
    matriz = np.empty((orden, orden + 1), dtype = 'f')

    print()
    # Bucle anidado para almacenar los valores ingresados por el usuario en la matriz
    for i in range(orden):
        for j in range(orden + 1):
            if j == orden:
                matriz[i, j] = float(input(f"Ingrese el resultado de la ecuacion {i + 1}: "))
            else:
                matriz[i, j] = float(input(f"Ingrese el elemento {i + 1, j + 1}: "))

    print("\nIngrese el vector incial para comenzar con el metodo\n")
    # Crea el vector inicial para comenzar con el metdo y se llena en el bucle for
    vectorIn = np.empty(orden, dtype = 'f')
    for comp in range(orden):
        vectorIn[comp] = float(input(f"Ingrese la componente {comp + 1} del vector: "))

    # Pide al usuario los valores necesarios para el metodo
    error = float(input("Ingrese el error de tolerancia (porcentaje): "))
    limite = float(input("Ingrese el limite de iteraciones: "))
    print()

    vectorSol = Jacobi(orden, error, limite, matriz, vectorIn)

    print("\nUna aproximacion a la solucion es:\n", np.transpose(vectorSol).reshape(orden, 1))

if __name__ == "__main__":
    sys.path.append("..//")
    from ModulosAdicionales import MatDiagDom
    orden = int(input("Ingrese la cantidad de ecuaciones: "))
    Metodo_de_Jacobi(orden)
else:
    from ModulosAdicionales import MatDiagDom