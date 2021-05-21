"""Modulo que contiene el Metodo de la Falsa Posicion"""

import sys
import sympy as sp

def Falsa_Posicion(expresion, xInf, xSup, tolerancia, limite):
    """Funcion que llevara a cabo el proceso del Metodo de la Falsa Posicion"""
    # Declaracion de variable simbolica
    x = sp.symbols('x')
    # Convierte la funcion a formato sympy
    fun = sp.sympify(expresion)
    # Variables auxiliares
    cont = 0
    il = 0
    iu = 0

    # Evalua la funcion en "xInf" y "xSup" el valor los almacena en "f_xInf" y en "f_xSup" correspondientemente
    f_xInf = float(fun.subs(x, xInf))
    f_xSup = float(fun.subs(x, xSup))

    print("-" * 127)
    print("|{:^8}|{:^8}|{:^12}|{:^12}|{:^28}|{:^20}|{:^31}|".format("a", "b", "f(a)", "f(b)", "x = b-((fb*(a-b))/(fa-fb))", "f(a) * f(x) < 0",
    f"|f(x)| < {tolerancia}"))
    print("-" * 127)

    # Bucle que se repetira hasta que se encuentre una aproximacion de la raiz o hasta que el se llegue al limite de iteraciones
    while True:
        if il >= 2:
            # Si la variable "il" es igual o mayor a dos significa que se han sobrepasado el limite
            # de iteraciones y se debe ejecutar la siguinte sentencia para que el metodo sea mas ediciente
            f_xInf /= 2
        elif iu >= 2:
            # De manera anñaloga que con el caso anterior (mas informacion en pagina 108 del Chapra)
            f_xSup /= 2

        # Formula para determinar 'xr'
        xr = xSup - ((f_xSup * (xInf - xSup)) / (f_xInf - f_xSup))

        # Evalua la funcion en "xr" y almacena el valor en "f_xr"
        f_xr = float(fun.subs(x, xr))

        # Incrementa el contador de interacciones
        cont += 1

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux1 = abs(f_xr) <= tolerancia
        aux2 = f_xInf * f_xr < 0

        print("|{:^8}|{:^8}|{:^12}|{:^12}|{:^28}|{:^12} - {:^5}|{:^18} - {:^10}|".format(round(xInf, 4), round(xSup, 4), round(f_xInf, 4),
        round(f_xSup, 4), round(xr, 4), round((f_xInf * f_xr), 4), bool(aux2), round(abs(f_xr), 8), bool(aux1)))

        
        if (f_xInf * f_xr) < 0:
            # La raiz se encuentra dentro del subintervalo inferior o izquierdo
            xSup = xr
            f_xSup = f_xr
            # Reestablece el valor de la otra variable auxiliar para que empiece otro conteo
            iu = 0
            # Se incrementa el valor de la variable auxiliar para saber si se tiene que dividir el intervalo
            il += 1
        elif (f_xInf * f_xr) > 0:
            # La raiz se encuentra dentro del subintervalo superior o derecho
            xInf = xr
            f_xInf = f_xr
            # Reestablece el valor de la otra variable auxiliar para que empiece otro conteo
            il = 0
            # Se incrementa el valor de la variable auxiliar para saber si se tiene que dividir el intervalo
            iu += 1
        elif (f_xInf * f_xr) == 0:
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
            print("-" * 127)
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo\n\n")
            sys.exit(1)

    print("-" * 127)
    print("\nSe contaron ", cont, "iteraciones\n")

    return xr


def Metodo_Falsa_Posicion(expr):
    print("\n\nMetodo de la falsa posicion\n")

    # Pide al usuario los valores necesarios para el metodo
    x1 = float(input("Ingrese un valor inicial inferior: "))
    x2 = float(input("Ingrese un valor final superior: "))
    error = float(input("Ingrese el error de tolerancia: "))
    limite = int(input("Ingrese el limite de iteraciones: "))
    print()

    xr = Falsa_Posicion(expr, x1, x2, error, limite)

    print("\nUna aproximacion a la raiz es:", xr, "\n")

if __name__ == "__main__":
    expr = input("\nIntroduce la funcion en terminos de x: ")
    Metodo_Falsa_Posicion(expr)