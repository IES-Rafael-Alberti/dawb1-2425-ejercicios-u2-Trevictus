# Ejercicio 2.3.3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
# Deberá solicitar el número hasta introducir uno correcto.

def pedir_numero():
    try:
        numero = int(input("Introduce un nº entero positivo: "))
        if numero <= 0:
            raise ValueError("El nº debe ser entero positivo.")
        return numero
    except ValueError as e:
        print(f"ERROR. {e}.")
        return pedir_numero()

def cuenta_atras(numero: int):
    numeros = []
    for i in range(numero, -1, -1):
        numeros.append(str(i))
    print(", ".join(numeros))

def main():
    numero = pedir_numero()
    if numero >= 0:
        cuenta_atras(numero)
    else:
        print("El nº debe ser entero positivo.")

if __name__ == "__main__":
    main()