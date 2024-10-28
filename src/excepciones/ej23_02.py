# Ejercicio 2.3.2
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def pedir_numero():
    try:
        numero = int(input("Introduce un nº entero positivo: "))
        if numero <= 0:
            raise ValueError("El nº debe ser entero positivo.")
        return numero
    except ValueError as e:
        print(f"ERROR. {e}.")
        return pedir_numero()

def mostrar_impares(numero: int):
    impares = []
    for i in range(1, numero + 1):
        if i % 2 != 0:
            impares.append(str(i))
    print(", ".join(impares))

def main():
    numero = pedir_numero()
    if numero > 0:
        mostrar_impares(numero)
    else:
        print("El nº debe ser entero positivo.")

if __name__ == "__main__":
    main()