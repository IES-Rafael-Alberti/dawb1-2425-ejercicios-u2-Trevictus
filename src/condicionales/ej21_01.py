#Ejercicio 2.1.1
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""
def preguntar_edad():
    num = None
    try:
        num = int(input("¿Cuál es tu edad?"))
    except:
        print("*ERROR*")

    return num
    

def comprobar_edad(edad)-> bool:
    if edad >= 18:
        return True
    return False

def mostrar_info(edad: int) -> str:
    if comprobar_edad(edad):
        return f"Con la edad de {edad} eres mayor."
    return f"Con la edad de {edad} eres menor."


    
def main():
    edad = preguntar_edad()
    if edad is not None:
        print(mostrar_info(edad))

if __name__ == "__main__":
    main()