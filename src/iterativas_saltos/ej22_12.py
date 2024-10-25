# Ejercicio 2.2.12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def preguntar_frase():
    return input("Ingresa tu frase favorita: ")

def preguntar_letra():
    vocales = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"
    letra = input("Ingresa tu letra a contar: ").strip()
    try:
        if letra not in vocales:
            raise ValueError (f"La letra {letra} no está entre las vocales.")
        return letra
    except ValueError as e:
        print(e)
    return None

def contar_letras(frase: str, letra: str)-> int:
    return frase.lower().count(letra.lower())


def main():
    frase = preguntar_frase()
    letra = None
    while letra is None:
        letra = preguntar_letra()
    contar = contar_letras(frase, letra)
    print(f"La letra {letra} aparece {contar} veces en la frase.")

if __name__ == "__main__":
    main()