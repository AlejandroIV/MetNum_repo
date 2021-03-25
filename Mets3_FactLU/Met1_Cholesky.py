"""Modulo que contiene el Metodo de Descomposicion de Cholesky"""

import numpy as np
import sys
import math

def matrizA(orden):
    """Funcion para definir los elementos de la matriz A y comprobar que sea simetrica y definida positiva"""
    # Pide al usuario los elementos de la matriz 'A'
    global A
    A = np.zeros((orden, orden))
    for i in range(orden):
        for j in range(orden):
            A[i][j] = int(input(f"Ingrese el elemento {i + 1, j + 1}: "))
    
    # Comprueba si la matriz es simetrica
    Asimetrica = np.equal(A, np.transpose(A))
    for i in range(orden):
        for j in range(orden):
            if not(Asimetrica[i][j]):
                print("\n\nLa matriz no es simetrica, por lo tanto, no es posible continuar con el metodo")
                print("Pruebe ingresando otros elementos para la matriz\n\n")
                sys.exit(1)
    
    # Comprueba si la matriz es definida positiva
    for sub in range(1, orden + 1):
        if np.linalg.det(A[:sub, :sub]) < 0:
            print("\n\nLa matriz no es definida positiva, por lo tanto, no es posible continuar con el metodo")
            print("Pruebe ingresando otros elementor para la matriz\n\n")
            sys.exit(1)

def Metodo_Cholesky(orden):
    """Funcion que llevara a cabo el proceso del Metodo de Cholesky"""
    # Crea la matriz 'L' que contendra los elementos calculados por el metodo de cholesky
    L = np.zeros((orden, orden))
    matrizA(orden)

    for i in range(orden):
        for j in range(i, orden):
            # Si se va a calcular un elemento de la diagonal principal se ejecuta lo siguiente
            if i == j:
                sumatoria1 = 0
                for k in range(i - 1, -1, -1):
                    sumatoria1 += L[k, i] * L[k, i]
                L[i, j] = math.sqrt(A[i, j] - sumatoria1)
            # Si se va a calcular un elemento que no pertenece a la diagonal principal se ejecuta lo siguiente
            if i != j:
                sumatoria2 = 0
                for l in range(i - 1, -1, -1):
                    sumatoria2 += L[l, i] * L[l, j]
                L[i, j] = (A[i, j] - sumatoria2) / L[i, i]

    print("\nLa matriz 'L' es: ")
    print(L, "\n")

if __name__ == "__main__":
    orden = int(input("\nIngrese el orden de la matriz: "))
    Metodo_Cholesky(orden)