# Ejercicio 2.1.10
# 
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# 
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

tipo_pizza = ("vegetariana", "no vegetariana")
ingredientes_vegetarianos = ("pimiento", "tofu")
ingredientes_no_vegetarianos = ("peperoni", "jamon", "salmon")
ingredientes_basicos = ("mozzarella", "tomate")


def preguntar():
        respuesta = input("Marque 1 si quiere pizza vegetariana, o 2 si es el caso contrario:\n")
        if respuesta == 1:
            return "Vegetariana"
        elif respuesta == 2:
            return "No vegetariana"
        else:
            return "Error, elija entre el 1 y el 2"
    
def menu(tipo):
    pizza = [ingredientes_basicos]

    print(f"Solo puedes escoger un ingrediente extra aparte de los ingredientes por defecto: {",".join(ingredientes_basicos)}")

    if tipo == "vegetariana":
        print(f"Los ingrediantes que tenemos para este tipo de pizza son: {", ".join(ingredientes_vegetarianos)}.")
        ingrediente = input("Elige pimiento o tofu.").lower()
        if ingrediente == "pimiento":
            pizza.append(ingredientes_vegetarianos[0])
        elif ingrediente == "tofu":
            pizza.append(ingredientes_vegetarianos[1])
        else:
            print("Ese ingrediente no es posible ponerlo en la pizza.")

    elif tipo == "no vegetariana":
        print(f"Los ingrediantes que tenemos para este tipo de pizza son: {", ".join(ingredientes_no_vegetarianos)}.")
        ingrediente = input("Elige peperoni, jamon o salmon.").lower()
        if ingrediente == "peperoni":
            pizza.append(ingredientes_vegetarianos[0])
        elif ingrediente == "jamon":
            pizza.append(ingredientes_vegetarianos[1])
        elif ingrediente == "salmon":
            pizza.append(ingredientes_vegetarianos[2])
        else:
            print("Ese ingrediente no es pòsible ponerlo en la pizza.")
    return pizza


def mostrar_info(tipo, ingredientes):
    print(f"Tu pizza es {tipo} y contiene {ingredientes}")



def main():
    tipo = preguntar()
    ingredientes = menu(tipo)
    mostrar_info(tipo, ingredientes)
    


if __name__ == "__main__":
    main()