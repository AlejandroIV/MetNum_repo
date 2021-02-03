import math as m
import sys
import sympy as s

"""Definicion de la funcion 'f de x'"""
def Funcion(n):

    #returnpow(n, 10) - 1
    #return(n**3) - n - 1
    #return ((668.06 / n) * (1 - pow(m.e, (-0.146843 * n))) - 40)
    #return (n**3) + (2 * (n**2)) - (29 * n) - 30
    #return s.exp(-1 * n) - n
    #return s.exp(-n**2) - n
    #return s.atan(n) - (2 * n) + 1
    #return s.cos(n) - (2**(-1 * n))
    #return (1/2) * (s.cos(n) + s.sin(n)) - n
    #return (n**3) + n + 16
    return s.sin(n) - s.csc(n) + 1

"""Definicion de la funcion que llevara a cabo el proceso del Metodo de la secante"""
def Secante(x, incremento, tolerancia):
    # Variable auxiliar
    cont = 0

    print("    x    ", "     f(x)     ", "  f(x + inc)  ", " xr = (inc * f(x)) / (f(x + inc) - f(x)) ", f"     |f(xn+1)| < {tolerancia}     ",
    sep = "|", end = "| \n")

    while(True):
        # Evalua las funciones en 'x = n'
        f_x = Funcion(x)

        xr = x - ((incremento * f_x) / (Funcion(x + incremento) - f_x))

        # Evalua la funcion en la raiz estimada
        f_xr = Funcion(xr)

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(f_xr) <= tolerancia
        print(" %4.4f  " % round(x, 4), "  %4.8f  " % round(f_x, 8), "  %4.8f  " % round(Funcion(x + incremento), 8),
        "                  %4.4f                 " % round(xr, 4),
        " %4.8f" % round(abs(f_xr), 8) + f"<= {tolerancia} - {aux}",
        sep = "|", end = "| \n")

        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            break
        else:
            x = xr

        cont += 1

        if cont == 100:
            # En caso que se hayan hecho 1000 iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("Se ha llegado al limite de iteraciones (100) y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo")
            sys.exit(1)

    print("Se contaron ", cont, "iteraciones")

    return xr

# Pide al usuario los valores
x1 = float(input("Ingrese un valor inicial: "))
incr = float(input("Ingrese el incremento: "))
error = float(input("Ingrese el error de tolerancia (en porcentaje): "))

xr = Secante(x1, incr, error)

print("La posible raiz es:", xr)