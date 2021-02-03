import math as m
import sys
import sympy as s

"""Definicion de la funcion 'f de x'"""
def Funciones():
    # Declaracion de variable simbolica
    x = s.symbols('x')

    #f_Y = pow(x, 10) - 1
    #f_Y = (x**3) - x - 1
    #f_Y = ((668.06 / x) * (1 - pow(m.e, (-0.146843 * x))) - 40)
    #f_Y = (x**3) + (2 * (x**2)) - (29 * x) - 30
    #f_Y = (s.exp(-1 * x)) - x
    #f_Y = s.cos(x) - (2**(-1 * x))
    #f_Y = (1/2) * (s.cos(x) + s.sin(x)) - x
    #f_Y = (x**3) + x + 16
    f_Y = s.log((x**2) + 1) - (s.exp(x / 2) * s.cos(s.pi * x))

    # Calcula la derivada para almacenarla en la variable 'fPrima_Y'
    fPrima_Y = f_Y.diff(x)

    # Diccionario que se regresara con la derivada y la funcion evaluada en el punto 'n'
    funciones = {"f de Y" : f_Y, "f prima de Y" : fPrima_Y}

    return funciones

"""Definicion de la funcion que llevara a cabo el proceso del Metodo de Newton-Raphson"""
def Newton_Raphson(xr, tolerancia):
    # Declaracion de variable simbolica
    x = s.symbols('x')
    # Variables auxiliares
    cont = 0
    funciones = Funciones()

    print("   xn    ", "     f(xn)     ", "     f'(xn)     ", "  xn+1 = xn - f(xn) / f'(xn)  ", f"     |f(xn+1)| < {tolerancia}    ",
    sep = "|", end = "| \n")

    while(True):
        # Variable auxiliar
        xOld = xr

        # Evalua la funcion sin derivar en 'x = n'
        f_xr = s.sympify(funciones["f de Y"]).subs(x, xr)
        # Evalua la funcion derivada en 'x = n'
        fPrima_xr = s.sympify(funciones["f prima de Y"]).subs(x, xr)

        xr = xOld - (f_xr / fPrima_xr)

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux = abs(s.sympify(funciones["f de Y"]).subs(x, xr)) <= s.Float(tolerancia)
        print(" %4.4f  " % round(xOld, 4), " %4.9f " % round(f_xr, 4), "   %4.8f  " % round(fPrima_xr, 4),
        "          %4.8f          " % round(xr, 4),
        "%4.8f" % round(abs(s.sympify(funciones["f de Y"]).subs(x, xr)), 8) + f"<= {tolerancia} - {aux}",
        sep = "|", end = "| \n")

        # Condicional que sirven como criterio de terminacion para terminar los calculos
        if abs(s.sympify(funciones["f de Y"]).subs(x, xr)) <= s.Float(tolerancia):
            break
        # Condicional que termina el metodo en caso de que la derivada sea igual a cero
        elif fPrima_xr == s.Float(0):
            print(f"La derivada de la funcion evaluada en el punto {xr} es igual a cero,por lo tanto, no es posible continuar con el metodo")
            print("Pruebe con otro intervalo")
            sys.exit(1)

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
x = float(input("Ingrese un valor inicial: "))
error = float(input("Ingrese el error de tolerancia (en porcentaje): "))

xr = Newton_Raphson(x, error)

print("La posible raiz es:", round(xr, 4))