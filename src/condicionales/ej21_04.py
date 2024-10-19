# Ejercicio 2.1.4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
from __init__ import *

def mostrar_par_impar(numero)-> str:
    try:    
        if int(numero)%2 == 0:
            return "El nº es par."
        else:
            return "El nº es impar."
    except ValueError:
        return "El programa no admite cadena de caracteres."
    except TypeError:
        return "El programa no admite cadena de caracteres."


def main():
    numero = pedir_numero()
    par_impar = mostrar_par_impar(numero)
    print(par_impar)

if __name__ == "__main__":
    main()