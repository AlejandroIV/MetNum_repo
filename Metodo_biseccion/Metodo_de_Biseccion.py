import math as m
import sys
import sympy as s

"""Definicion de la funcion "f de x"""
def Funcion(x):
    return x**3 - x - 1
    #return pow(x, 10) - 1
    #return pow(x, 3) - x - 1
    #return((668.06 / x) * (1 - pow(m.e, (-0.146843 * x))) - 40)
    #return s.cos(x) - (2**(-1 * x))
    #return (1/2) * (s.cos(x) + s.sin(x)) - x
    #return (x**3) + x + 16
    #return s.ln((x**2) + 1) - (s.exp(x / 2) * s.cos(s.pi * x))

"""Definicion de la funcion que llevara a cabo el proceso del Metodo de Biseccion"""
def Biseccion(xInf, xSup, tolerancia):
    # Variables auxiliares
    cont = 0
    print("| a | b | f(a) | x = (a + b) / 2", f"| |f(x)| < {tolerancia} | f(a) * f(x) < 0 |")
    print("   a  ", "b  ", "f(a)   ", "x = (a + b) / 2  ", f"     |f(x)| < {tolerancia}    ",
    "f(a) * f(x) < 0", sep = "|       ", end = "    | \n")

    # Bucle que se repetira hasta que se encuentre la raiz
    while(True):
        # Valor medio del intervalo
        xr = (xInf + xSup) / 2

        # Evalua la funcion en "xInf" y "xr" y almacena los valores en "f_xInf" y "f_xr" correspondientemente
        f_xInf = Funcion(xInf)
        f_xr = Funcion(xr)

        # Error relativo porcentual sin conocer el valor verdadero
        #print(abs(xr), "-", abs(xInf), "/", abs(xr), "* 100 es igual a", abs((abs(xr) - abs(xInf)) / abs(xr)) * 100)
        # Error relativo porcentual conociendo el valor verdadero
        #print(14.8011, "-", xr, "/", 14.8011, "* 100 da igual a ", (abs((14.8011 - xr) / 14.8011) * 100))

        # Incrementa el contador de interacciones
        cont += 1

        # En estas sentencias la raiz siempre se encuentra dentro del intervalo, por lo tanto, 
        # el intervalo se ira cerrando hasta que su longitud del intervalo sea menor a la tolerancia
        #if(abs((abs(xr) - abs(xInf)) / abs(xr)) * 100 <= tolerancia):
        #    break

        # Asignacion de valores a variables auxiliares para imprimirlos
        aux1 = abs(f_xr) <= tolerancia
        aux2 = f_xInf * f_xr < 0
        print("%4.4f" % round(xInf, 4), "%4.4f" % round(xSup, 4), "%4.7f" % round(f_xInf, 4), "%4.18f" % round(xr, 4), 
        "%4.8f" % round(abs(f_xr), 8) + f"<= {tolerancia} - {aux1}", "%4.8f" % (f_xInf * f_xr) + f"< 0 - {aux2}", sep = "|    ",
        end = " | \n")

        if(f_xInf * f_xr < 0):
            # La raiz se encuentra dentro del subintervalo inferior o izquierdo
            xSup = xr
        elif(f_xInf * f_xr > 0):
            # La raiz se encuentra dentro del subintervalo superior o derecho
            xInf = xr 
        elif(f_xInf * f_xr == 0):
            # Se ha encontrado la raíz, por lo tanto, termina el calculo
            break
        
        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if abs(f_xr) <= tolerancia:
            break
        elif abs(f_xInf) <= tolerancia:
            xr = xInf
            break
        elif abs(Funcion(xSup)) <= tolerancia:
            xr = xSup
            break

        if cont == 1000:
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

xr = Biseccion(x1, x2, error)

print("La posible raiz es:", xr)