# Ejercicio 2.2.18
# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


def sumar_digitos(num: int)-> int:
    return sum(map(int, str(num)))

def es_par(numero: int)-> bool:
    return numero % 2 == 0 and numero != 0

def solicitar_numeros()-> int:
    finalizar = False
    while not finalizar:
        try:
            numero = int(input("Ingresa nº o -1 para finalizar: "))
            return numero
        except ValueError:
            print("No se admiten cadenas. Ingresa un nº: ")

def procesar_numeros(numero: int, cont_pares: int)-> int:
    if numero >= 0:
        suma = sumar_digitos(numero)
        print(suma)
        if es_par(numero):
            cont_pares += 1
    else:
        print("Ingresa un nº entero positivo: ")
    return cont_pares
def main():
    
    numero = 0
    cont_pares = 0
    while numero != -1:
        numero = solicitar_numeros()
        if numero != -1:
            cont_pares = procesar_numeros(numero, cont_pares)
    print(cont_pares)




if __name__ == "__main__":
    main()