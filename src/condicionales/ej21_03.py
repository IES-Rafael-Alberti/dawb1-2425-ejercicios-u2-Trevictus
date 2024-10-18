# Ejercicio 2.1.3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numeros = []

def pedir_numeros()-> list:
    cont = 0
    while cont < 2:
        try:
            numero = float(input("Ingresa un nº: "))
            numeros.append(numero)
            cont += 1
        except ValueError:
            print("No es válido introducir una cadena de caracteres.")
    return numeros


def mostrar_division():
    try:
        division = numeros[0]/numeros[1]
        return f"La división del 1er nº entre el 2º da como resultado: {division}"
    except ZeroDivisionError:
        return "Introducir un cero como divisor no es posible de operar."


def main():
    pedir_numeros()
    print(mostrar_division())


if __name__ == "__main__":
    main()