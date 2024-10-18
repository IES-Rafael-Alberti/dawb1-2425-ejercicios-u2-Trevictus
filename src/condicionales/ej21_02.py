# Ejercicio 2.1.2
"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

CONTRASENIA = "contraseña"

def pedir_contrasenia():
    return input("¿Cuál es la contraseña?\n").lower()


def comprobar_pass(password: str) -> bool:
    return password.lower() == CONTRASENIA.lower()


def main():
    cont_introducida = pedir_contrasenia()

    if comprobar_pass(cont_introducida):
        print(f"La contraseña {cont_introducida} coincide.")
    else:
        print(f"La contraseña { cont_introducida} no coincide con la contraseña.")


if __name__ == "__main__":
    main()