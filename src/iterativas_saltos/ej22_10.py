# Ejercicio 2.2.10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True



def main():
    try:
        numero = int(input("Introduce un nº entero: "))
        if es_primo(numero):
            print(f"El nº {numero} es primo.")
        else:
            print(f"El nº {numero} no es primo.")
    except ValueError:
        print("ERROR, debes introducir un nº.")


if __name__ == "__main__":
    main()