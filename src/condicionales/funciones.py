import os 
import platform
import time 

# Funcion para introducir decimales
def pedir_numero():
    while True:
        valor = input("Ingresa un nº: ")
        try:
            return float(valor)
        except ValueError:
            print("No es válido introducir una cadena de caracteres.")


# Funcion para limpiar la consola
def borar_consola():
    sistema = platform.system() 
    if sistema == "Windows": 
        os.system('cls') 
    else: 
        os.system('clear')


#Funcion que valida si es un numero
def validar_numero():
    encontrar_fin = False
    while not encontrar_fin:
        try:
            numero = float(input("Ingresa nº: "))
            return numero
        except ValueError:
            print("Entrada no válida.")



print("Esto se imprimirá primero.") 
time.sleep(2) # Pausa la ejecución durante 2 segundos 
print("Esto se imprimirá después de 2 segundos.")
borar_consola()