import math as m
import sys

"""Definicion de la funcion "f de x"""
def Funcion(x):
    #return pow(x, 10) - 1
    #return pow(x, 3) - x - 1
    return((668.06 / x) * (1 - pow(m.e, (-0.146843 * x))) - 40)

"""Definicion de la funcion que llevara a cabo el proceso del Metodo de la Falsa Posicion"""
def Falsa_Posicion(xInf, xSup, tolerancia):
    # Variables auxiliares
    cont = 0
    il = 0
    iu = 0

    # Evalua la funcion en "xInf" y "xSup" el valor los almacena en "f_xInf" y en "f_xSup" correspondientemente
    f_xInf = Funcion(xInf)
    f_xSup = Funcion(xSup)

    # Bucle que se repetira hasta que se encuentre la raiz
    while(True):

        if il >= 2:
            # Si la variable "il" es igual o mayor a dos significa que se han sobrepasado el limite
            # de iteraciones y se debe ejecutar la siguinte sentencia para que el metodo sea mas ediciente
            f_xInf /= 2
        elif iu >= 2:
            # De manera anñaloga que con el caso anterior (mas informacion en pagina 108 del Chapra)
            f_xSup /= 2

        # Valor medio del intervalo
        xr = xSup - ((f_xSup * (xInf - xSup)) / (f_xInf - f_xSup))

        # Evalua la funcion en "xr" el valor en "f_xr"
        f_xr = Funcion(xr)

        # Incrementa el contador de interacciones
        cont += 1

        if(f_xInf * f_xr < 0):
            # La raiz se encuentra dentro del subintervalo inferior o izquierdo
            xSup = xr
            f_xSup = Funcion(xSup)
            # Reestablece el valor de la otra variable auxiliar para que empiece otro conteo
            iu = 0
            # Se incrementa el valor de la variable auxiliar para saber si se tiene que dividir el intervalo
            il += 1
        elif(f_xInf * f_xr > 0):
            # La raiz se encuentra dentro del subintervalo superior o derecho
            xInf = xr
            f_xInf = Funcion(xInf)
            # Reestablece el valor de la otra variable auxiliar para que empiece otro conteo
            il = 0
            # Se incrementa el valor de la variable auxiliar para saber si se tiene que dividir el intervalo
            iu += 1
        elif(f_xInf * f_xr == 0):
            # Se ha encontrado la raíz, por lo tanto, termina el calculo
            break
        
        # Condicionales que sirven como criterio de terminacion para terminar los calculos
        if(not(f_xSup * f_xInf > 0)) and (abs((xSup - xInf) / (xSup + xInf)) * 100 <= tolerancia):
            print(abs((xSup - xInf) / (xSup + xInf)) * 100)
            break
        elif abs(f_xInf) <= tolerancia:
            print(abs(f_xInf))
            xr = xInf
            break
        elif abs(Funcion(xSup)) <= tolerancia:
            print(Funcion(xSup))
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

xr = Falsa_Posicion(x1, x2, error)

print("La posible raiz es:", xr)