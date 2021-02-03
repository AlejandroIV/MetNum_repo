"""Modulo que contiene el Metodo de Newton-Raphson"""

import math as m
import sys
import sympy as sp

# Declaracion de variable simbolica
x = sp.symbols('x')

"""Definicion de la funcion 'f de x'"""
def Funciones():
    # Calcula la derivada de la funcion almacenada en "f_Y" para almacenarla en la variable 'fPrima_Y'
    fPrima_Y = f_Y.diff(x)

    # Diccionario que se regresara con la derivada y la funcion evaluada en el punto 'n'
    funciones = {"f de Y" : f_Y, "f prima de Y" : fPrima_Y}

    return funciones

"""Definicion de la funcion que llevara a cabo el proceso del Metodo de Newton-Raphson"""
def Newton_Raphson(xr, tolerancia, limite):
    # Declaracion de variable simbolica
    x = sp.symbols('x')
    # Variables auxiliares
    cont = 0
    funciones = Funciones()

    print("-" * 93)
    print("|{:^8}|{:^12}|{:^12}|{:^24}|{:^31}|".format("xn", "f(xn)", "f'(xn)", "x* = xn-(f(xn)/f'(xn))", f"|f(x*)| < {tolerancia}"))
    print("-" * 93)

    while True:
        # Variable auxiliar
        xOld = xr

        # Evalua la funcion sin derivar en 'x = n'
        f_xr = sp.sympify(funciones["f de Y"]).subs(x, xr)
        # Evalua la funcion derivada en 'x = n'
        fPrima_xr = sp.sympify(funciones["f prima de Y"]).subs(x, xr)

        xr = xOld - (f_xr / fPrima_xr)

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(sp.sympify(funciones["f de Y"]).subs(x, xr)) <= sp.Float(tolerancia)

        print("|{:^8}|{:^12}|{:^12}|{:^24}|{:^18} - {:^10}|".format(round(xOld, 4), round(f_xr, 4), round(fPrima_xr, 4), round(xr, 4),
        round(abs(sp.sympify(funciones["f de Y"]).subs(x, xr)), 8), bool(aux)))

        # Condicional que sirven como criterio de terminacion para terminar los calculos
        if abs(sp.sympify(funciones["f de Y"]).subs(x, xr)) <= sp.Float(tolerancia):
            break
        # Condicional que termina el metodo en caso de que la derivada sea igual a cero
        elif fPrima_xr == sp.Float(0):
            print(f"La derivada de la funcion evaluada en el punto {xr} es igual a cero,por lo tanto, no es posible continuar con el metodo")
            print("Pruebe con otro intervalo")
            sys.exit(1)

        cont += 1

        if cont == limite:
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("-" * 93)
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo\n\n")
            sys.exit(1)

    print("-" * 93)
    print("\nSe contaron ", cont, "iteraciones")

    return xr

def Metodo_Newton_Raphson(expr):
    print("\n\nMetodo de Newton Raphson\n")
    # Convierte a la funcion a formato sympy
    global f_Y
    f_Y = sp.sympify(expr)

    # Pide al usuario los valores necesarios para el metodo
    x = float(input("Ingrese un valor inicial: "))
    error = float(input("Ingrese el error de tolerancia (en porcentaje): "))
    limite = int(input("Ingrese el limite de iteraciones: "))

    xr = Newton_Raphson(x, error, limite)

    print("\nLa posible raiz es:", xr, "\n")