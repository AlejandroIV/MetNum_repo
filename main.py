import sympy as sp

# Declaracion de variable simbolica
x = sp.symbols('x')

#Pide al usuario la funcion
expr = input("Introduce la funcion en terminos de x: ")
fun = sp.sympify(expr)

print("\nMetdos Numericos\n")
print("1.- Metodo de biseccion")
print("2.- Metodo de falsa posicion")
print("3.- Metodo de Newton-Raphson")
print("4.- Metodo de la secante")
print("0.- Salir\n")

while(True):
    opcion = int(input("Ingrese la opcion que desee: "))
    if(opcion > -1 and opcion < 5):
        break

if(opcion == 1):
    print("Metodo de biseccion")
elif(opcion == 2):
    print("Metodo de falsa posicion")
elif(opcion == 3):
    print("Metodo de Newton-Raphson")
elif(opcion == 4):
    print("Metodo de la secante")