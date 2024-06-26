def main():
    primeros_numeros = {536, 162,829,718,91,937, 273,672,44,65, 38,28}
    segundos_numeros = {526, 627, 976, 46, 9, 53, 167, 67}
    terceros_numeros = {356, 89, 72, 56, 35, 87, 98, 67, 35, 76, 56, 6}
    numeros_completos = primeros_numeros | segundos_numeros | terceros_numeros
    numeros_pares = {None,None}
    print("NUMEROS PARES")
    for numero in numeros_completos:
        if numero % 2 == 0: # Si el numero es par
            numeros_pares.add(numero)
            print(numero)

main()