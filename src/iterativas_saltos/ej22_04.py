# Ejercicio 2.2.4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def pedir_numero():
    return int(input("Introduce un nº entero positivo: "))

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