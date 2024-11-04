# Ejercicio 2.2.20
# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
# Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def pedir_cadena():
    cadena = input("Ingresa una frase: ")
    return cadena

def pedir_letra():
    letra = input("Ingresa una letra: ")
    return letra

def recorrer_frase(cadena, letra_encontrar):
    for i, letra in enumerate(cadena):
        if letra == letra_encontrar:
            print(f"Existe la letra {letra_encontrar} en indice {i}.")
        else:
            print(f"No hay coincidencia en {i}")



def main():
    cadena = pedir_cadena()
    letra = pedir_letra()
    recorrer_frase(cadena, letra)

if __name__ == "__main__":
    main()