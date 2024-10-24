# Ejercicio 2.2.7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def mostrar_tabla_multiplicar():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print("---------")


def main():
    mostrar_tabla_multiplicar()

if __name__ == "__main__":
    main()