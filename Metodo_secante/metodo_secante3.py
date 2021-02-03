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
def Secante(xInf, xSup, tolerancia):
    # Variable auxiliar
    cont = 0

    print("    a    ", "    b    ", "    f(a)    ", "    f(b)     ", "  xr = (f(b)(a - b)) / (f(a) - f(b))  ",
    f"      |f(xr)| < {tolerancia}       ", sep = "|", end = "| \n")

    while(True):
        # Evalua las funciones en 'x = n'
        f_xSup = Funcion(xSup)
        f_xInf = Funcion(xInf)

        xr = xSup - ((f_xSup * (xInf - xSup)) / (f_xInf - f_xSup))

        f_xr = Funcion(xr)

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(f_xr) <= tolerancia
        print(" %4.4f  " % round(xInf, 4), " %4.4f  " % round(xSup, 4), " %4.8f " % round(f_xInf, 4), " %4.8f " % round(f_xSup, 4),
        "                %4.4f                " % round(xr, 4),
        " %4.8f " % round(f_xr, 8) + f"<= {tolerancia} - {aux}", sep = "|", end = "| \n")

        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            print(abs(f_xr))
            break
        else:
            xInf = xSup
            xSup = xr

        cont += 1

        if cont == 10:
            # En caso que se hayan hecho 1000 iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("Se ha llegado al limite de iteraciones (1000) y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo")
            sys.exit(1)

    print("Se contaron ", cont, "iteraciones")

    return xr

# Pide al usuario los valores
x1 = float(input("Ingrese un valor inicial inferior: "))
x2 = float(input("Ingrese un valor final superior: "))
error = float(input("Ingrese el error de tolerancia (en porcentaje): "))

xr = Secante(x1, x2, error)

print("La posible raiz es:", xr)