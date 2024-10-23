# Ejercicio 2.2.6
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# 
# *
# **
# ***
# ****
# *****


def pedir_numero():
    return int(input("Introduce un nº entero: "))

def mostrar_triangulo(altura: int):
    for i in range(1, altura + 1):
        print('*' * i)

def main():
    altura = pedir_numero()
    mostrar_triangulo(altura)


if __name__ == "__main__":
    main()