"""Modulo que contiene el Metodo de la Secante"""

import sys
import sympy as sp

def Secante(expresion, xr, incremento, tolerancia, limite):
    """Funcion que llevara a cabo el proceso del Metodo de la secante"""
    # Declaracion de la variable simbolica
    x = sp.symbols('x')
    # Convierte a la funcion a formato sympy
    fun = sp.sympify(expresion)
    # Variable auxiliar
    cont = 0

    print("-" * 86)
    print("|{:^8}|{:^12}|{:^30}|{:^31}|".format("x", "f(x)", "xr = (inc*fx)/(f(x+inc)-fx)", f"|f(xr)| < {tolerancia}"))
    print("-" * 86)

    # Bucle que se repetira hasta que se encuentre una aproximacion de la raiz o hasta que el se llegue al limite de iteraciones
    while(True):
        p = xr
        # Evalua las funciones en 'x = p'
        f_x = float(fun.subs(x, p))

        xr = xr - ((incremento * f_x) / (float(fun.subs(x, (xr + incremento))) - f_x))

        cont += 1

        # Evalua la funcion en la raiz estimada
        f_xr = float(fun.subs(x, xr))

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(f_xr) <= tolerancia

        print("|{:^8}|{:^12}|{:^30}|{:^18} - {:^10}|".format(round(p, 4), round(f_x, 8), round(xr, 4), round(abs(f_xr), 8), bool(aux)))

        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            break

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

    # Pide al usuario los valores necesarios para el metodo
    x1 = float(input("Ingrese un valor inicial: "))
    incr = float(input("Ingrese el incremento: "))
    error = float(input("Ingrese el error de tolerancia (en porcentaje): "))
    limite = int(input("Ingrese el limite de iteraciones: "))
    print()

    xr = Secante(expr, x1, incr, error, limite)

    print("\nUna aproximacion a la raiz es:", xr, "\n")

if __name__ == "__main__":
    expr = input("\nIntroduce la funcion en terminos de x: ")
    Metodo_Secante(expr)