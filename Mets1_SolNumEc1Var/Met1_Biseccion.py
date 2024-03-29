"""Modulo que contiene el Metodo de Biseccion"""

import sys
import sympy as sp

def Biseccion(expresion, xInf, xSup, tolerancia, limite):
    """Funcion que llevara a cabo el proceso del Metodo de Biseccion"""
    # Declaracion de variable simbolica
    x = sp.symbols('x')
    # Convierte la funcion a formato sympy
    fun = sp.sympify(expresion)
    # Variables auxiliares
    cont = 0

    print("-" * 111)
    print("|{:^8}|{:^8}|{:^12}|{:^18}|{:^27}|{:^31}|".format("a", "b", "f(a)", "x = (a + b) / 2", "f(a) * f(x) < 0", f"|f(x)| < {tolerancia}"))
    print("-" * 111)

    # Bucle que se repetira hasta que se encuentre una aproximacion de la raiz o hasta que el se llegue al limite de iteraciones
    while True:
        # Valor medio del intervalo
        xr = (xInf + xSup) / 2

        # Evalua la funcion en "xInf" y "xr" y almacena los valores en "f_xInf" y "f_xr" correspondientemente
        f_xInf = float(fun.subs(x, xInf))
        f_xr = float(fun.subs(x, xr))

        # Incrementa el contador de interacciones
        cont += 1

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux1 = abs(f_xr) <= tolerancia
        aux2 = f_xInf * f_xr < 0

        print("|{:^8}|{:^8}|{:^12}|{:^18}|{:^14} - {:^10}|{:^18} - {:^10}|".format(round(xInf, 4), round(xSup, 4), round(f_xInf, 8), round(xr,8), 
        round((f_xInf * f_xr), 8), bool(aux2), round(abs(f_xr), 8), bool(aux1)))

        if f_xInf * f_xr < 0:
            # La raiz se encuentra dentro del subintervalo inferior o izquierdo
            xSup = xr
        elif f_xInf * f_xr > 0:
            # La raiz se encuentra dentro del subintervalo superior o derecho
            xInf = xr 
        elif f_xInf * f_xr == 0:
            # Se ha encontrado la raíz, por lo tanto, termina el calculo
            break
        
        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            break
        elif abs(f_xInf) <= tolerancia:
            xr = xInf
            break
        elif abs(float(fun.subs(x, xSup))) <= tolerancia:
            xr = xSup
            break

        if cont == limite:
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("-" * 111)
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo\n\n")
            sys.exit(1)

    print("-" * 111)
    print("\nSe contaron ", cont, "iteraciones\n")

    return xr


def Metodo_Biseccion(expr):
    print("\n\nMetodo de Biseccion\n")

    # Pide al usuario los valores necesarios para el metodo
    x1 = float(input("Ingrese un valor inicial inferior: "))
    x2 = float(input("Ingrese un valor final superior: "))
    error = float(input("Ingrese el error de tolerancia: "))
    limite = int(input("Ingrese el limite de iteraciones: "))
    print()

    xr = Biseccion(expr, x1, x2, error, limite)

    print("\nUna aproximacion a la raiz es:", xr, "\n")

if __name__ == "__main__":
    expr = input("\nIntroduce la funcion en terminos de x: ")
    Metodo_Biseccion(expr)