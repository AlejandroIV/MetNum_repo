"""Modulo que contiene las formulas de la Integracion Numerica (Newton Cotes) para calcular la integral"""

from sage.all import SR, sage, round
import numpy as np
from Mdls_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, FormulasInt

def Integracion_Numerica(nombre):
    """Funcion que aplicara las formulas de Integracion Numerica"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Pide al usuario una opcion
    dtsFormulas = FormulasInt(matDatos)

    # Si el usuario decide usar la formula de integracion trapecial [Burden p. 192]
    if dtsFormulas[1][0] == 1:
        # Termino que multiplica a las sumas
        integral = dtsFormulas[1][2] / 2
        # Termino de las sumas
        sumatoria = dtsFormulas[0][0, 1] + dtsFormulas[0][(dtsFormulas[1][1] - 1), 1]
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            sumatoria += 2 * dtsFormulas[0][suma, 1]

    # Si el usuario decide usar la formula de integracion de simpson 1/3
    elif dtsFormulas[1][0] == 2:
        # Termino que multiplica a las sumas
        integral = (dtsFormulas[1][2] / 3)
        # Termino de las sumas
        sumatoria = dtsFormulas[0][0, 1] + dtsFormulas[0][(dtsFormulas[1][1] - 1), 1]
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            # Terminos con indice impar
            if suma % 2 != 0:
                sumatoria += 4 * dtsFormulas[0][suma, 1]
            # Terminos con indice par
            else:
                sumatoria += 2 * dtsFormulas[0][suma, 1]

    # Si el usuario decide usar la formula de integracion de simpson 3/8
    elif dtsFormulas[1][0] == 3:
        # Termino que multiplica a las sumas
        integral = ((3 * dtsFormulas[1][2]) / 8)
        # Termino de las sumas
        sumatoria = dtsFormulas[0][0, 1] + dtsFormulas[0][(dtsFormulas[1][1] - 1), 1]
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            # Terminos con indice multiplo de 3
            if suma % 3 == 0:
                sumatoria += 2 * dtsFormulas[0][suma, 1]
            # Terminos con los indices restantes
            else:
                sumatoria += 3 * dtsFormulas[0][suma, 1]

    print(sumatoria)
    integral *= sumatoria

    # Imprime el resultado
    listaAux = ["regla del trapecio", "regla de simpson 1/3", "regla de simpson 3/8"]
    print(f"\n\nUsando la formula de integracion numerica {listaAux[dtsFormulas[1][0] - 1]} y con h = {dtsFormulas[1][2]}")
    print(f"La aproximacion de la integral de x = {dtsFormulas[0][0, 0]} a x = {dtsFormulas[0][(dtsFormulas[1][1] - 1), 0]}", end = " ")
    print(f"con {dtsFormulas[1][1]} nodos es: {round(integral, 7)}")

def IntegracionNumerica():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Integracion_Numerica(fNombre)

if __name__ == "__main__":
    Integracion_Numerica("prueba")