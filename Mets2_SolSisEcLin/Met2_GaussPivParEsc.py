"""Modulo que contiene el Metodo de Eliminacion Gaussiana con Pivoteo Parcial Escalonado"""

import numpy as np

def Metodo_Gauss_PivParEsc(orden):
    """Funcion que llevara a cabo el Metodo de Eliminacion Gaussiana con Pivoteo Parcial Escalonado"""
    # Crea una matriz sin valores asignados para almacenar numeros de tipo 'float'
    A = np.empty((orden, orden + 1), dtype = 'f')

    # Bucle anidado para almacenar los valores ingresados por el usuario en la matriz
    for i in range(orden):
        for j in range(orden + 1):
            if j == orden:
                A[i, j] = float(input(f"Ingrese el resultado de la ecuacion {i + 1}: "))
            else:
                A[i, j] = float(input(f"Ingrese el elemento {i + 1, j + 1}: "))

    # Se crea la matriz que contendra los vectores fila: vector de escala y vector de indices
    V = np.empty((2, orden), dtype = 'f')
    for p in range(orden):
        auxMax = abs(A[p, 0])
        for q in range(orden):
            if auxMax < abs(A[p, q]):
                auxMax = abs(A[p, q])
        
        V[0, p] = auxMax  # Almacena los valores mayores de cada fila de la matriz A en la primera fila de la matriz de vectores fila 'V' (vector de escala)

    # Bucle que llenara la segunda fila de la matriz de vectores fila 'V' (vector de indices)
    for r in range(orden):
        V[1, r] = r

    # Bucle anidado que llevara a cabo el metodo
    for k in range(1, orden):  # Comienza desde la segunda ecuacion de la matriz
        auxMax = abs(A[k - 1, k - 1] / V[0, k - 1])
        auxMaxIndex = k - 1
        for o in range(k, orden):  # Bucle que busca el elemento que se usara como pivote (el elemento mayor de la columna)
            if auxMax < abs(A[o, k - 1] / V[0, o]):
                auxMax = abs(A[o, k - 1] / V[0, o])
                auxMaxIndex = o

        # Realiza los cambios necesarios en las columnas de la matriz de vectores fila 'V'
        vectFilaTemp = np.copy(V[:, k - 1])
        V[:, k - 1] = np.copy(V[:, auxMaxIndex])
        V[:, auxMaxIndex] = vectFilaTemp

        # Realiza el intercambio de los renglones
        vectorTemp = np.copy(A[auxMaxIndex])
        A[auxMaxIndex] = np.copy(A[k - 1])
        A[k - 1] = vectorTemp

        for l in range(k, orden):  # Bucle que convierte en cero los elementos por debajo del pivote
            # Calcula el numero que se usara para la conversion de los numeros debajo del pivote
            multiplicador = A[l, k - 1] / A[k - 1, k - 1]
            # Realiza las operaciones con los renglones de la matriz para convertir los numeros debajo del pivote en cero
            A[l] = (-1 * (multiplicador * A[k - 1])) + A[l]

    print("\n", np.around(A, decimals = 6))
    print("\nCambios: ", V[1, :], "\n")

    x = np.zeros(orden)  # Vector solucion
    # Bucle que llenara el vector solucion haciendo el despeje hacia atras
    for n in range(orden - 1, -1, -1):
        sumatoria = 0
        for m in range(orden - 1, -1, -1):
            sumatoria += (-1) * (x[m]) * (A[n, m])
        x[n] = (1 / A[n, n]) * (A[n, orden] + sumatoria)

    print("\nVector solucion: \n", np.around(np.transpose(x).reshape(orden, 1), decimals = 4))

if __name__ == "__main__":
    orden = int(input("Ingrese la cantidad de ecuaciones: "))
    Metodo_Gauss_PivParEsc(orden)