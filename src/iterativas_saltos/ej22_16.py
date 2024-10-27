# Ejercicio 2.2.16
# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

lista_num = []

def validar_numero():
    encontrar_fin = False
    while not encontrar_fin:
        try:
            numero = float(input("Ingresa nº o 0 para terminar: "))
            return numero
        except ValueError:
            print("Entrada no válida.")


def main():
    encontrar_fin = False
    while not encontrar_fin:
        numero = validar_numero()
        lista_num.append(numero)
        if numero == 0:
            print(f"El mayor nº ingrsado ha sido el {max(lista_num)}")
            encontrar_fin = True

if __name__ == "__main__":
    main()