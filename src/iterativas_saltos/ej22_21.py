# Ejercicio 2.2.21
# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def pedir_monto():
    list_monto = []
    finalizar = False
    while not finalizar:
        try:
            monto = float(input("Ingresa monto: "))
            if monto < 0:
                raise ValueError("Nºs negativos no cuentan para el monto.")
            if monto == 0:
                suma = sum(list_monto)
                if suma > 1000:
                    descuento = (suma * 10) / 100
                    return f"Tienes un descuento de 10% haciendo un total de: {suma - descuento}"
                else:
                    return f"El total asciende a: {suma}"
            elif monto > 0:
                list_monto.append(monto)
            else:
                return "Nº no válido."
        except ValueError as e:
            print(f"ERROR {e} intenta de nuevo.")
        except Exception as e:
            print(f"debes ingrsar nºs válidos: {e}")

def main():
    print(pedir_monto())

if __name__ == "__main__":
    main()