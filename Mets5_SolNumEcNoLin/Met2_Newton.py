"""Modulo que contiene el Metodo de Newton Modificado para la solucion de sistemas de ecuaciones no lineales"""

from sage.all import SR, jacobian, var
import sys
import numpy as np
from Met_Newton.Preparar_Programa import Llenar_Vector_Funciones

def Metodo_Newton(tolerancia, limite, nombre, opcion):
    """Funcion que llevara a cabo el Metodo de Newton"""
    # Primero llena un vector columna con las funciones contenidas en el documento de texto
    vectFun = Llenar_Vector_Funciones(nombre)
    # Despues crea un vector de flotantes que contendra los valores de las variables dados por el usuario   
    vectSol = np.array([3], dtype = 'f')
    vectSol = np.reshape(vectSol, (vectSol.shape[0], 1))
    # Declara las variables para poder calcular el jacobiano
    x = var('x')

    # Crea la matriz que contendra el jacobiano de las funciones
    matJac = np.empty(0, dtype = type(SR()))
    # Bucle que recorre todo el vector de funciones para calcular la matriz jacobiana y almacenarla en matJac
    for funcion in vectFun:
        # Ira calculando el jacobiano de cada fila
        filaJac = jacobian(funcion[0], (x))
        # Se selecciona 'funcion[0]' porque 'funcion' es una lista
        # Bucle que ira agregando las funciones una por una para separarlas
        for derPar in filaJac[0]:
            matJac = np.append(matJac, derPar)

    # Se usa para considerar una presicion de 6
    np.set_printoptions(precision = 6, suppress = True)

    matJac = np.reshape(matJac, ((vectFun.shape[0]), (vectFun.shape[0])))

    # Crea la matriz que se mandara como parametro para la funcion que va a calcular 'y' (aplicando el Metodo de Jacobi)
    mtrzY = np.empty((matJac.shape[0], (matJac.shape[0] + 1)), dtype = 'f')

    # Calcula la norma de 'vectSol'
    normaX1 = np.linalg.norm(vectSol)

    # Crea la matriz que contendra los valores obtenidos en cada iteracion para poder imprimirlos
    matIter = np.copy(vectSol)
    matIter = np.append(matIter, 0)

    contIt = 0
    # Bucle que se repetira hasta que el error sea menor o igual al permitido
    while True:
        # Bucle anidado que evaluara cada una de las funciones que hay en la matriz jacobiana y cada una que hay
        # en el vector columna que tiene las funciones y los resultados los ira almacenando en la matriz 'mtrzY'
        for cont1 in range(matJac.shape[0]):
            for cont2 in range(matJac.shape[0] + 1):
                # Cuando se cumple la condicion quiere decir que ahora hay que considerar la funcion del vector de funciones
                if cont2 == matJac.shape[0]:
                    # Se cambiara de signo cuando se evaluen las funciones
                    mtrzY[cont1, cont2] = (-1) * (vectFun[cont1][0].subs(x = vectSol[0, 0]))
                    continue
                mtrzY[cont1, cont2] = matJac[cont1, cont2].subs(x = vectSol[0, 0])

        if opcion == 1:
            # Manda a llamar a la funcion "Jacobi" para resolver el sistema de ecuaciones
            vectY = Met_Jacobi.Jacobi(mtrzY)
        else:
            # Calula la inversa del jacobiano y lo multiplica por el vector que contiene como valores las funciones evaluadas con signo negativo
            vectY = np.matmul(np.linalg.inv(mtrzY[:, :(matJac.shape[0])]), np.reshape(mtrzY[:, (matJac.shape[0]):], (matJac.shape[0], 1)))

        vectSol += vectY

        contIt += 1

        # Ingresa el vector 'vectSol' en una nueva columna de la matriz 'matIter'
        matIter = np.append(matIter, vectSol)

        # Calcula la norma de 'vectSol'
        normaX2 = np.linalg.norm(vectSol)

        # Calcula el error aproximado porcentual y almacena el resultado en la variable 'errorAproxPorcen'
        errorAproxPorcen = ((normaX2 - normaX1) / normaX2) * 100

        matIter = np.append(matIter, abs(errorAproxPorcen))

        if abs(errorAproxPorcen) < tolerancia:
            break

        if contIt == limite:
            matIter = np.reshape(matIter, ((contIt + 1), (vectSol.shape[0] + 1)))
            print("-" * (15 * vectSol.shape[0]))
            # Se imprimen los resultados por cada iteracion
            print(matIter)
            print("-" * (15 * vectSol.shape[0]))
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no se ha determinado el resultado y se detiene la ejecucion del programa
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado un posible resultado")
            print("Pruebe con otro vector inicial\n\n")
            sys.exit(1)

        # Se copia el valor de 'normaX2' en la variable 'normaX1' para que en la siguiente iteracion se considere la norma que se acaba de calcular
        normaX1 = normaX2

    print('-' * (15 * vectSol.shape[0]))
    print((' ' * 5) + 'x' + (' ' * 4), sep = '', end = '')
    print((' ' * 6) + 'error')

    matIter = np.reshape(matIter, ((contIt + 1), (vectSol.shape[0] + 1)))

    print("-" * (15 * vectSol.shape[0]))
    # Se imprimen los resultados por cada iteracion
    print(matIter)
    print("-" * (15 * vectSol.shape[0]))
    print("\nSe contaron ", contIt, "iteraciones\n")

    # Regresa la solucion aproximada
    return vectSol


def Newt(FNombre, op):
    error = float(input("Ingresa la tolerancia: "))
    lim = float(input("Ingresa el limite de iteraciones: "))
    print()
    print(Metodo_Newton(error, lim, FNombre, op))

if __name__ == "__main__":
    sys.path.append("..//")
    import Met_Jacobi
    FNombre = input("Ingresa el nombre del archivo: ")
    print("\nElije alguna de las siguientes opciones: ")
    print("1 - Usar el Metodo de Jacobi para determinar el valor del vector 'y'")
    print("2 - Calcular la inversa de la matriz jacobiana para determinar el valor del vector 'y'")
    opc = int(input("Opcion: "))
    print()
    error = float(input("Ingresa la tolerancia: "))
    lim = float(input("Ingresa el limite de iteraciones: "))
    print(Metodo_Newton(error, lim, FNombre, opc))
else:
    import Met_Jacobi