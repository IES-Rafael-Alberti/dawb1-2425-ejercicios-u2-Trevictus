# Ejercicio 2.2.15
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

lista_num = []

def validar_numero():
    encontrar_fin = False
    while not encontrar_fin:
        try:
            numero = float(input("Ingresa nº o 0 para terminar: "))
            # if numero < 0:
            #     raise ValueError("No se permiten nºs negativos.")
            return numero
        except ValueError:
            print("Cadenas no permitidas.")
        # except ValueError as e:
        #     print(f"{e}")


def main():
    encontrar_fin = False
    while not encontrar_fin:
        numero = validar_numero()
        if numero >= 0:
            lista_num.append(numero)
        if numero == 0:
            print(f"Nºs ingresados {lista_num}")
            print(f"La suma de los nºs ingresados es: {sum(lista_num)}")
            encontrar_fin = True

if __name__ == "__main__":
    main()