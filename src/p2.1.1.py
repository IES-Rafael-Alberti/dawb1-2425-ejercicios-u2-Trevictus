#Ejercicio 2.1.1
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""

def comprobar_edad(edad: int)-> str:
    if edad >= 18:
        return f"Con la edad de {edad} eres mayor."
    else:
        return f"Con la edad de {edad} eres menor."
    
def main():
    edad = int(input("Ingresa tu edad: "))
    alerta = comprobar_edad(edad)
    print(alerta)

if __name__ == "__main__":
    main()