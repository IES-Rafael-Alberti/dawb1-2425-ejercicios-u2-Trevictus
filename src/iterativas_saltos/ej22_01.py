# Ejercicio 2.2.1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def pedir_palabra()-> str:
    return input("Ingresa tu palabra preferida: ")

def mostrar_palabra_repetida(palabra: str)-> str:
    """
    cont = 0
    while cont < 10:
        print(palabra)
        cont +=1
    """
    vacio = ""
    for i in range (10):
        vacio += palabra + " "
    print(vacio)


def main():
    palabra = pedir_palabra()
    mostrar_palabra_repetida(palabra)

if __name__ == "__main__":
    main()