# Ejercicio 2.2.17
# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def sumar_digitos(numero: int)-> int:
    return sum(map(int, str(numero)))

def main():
    numero = int(input("introduce un nº: "))
    suma = sumar_digitos(numero)
    print(suma)

if __name__ == "__main__":
    main()