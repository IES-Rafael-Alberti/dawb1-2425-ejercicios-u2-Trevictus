# Ejercicio 2.1.5
"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

def preguntar_edad():
    num = None
    try:
        num = int(input("¿Cuál es tu edad?"))
    except:
        print("*ERROR*")

    return num

def preguntar_ingresos():
    num = None
    try:
        num = float(input("¿Cuales son tus ingresos mensuales?\n"))
    except:
        print("ERROR")
    return num

def mostrar_tributacion(edad, ingresos)-> str:
    if edad < 16 or ingresos < 1000:
        return "No tributas"
    elif edad >= 16 and ingresos >= 1000:
        return "Tributas"



def main():
    edad = preguntar_edad()
    ingresos = preguntar_ingresos()
    tributacion = mostrar_tributacion(edad, ingresos)
    print(tributacion)

if __name__ == "__main__":
    main()