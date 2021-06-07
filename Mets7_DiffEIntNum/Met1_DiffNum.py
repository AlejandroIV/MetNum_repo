"""Modulo que contiene las formulas ordinarias de la Derivacion Numerica para calcular la primera derivada"""

from sage.all import SR, sage, round
import numpy as np
from Mdls_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, FormulasDer

def Derivacion_Numerica(nombre):
    """Funcion que aplicara las formulas de la Derivacion Numerica"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Pide al usuario que elija una opcion
    dtsFormulas = FormulasDer(matDatos)

    # Aplica la formula segun sea el caso [Burden pp. 170, 171]
    # Si el usuario decide usar la formula de derivacion numerica centrada
    if dtsFormulas[1][0] == 3:
        # Si el usuario decide usar 3 puntos
        if dtsFormulas[1][1] == 3:
            derivada = (1 / (2 * dtsFormulas[1][2])) * (dtsFormulas[0][2, 1] - dtsFormulas[0][0, 1])
        # Si el usuario decide usar 5 puntos
        else:
            derivada = (1 / (12 * dtsFormulas[1][2])) * (dtsFormulas[0][0, 1] - (8 * dtsFormulas[0][1, 1]) + (8 * dtsFormulas[0][3, 1]) - dtsFormulas[0][4, 1])

    else:
        # Si el usuario decide usar la formula de derivacion numerica hacia adelante
        if dtsFormulas[1][0] == 1:
            # Si el usuario decide usar 3 puntos
            if dtsFormulas[1][1] == 3:
                derivada = (1 / (2 * dtsFormulas[1][2])) * (((-3) * dtsFormulas[0][0, 1]) + (4 * dtsFormulas[0][1, 1]) - dtsFormulas[0][2, 1])
            # Si el usuario decide usar 5 puntos
            else:
                derivada = (1 / (12 * dtsFormulas[1][2])) * (((-25) * dtsFormulas[0][0, 1]) + (48 * dtsFormulas[0][1, 1]) - (36 * dtsFormulas[0][2, 1]) \
                + (16 * dtsFormulas[0][3, 1]) - (3 * dtsFormulas[0][4, 1]))

        # Si el usuario decide usar la formula de derivacion numerica hacia atras
        else:
            # Si el usuario decide usar 3 puntos
            if dtsFormulas[1][1] == 3:
                derivada = (1 / (2 * dtsFormulas[1][2])) * (dtsFormulas[0][0, 1] - (4 * dtsFormulas[0][1, 1]) + (3 * dtsFormulas[0][2, 1]))
            # Si el usuario decide usar 5 puntos
            else:
                derivada = (1 / (12 * dtsFormulas[1][2])) * ((3 * dtsFormulas[0][0, 1]) - (16 * dtsFormulas[0][1, 1]) + (36 * dtsFormulas[0][2, 1]) \
                - (48 * dtsFormulas[0][3, 1]) + (25 * dtsFormulas[0][4, 1]))

    # Imprime el resultado
    listaAux = ["hacia adelante", "hacia atras", "centrada"]
    print(f"\n\nUsando la formula de diferenciacion numerica {listaAux[dtsFormulas[1][0] - 1]} y con h = {dtsFormulas[1][2]}")
    print(f"Al aproximar las formulas de {dtsFormulas[1][1]} puntos se obtiene que la primera derivada en el punto {dtsFormulas[2]} es: {round(derivada, 8)}")

def DerivacionNumerica():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Derivacion_Numerica(fNombre)

if __name__ == "__main__":
    Derivacion_Numerica("prueba")