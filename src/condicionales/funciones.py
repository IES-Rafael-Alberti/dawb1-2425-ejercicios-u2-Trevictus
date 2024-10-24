from os import system, name

# Funcion para introducir decimales
def pedir_numero():
    while True:
        valor = input("Ingresa un nº: ")
        try:
            return float(valor)
        except ValueError:
            print("No es válido introducir una cadena de caracteres.")


# Funcion para limpiar la consola
def clear():
    if name == 'nt':
        _ = system('cls')