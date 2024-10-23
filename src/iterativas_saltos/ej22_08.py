# Ejercicio 2.2.8
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

def pedir_numero():
    return int(input("Introduce un nº entero: "))

def mostrar_triangulo(altura: int):
    for i in range(1, altura + 1):
        vacio = ""
        for j in range(i * 2 - 1, 0, -2):
            vacio += str(j) + " "
        print(vacio)

def main():
    altura = pedir_numero()
    mostrar_triangulo(altura)

if __name__ == "__main__":
    main()