# Ejercicio 2.1.8
# 
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel 	Puntuación
# Inaceptable 	0.0
# Aceptable 	0.4
# Meritorio 	0.6 o más
# 
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

NIVELES = "inaceptable", "aceptable", "meritorio"
puntuacion = 0.0, 0.4, 0.6

def leer_puntuacion():
    try:
        puntuacion = float(input("¿Cuál es tu puntuación?\n"))
    except ValueError:
        print("ERROR. Introduce un nº.")
    return puntuacion

def cuantia(puntuacion: float)-> str:
    beneficio = puntuacion * 2400
    maximo_ben = 0.6 * 2400
    if 0.0 < puntuacion < 0.4:
        return f"con la puntuacion de {puntuacion} y un rendimiento {NIVELES[0]} obtienes de beneficio {beneficio}"
    elif 0.4 <= puntuacion < 0.6:
        return f"con la puntuacion de {puntuacion} y un rendimiento {NIVELES[1]} obtienes de beneficio {beneficio}"
    elif puntuacion == 0.6:
        return f"con la puntuacion de {puntuacion} y un rendimiento {NIVELES[2]} obtienes de beneficio {beneficio}"
    elif puntuacion >= 0.6:
        return f"con la puntuacion de {puntuacion} y un rendimiento {NIVELES[2]} obtienes de beneficio {maximo_ben}"
    else:
        return "ERROR. Puntuación inválida."


def main():
    puntuacion = leer_puntuacion()
    beneficio = cuantia(puntuacion)
    print(beneficio)

if __name__ == "__main__":
    main()