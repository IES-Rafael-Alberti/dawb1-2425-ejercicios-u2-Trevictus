# Ejercicio 2.1.9
# 
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def preguntar_edad():
    num = None
    try:
        num = float(input("¿Cuál es tu edad?"))
    except:
        print("*ERROR*")

    return num

def asignar_precio_entrada(edad: float)-> str:
    if edad < 4:
        return "Puedes entrar gratis."
    elif 4 <= edad <= 18:
        return "Debes pagar 5€ para entrar."
    else:
        return "Debes pagar 10€ para entrar."


def main():
    edad = preguntar_edad()
    entrada = asignar_precio_entrada(edad)
    print(entrada)

if __name__ == "__main__":
    main()