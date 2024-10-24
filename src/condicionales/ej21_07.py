# Ejercicio 2.1.7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta 	Tipo impositivo
# Menos de 10000€ 	5%
# Entre 10000€ y 20000€ 	15%
# Entre 20000€ y 35000€ 	20%
# Entre 35000€ y 60000€ 	30%
# Más de 60000€ 	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def preguntar_renta_anual():
    return float(input("¿Cuál es tu renta anual?\n"))

def mostrar_tipo_impositivo(cuantia: float)-> str:
    if cuantia < 10000:
        return "Tus impuestos son del 5%."
    elif 10000 <= cuantia <=20000:
        return "tus impuestos son del 15%."
    elif 20000 < cuantia <= 35000:
        return "Tus impuestos son del 20%."
    elif 35000 < cuantia <= 60000:
        return "Tus impuestos son del 30%."
    else:
        return "Tus impuestos son del 45%."


def main():
    cuantia = preguntar_renta_anual()
    tipo_impositivo = mostrar_tipo_impositivo(cuantia)
    print(tipo_impositivo)

if __name__ == "__main__":
    main()