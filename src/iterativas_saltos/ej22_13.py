# Ejercicio 2.2.13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def retornar_eco():
    salir = False
    eco = input("Escribe algo o 'salir' para finalizar el programa: ")
    if eco == "salir":
            print("Eco finalizado.")
            salir = True
    else:
            print(eco)
    while not salir:
        eco = input()
        if eco == "salir":
            print("Eco finalizado.")
            salir = True
        else:
            print(eco)
            



def main():
    retornar_eco()

if __name__ == "__main__":
    main()