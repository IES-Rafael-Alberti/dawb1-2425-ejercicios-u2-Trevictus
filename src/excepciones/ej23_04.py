# Ejercicio 2.3.4
# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def pedir_entero():
    try:
        numero = int(input("Ingresa nº entero: "))
        return numero
    except ValueError as e:
        print("La entrada no es correcta.")
        raise e


def main():
    try:
        numero = pedir_entero()
        print(f"Ingresaste el {numero}")
    except ValueError:
        print("ERROR. No se ingresó nº entero.")

if __name__ == "__main__":
    main()