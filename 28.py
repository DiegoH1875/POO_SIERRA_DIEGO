# Programa de Dependecia
from typing import Any


class Producto:
    def __init__(self, nombre,precio, codigo_de_barras):
        try:
            self.nombre = str(nombre)
            self.precio = float(precio)
            self.codigo_de_barras = int(codigo_de_barras)
        except ValueError as e:
            raise ValueError(f"Error in datatype conversion {e} wrong data type")
    def mostrar_precio(self):
        print(f"El precio de {self.nombre} es ${self.precio}")

class Lacteos(Producto):
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

class Cliente:
    def __init__(self, nombre, numero_membresia):
        self.nombre = nombre
        try:
            self.numero_membresia = int(numero_membresia)
        except ValueError:
            raise ValueError (F"Error en conversion de dato {numero_membresia} debe ser clase int")
    def comprar(self, producto):
        if isinstance(producto, Producto):
            producto.mostrar_precio()
        else:
            print("Ese producto no existe en la tienda")
        
def main():
    leche_lala = Lacteos("Leche Entera", "LALA", 40.50,426531819211)
    cliente_Aaron = Cliente("Aaron Sierra", 45137)
    cliente_Aaron.comprar(leche_lala)

if __name__=="__main__":
    main()
    