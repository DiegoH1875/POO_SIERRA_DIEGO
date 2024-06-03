def main():
    edades = [23, 66,34, 35, 67, 25, 12, 8,45, 9, 14, 16, 18, 14, 16, 17, 18, 19, 76, 90, 91, 88, 81]
    infancia = []
    adolescencia = []
    jovenes = []
    adultos = []
    
    # Separa las categorias
    # Imprime lista de edades originales
    print("LISTA DE EDADES ORIGINAL")
    for edad in edades:
        if 11 >= edad >= 6:
            infancia.append(edad)
        elif 17 >= edad >= 12:
            adolescencia.append(edad)
        elif 26 >= edad >= 18:
            jovenes.append(edad)
        else:
            adultos.append(edad)
        print (f"{edad}," ,end="")
    print()
    

    # Imprime las edades segun la categoria
    print("EDADES SEPARADAS EN CATEGORIAS")
    print()
    # INFANTES
    print("INFANCIA")
    for edad in infancia:
        print (f"{edad}," ,end="")

    print()
    
    # ADOLESCENTES
    print("ADOLESCENCIA")
    for edad in adolescencia:
        print (f"{edad}," ,end="")
    print()
    
    # JOVENES
    print("JOVENES")
    for edad in jovenes:
        print (f"{edad}," ,end="")
    print()
    
    #Adultos
    print("ADULTOS")
    for edad in adultos:
        print (f"{edad}," ,end="")
    print()

main()
