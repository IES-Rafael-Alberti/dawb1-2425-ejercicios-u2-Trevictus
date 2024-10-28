# Ejercicio 2.2.22
# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

lista_par = []
lista_impar = []

def pedir_numeros():
    finalizar = False
    while not finalizar:    
        try:
            numero = int(input("Ingresa nºs enteros positivos: "))
            if numero < 0:
                print("ERROR. No puede ser negativo.")
            elif numero == 0:
                print("programa finalizado.")
                finalizar = True
            else:
                definir_par_impar(numero)
        except:
            print("ERROR debe ser un nº entero y positivo")
    return numero

def definir_par_impar(numero: int):
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

def contar_par_impar():
    return f"Has introducido {len(lista_par)} nºs pares y {len(lista_impar)} impares."


def main():
    pedir_numeros()
    print(contar_par_impar())

if __name__ == "__main__":
    main()