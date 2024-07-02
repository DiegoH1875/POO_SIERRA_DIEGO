# Programa de herencia
class Product:
    def __init__(self, nombre,precio, codigo_de_barras):
        try:
            self.nombre = str(nombre)
            self.precio = float(precio)
            self.codigo_de_barras = int(codigo_de_barras)
        except ValueError as e:
            raise ValueError(f"Error in datatype conversion {e} wrong data type")
    def mostrar_precio(self):
        print(f"El precio de {self.nombre} es ${self.precio}")

class Lacteos(Product):
    def __init__(self, nombre, marca, precio, codigo_de_barras):
        super().__init__(nombre, precio, codigo_de_barras)
        self.marca = str(marca)
        self.categoria = "Lacteos"

    def describir_producto(self):
        print(F"Nombre: {self.nombre}")
        print(F"Marca: {self.marca}")
        print(F"Categoria: {self.categoria}")
        print(F"Codigo de barras: {self.codigo_de_barras}")
        self.mostrar_precio()

def main():
    leche_lala = Lacteos("Leche Entera", "LALA", 40.50,426531819211)
    leche_lala.describir_producto()

if __name__=="__main__":
    main()

