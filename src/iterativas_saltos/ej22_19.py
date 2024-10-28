# Ejercicio 2.2.19
# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
# Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
# Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

def menu():
    listado = ("Goma", "Lápiz", "Papel")
    finalizar = False
    while not finalizar:
        try:   
            opcion = int(input("Ingresa opción:\n1-> Comenzar programa.\n2-> Imprimir listado.\n3-> Finalizar programa.\n=>"))
            if opcion == 1:
                return "Programa comenzado."
            elif opcion == 2:
                return f"El listado es el siguiente: {", ".join(listado)}"
            elif opcion == 3:
                finalizar = True
            else:
                raise ValueError("ERROR. Ingresa una opción")
        except ValueError as _:
            print(f"ERROR. Ingresa una opción válida")

def main():
    print(menu())

if __name__ == "__main__":
    main()