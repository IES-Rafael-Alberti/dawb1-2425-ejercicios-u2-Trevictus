import random



def bienvenida():
    print("Bienvenido a adivinar numero!!!")

def menu():
    intentos = 5
    numero_maximo = 100
    finalizar = False
    while not finalizar:
        opcion = int(input("Introduce una opcion:\n1=> Jugar\n2=> Configurar\n3=> Mostrar configuración\n4=>Salir\n->"))
        if opcion == 1:
            jugar(intentos, numero_maximo)
        elif opcion == 2:
            intentos, numero_maximo = configurar()
        elif opcion == 3:
            mostrar_configuracion(intentos, numero_maximo)
        elif opcion == 4:
            finalizar = True
            print("Programa finalizado.")
        else:
            print("Opción no válida")
    return opcion

def jugar(intentos, numero_maximo):
    numero_aleatorio = random.randint(0, numero_maximo)
    while intentos > 0:
        eleccion_jugador = int(input("Intenta adivinar el numero entre 0 y 100.\n"))
        if eleccion_jugador == numero_aleatorio:
            print("Enhorabuena, has ganado.")
        elif eleccion_jugador < numero_aleatorio:
            print("El nº que buscas es mayor.")
        elif eleccion_jugador > numero_aleatorio:
            print("El nº que buscas es menor.")
        
        intentos -= 1
        print(f"Lo siento... Te quedan {intentos} intentos.")
    print("Has perdido")

def configurar():
    finalizar = False
    while not finalizar:
        try:
            intentos = int(input("Intentos a realizar: "))
            if intentos <= 0:
                raise ValueError("Los intentos introducidos deben ser mayor a 0.")
            numero_maximo = int(input("El nº aleatorio se generará de 0 a : "))
            if numero_maximo <= 0:
                raise ValueError("El rango debe ser mayor a 0.")
            return intentos, numero_maximo
        except ValueError as e:
            print(f"ERROR. {e}")

def mostrar_configuracion(intentos, numero_maximo):
    print(f"Configuracion actual:\nIntentos: {intentos}\nRango nº aleatorio: 0 a {numero_maximo}")




def main():
    menu()

if __name__ == "__main__":
    main()







