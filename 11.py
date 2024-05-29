# Programa que convierta "Hola mundo" a mayusculas usando un for
def main():
    cadena = "Hola Mundo"
    print(cadena)
    for i in range(len(cadena)):
        print(cadena[i].upper())
    
main()