#Operacion suma con los elementos de una lista
def main():
    numeros = [67, 879,4356, 2394,4, 5673, 5748, 1345, 34, 279, 22]
    # Suma los numeros
    suma = 0
    for numero in numeros:
        suma += numero
    # Imprime suma
    print(f"La suma total de los elementos es igual a: {suma}")

main()
