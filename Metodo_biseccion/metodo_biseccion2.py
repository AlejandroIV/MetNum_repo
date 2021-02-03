import math as m
import sys

"""Definicion de la funcion "f de x"""
def Funcion(x):
    #return pow(x, 10) - 1
    #return pow(x, 3) - x - 1
    return((668.06 / x) * (1 - pow(m.e, (-0.146843 * x))) - 40)

"""Regresa la cantidad de iteraciones necesarias para llegar al resultado deseado"""
def Iteraciones(deltaX, xInf, xSup):
    return m.log((deltaX) / (abs(xSup - xInf) / 2)) / m.log(2)

"""Definicion de la funcion que llevara a cabo el proceso del Metodo de Biseccion"""
def Biseccion(xInf, xSup, tolerancia, limite):
    # Variables auxiliares
    cont = 0
    argAux = xSup - xInf

    # Bucle que se repetira hasta que se encuentre la raiz
    while True:
        # Valor medio del intervalo
        xr = (xInf + xSup) / 2

        # Evalua la funcion en x1 y xr y almacena los valores en f_x1 y f_xr correspondientemente
        f_xInf = Funcion(xInf)
        f_xr = Funcion(xr)

        # Incrementa el contador de interacciones
        cont += 1

        if f_xInf * f_xr < 0:
            # La raiz se encuentra dentro del subintervalo inferior o izquierdo
            xSup = xr
        elif f_xInf * f_xr > 0:
            # La raiz se encuentra dentro del subintervalo superior o derecho *1 
            xInf = xr 
        elif f_xInf * f_xr == 0:
            # Se ha encontrado la raíz, por lo tanto, termina el calculo
            break

        #print(abs((xSup - xInf) / (xSup + xInf)))
        if (xSup + xInf) != 0:
            if (not(Funcion(xSup) * f_xInf > 0)) and (abs((xSup - xInf) / (xSup + xInf)) * 100 <= tolerancia):
                print(abs((xSup - xInf) / (xSup + xInf)) * 100)
                print("Se contaron ", Iteraciones(argAux, xInf, xSup), "iteraciones")
                break

        if cont == limite:
            # En caso que se hayan hecho 1000 iteraciones, entonces suponemos que
            # no existe raiz en el intervalo y se detiene la ejecucion del programa
            print("Se ha llegado al limite de iteraciones (1000) y no se ha encontrado una posible raiz")
            print("Pruebe con otro intervalo")
            sys.exit(1)

    return xr

# Pide al usuario los valores
x1 = float(input("Ingrese un valor inicial inferior: "))
x2 = float(input("Ingrese un valor final superior: "))
error = float(input("Ingrese el error de tolerancia (en porcentaje): "))
limite = int(input("Ingrese el limite de iteraciones: "))

xr = Biseccion(x1, x2, error, limite)

print("La posible raiz es:", xr)