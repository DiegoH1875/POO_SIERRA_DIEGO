def main():
    MAYORIA_EDAD = 18
    edades = [34, 16, 68, 23, 12, 11, 17, 57, 24, 13, 19, 18, 18, 15, 24, 27]
    mayores_de_edad = []
    menores_de_edad = []
    for edad in edades:
        if edad >= MAYORIA_EDAD:
            mayores_de_edad.append(edad)
        else:
            menores_de_edad.append(edad)
    
    #Imprime las listas con las edades menores de edad
    print("MENORES DE EDAD")
    i = 1
    for edad in menores_de_edad:
        print(f"{i} -> {edad}")
        i += 1
    print()
    # Imprime la lista con los mayores de edad
    print("MAYORES DE EDAD")
    i = 1
    for edad in mayores_de_edad:
        print(f"{i} -> {edad}")
        i += 1

main()