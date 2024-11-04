# Ejercicio 2.2.5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# 
# # Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# # En donde:
# # - amount: Cantidad a invertir
# # - interest: Interes porcentual anual 

def preguntar_amount():
    return float(input("Ingresa la cantidad a invertir: "))

def preguntar_interest():
    return float(input("Ingresa el interés anual: "))

def preguntar_anios():
    return float(input("Ingresa el total de años: "))

def mostrar_capital_obtenido(amount, interest, anios)-> float:
    capital_obtenido = amount * (1 + interest /100) ** anios
    return capital_obtenido
    


def main():
    amount = preguntar_amount()
    interest = preguntar_interest()
    anios = preguntar_anios()
    capital = mostrar_capital_obtenido(amount, interest, anios)
    print(f"El capital obtenido tras esos años con esa inversion a ese interes asciende a: {capital}")

if __name__ == "__main__":
    main()