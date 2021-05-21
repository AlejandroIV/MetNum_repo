"""Modulo que contiene el Metodo de Newton-Raphson"""

import sys
import sympy as sp

def Newton_Raphson(expresion, xr, tolerancia, limite):
    """Funcion que llevara a cabo el proceso del Metodo de Newton-Raphson"""
    # Declaracion de variable simbolica (esta variable no puede ser global, sino causaria errores)
    x = sp.symbols('x')
    # Convierte a la funcion a formato sympy y calcula la derivada
    f_X = sp.sympify(expresion)
    fPrima_X = f_X.diff(x)
    # Variable auxiliar
    cont = 0

    # Evalua la funcion sin derivar en 'x = xr'
    f_xr = float(f_X.subs(x, xr))
    # Evalua la funcion derivada en 'x = xr'
    fPrima_xr = float(fPrima_X.subs(x, xr))

    print("-" * 93)
    print("|{:^8}|{:^12}|{:^12}|{:^24}|{:^31}|".format("xn", "f(xn)", "f'(xn)", "x* = xn-(f(xn)/f'(xn))", f"|f(x*)| < {tolerancia}"))
    print("-" * 93)

    # Bucle que se repetira hasta que se encuentre una aproximacion de la raiz o hasta que el se llegue al limite de iteraciones
    while True:
        # Variable auxiliar
        xOld = xr

        # Condicional que termina el metodo en caso de que la derivada sea igual a cero
        if fPrima_xr == 0:
            print(f"La derivada de la funcion evaluada en el punto {xr} es igual a cero,por lo tanto, no es posible continuar con el metodo")
            print("Pruebe con otro intervalo")
            sys.exit(1)

        xr = xOld - (f_xr / fPrima_xr)

        cont += 1

        # Evalua la funcion sin derivar en 'x = xr'
        f_xr = float(f_X.subs(x, xr))
        # Evalua la funcion derivada en 'x = xr'
        fPrima_xr = float(fPrima_X.subs(x, xr))

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(f_xr) <= tolerancia

        print("|{:^8}|{:^12}|{:^12}|{:^24}|{:^18} - {:^10}|".format(round(xOld, 4), round(float(f_X.subs(x, xOld)), 4),
        round(float(fPrima_X.subs(x, xOld)), 4), round(xr, 4), round(abs(f_xr), 8), bool(aux)))

        # Condicional que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            break

        if cont == limite:
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("-" * 93)
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo\n\n")
            sys.exit(1)

    print("-" * 93)
    print("\nSe contaron ", cont, "iteraciones\n")

    return xr

def Metodo_Newton_Raphson(expr):
    print("\n\nMetodo de Newton Raphson\n")

    # Pide al usuario los valores necesarios para el metodo
    x = float(input("Ingrese un valor inicial: "))
    error = float(input("Ingrese el error de tolerancia (en porcentaje): "))
    limite = int(input("Ingrese el limite de iteraciones: "))

    xr = Newton_Raphson(expr, x, error, limite)

    print("\nUna aproximacion a la raiz es:", xr, "\n")

if __name__ == "__main__":
    expr = input("\nIntroduce la funcion en terminos de x: ")
    Metodo_Newton_Raphson(expr)