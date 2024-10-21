"""Actividad 1: Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. """

def introducir_numeros():
    encontrar_fin = False
    lista_numeros = []

    while not encontrar_fin:
        numeros = input("Introduce nºs y escribe fin para finalizar: ")
        
        if numeros == "fin":
            encontrar_fin = True
        else:
            try:
                lista_numeros.append(int(numeros))
            except ValueError:
                print("Por favor introduce nºs válidos.")
            
    print(f"Suma del total: {sum(lista_numeros)}\nTotal de nºs: {len(lista_numeros)}\nMedia total: {sum(lista_numeros)/len(lista_numeros)}")

def main():
    introducir_numeros()

if __name__ == "__main__":
    main()
