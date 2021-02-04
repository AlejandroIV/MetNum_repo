"""Modulo que contiene el Metodo de la Secante"""

import math as m
import sys
import sympy as sp

# Declaracion de la variable simbolica
x = sp.symbols('x')

def Funcion(n):
    """Definicion de la funcion 'f de x'"""
    return float(fun.subs(x, n))

def Secante(x, incremento, tolerancia, limite):
    """Funcion que llevara a cabo el proceso del Metodo de la secante"""
    # Variable auxiliar
    cont = 0

    print("-" * 86)
    print("|{:^8}|{:^12}|{:^30}|{:^31}|".format("x", "f(x)", "xr = (inc*fx)/(f(x+inc)-fx)", f"|f(xr)| < {tolerancia}"))
    print("-" * 86)

    while(True):
        # Evalua las funciones en 'x = n'
        f_x = Funcion(x)

        xr = x - ((incremento * f_x) / (Funcion(x + incremento) - f_x))

        # Evalua la funcion en la raiz estimada
        f_xr = Funcion(xr)

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(f_xr) <= tolerancia

        print("|{:^8}|{:^12}|{:^30}|{:^18} - {:^10}|".format(round(x, 4), round(f_x, 8), round(xr, 4), round(abs(f_xr), 8), bool(aux)))

        cont += 1

        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            break
        else:
            x = xr

        if cont == limite:
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("-" * 86)
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo\n\n")
            sys.exit(1)

    print("-" * 86)
    print("\nSe contaron ", cont, "iteraciones\n")

    return xr

def Metodo_Secante(expr):
    print("\n\nMetodo de la Secante\n")
    # Convierte a la funcion a formato sympy
    global fun
    fun = sp.sympify(expr)

    # Pide al usuario los valores necesarios para el metodo
    x1 = float(input("Ingrese un valor inicial: "))
    incr = float(input("Ingrese el incremento: "))
    error = float(input("Ingrese el error de tolerancia (en porcentaje): "))
    limite = int(input("Ingrese el limite de iteraciones: "))
    print()

    xr = Secante(x1, incr, error, limite)

    print("La posible raiz es:", xr)