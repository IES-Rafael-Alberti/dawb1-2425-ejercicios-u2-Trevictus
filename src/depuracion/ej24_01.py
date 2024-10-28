# Ejercicio 2.4.1
# Algoritmo burbuja

def burbuja(lista): 
    n = len(lista) #Longitud de la lista
    for i in range(n): #Se recorre cada elemento de la lista n
        for j in range(0, n-i-1): #A cada elemento se le asigna una posicion en la variable j
            if lista[j] > lista[j+1]: #Si el valor de la posicion es mas alto que su siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]#Se invierte el orden de los dos elementos comparados
    return lista                                           #Se vuelve a comenzar el recorrido de los elementos por por la lista n

def main():
    n = [45, 12, 76, 11, 1, 234, 32, 33, 34, 6]
    print(burbuja(n))

if __name__ == "__main__":
    main()