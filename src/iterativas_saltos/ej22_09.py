# Ejercicio 2.2.9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasenia = "contraseña"

def preguntar_contrasenia():
    respuesta = input("Ingresa contraseña: ")
    while respuesta != contrasenia:
        print("ERROR. Inténtalo de nuevo: ")
        respuesta = input("Ingresa contraseña: ")
    return "Acceso concedido!"

def main():
    print(preguntar_contrasenia())

if __name__ == "__main__":
    main()