# Ejercicio 2.2.11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def pedir_palabra():
    return input("Ingresa tu palabra preferida: ")

def mostrar_letras_reves(palabra):
    vacio = ""
    for letra in reversed(palabra):
        vacio += letra + " "
    print(vacio)

def main():
    palabra = pedir_palabra()
    mostrar_letras_reves(palabra)

if __name__ == "__main__":
    main()