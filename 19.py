# Crea un programa con 2 conjuntos con nombres de frutas
def main():
    frutas_tropicales = {"Mango", "Uva", "Fresa", "Sandia", "Platano"}
    frutas_invernales = {"Manzana","Naranja", "Mandarina", "Toronja"}
    frutas = frutas_tropicales | frutas_tropicales
    frutas.add("Melon")
    for fruta in frutas:
        print(fruta)

main()