
def pedir_numero():
    numero = None
    while numero is None:
        try:   
            numero = int(input("Ingresa un nº para formar la piramide: "))
            if numero > 0:
                return numero
            elif numero < 0:
                print("ERROR. Nº negativo.")
                numero = None
        except ValueError:
            print("Cadenas no válidas.")

def validar_par_impar(numero: int)-> bool:
    if numero % 2 == 0:
        return True
    else:
        return False
    
def crear_piramide(numero: int):
    vacio = ""
    if numero % 2 == 0:
        for i in range(0, numero + 1, 2):
            vacio = str(i) + " " + vacio
            print(vacio)
    else:
        for i in range(1, numero + 1, 2):
            vacio = str(i) + " " + vacio
            print(vacio)
    

def main():
    numero = pedir_numero()
    if numero != None:
        crear_piramide(numero)


if __name__ == "__main__":
    main()