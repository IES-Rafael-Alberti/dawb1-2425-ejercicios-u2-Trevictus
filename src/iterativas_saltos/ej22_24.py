# Ejercicio 2.2.24
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad de números primos ingresados.

def pedir_numeros():
    lista_numeros = []
    finalizar = False
    while not finalizar:
        try:
            numeros = int(input("Ingresa nºs: "))
            if numeros == 0:
                print("Programa finalizado.")
                finalizar = True
            elif numeros > 1:
                lista_numeros.append(numeros)
            else:
                print("ERROR. No se admiten nºs negativos.")
        except ValueError:
            print("Ingresa un nº válido por favor. ")
    return lista_numeros

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    numeros = pedir_numeros()
    primos = []
    for num in numeros:
        if es_primo(num):
            primos.append(num)
    print(f"La cantidad de nºs primos es: {len(primos)}")

if __name__ == "__main__":
    main()