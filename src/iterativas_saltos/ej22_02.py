# Ejercicio 2.2.2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def preguntar_edad():
    return int(input("¿Cuál es tu edad?\n"))

def mostrar_anios_cumplidos(edad: int):
    vacio = ""
    for i in range (edad + 1):
        vacio += str(i) + " "
    print(vacio)


def main():
    edad = preguntar_edad()
    mostrar_anios_cumplidos(edad)
    

if __name__ == "__main__":
    main()