# Ejercicio 2.1.6
"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

LETRA_HOMBRE_GRUPO_A = "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
LETRA_MUJER_GRUPO_A = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"


def preguntar_nombre():
    return input("¿Cuál es tu nombre?\n")

def preguntar_sexo():
    return input("¿Cuál es tu sexo?\n")

def asignar_clase(nombre, sexo):
    letra = nombre[0]
    if sexo == "mujer":
        if letra.lower() in LETRA_MUJER_GRUPO_A:
            return "Perteneces al grupo A."
        else:
            return "Perteneces al grupo B."
    elif sexo == "hombre":
        if letra.lower() in LETRA_HOMBRE_GRUPO_A:
            return "Perteneces al grupo A."
        else:
            return "Perteneces al grupo B."
    else:
        return "Sexo no válido."

def main():
    nombre = preguntar_nombre()
    sexo = preguntar_sexo()
    grupo = asignar_clase(nombre, sexo)
    print(grupo)

if __name__ == "__main__":
    main()