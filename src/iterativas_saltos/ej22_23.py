# Ejercicio 2.2.23
# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
# Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
# Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron.
# Ejemplo de ejecución:
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.


def ingresar_titulos():
    finalizar = False
    linea = ""
    contador_lineas = 0
    while not finalizar:
        try:
            libro = input("Ingresa un título de libro, ingresa '/' para terminar una linea o ingresa (asterisco) para finalizar:\n ")
            if libro == "/":
                validar_numericos(linea)
                contador_lineas += 1
                linea = ""
            elif libro == "*":
                print("Programa finalizado.")
                if linea:
                    validar_numericos(linea)
                    contador_lineas += 1
                finalizar = True
            else:
                linea = linea + libro
        except:
            print("ERROR desconocido.")
    print(f"Fin. Se leyeron {contador_lineas} líneas completas.")

def validar_numericos(libro):
    contador = 0
    for i in libro:
        if i.isdigit():
            contador += 1
    print(f"Línea completa. aparecen {contador} dígitos numéricos.")

def main():
    ingresar_titulos()
    

if __name__ == "__main__":
    main()