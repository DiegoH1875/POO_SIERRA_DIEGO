import os
from sys import exit

def clear_terminal():
    # A function to clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_terminal()
    print ("MENU PARA EXPLICACION DE CLASES: ")
    print("OPCIONES")
    print("[A] para abstraccion")
    print("[E] para encapsulamiento")
    print("[H] para herencia")
    print("[P] para polimorfismo")
    print("[S] para salir ")
    opciones = ["A","E", "H", "P", "S"]
    # Que el usuario seleccione una opcion valida
    opcion_elegida = ""
    while True:
        opcion_elegida = input("Selecciona una opcion valida: ").upper()
        if opcion_elegida in opciones:
            break
        continue
    # Explicacion de lo que el usario pidio
    match opcion_elegida:
        case 'A':
            # Abstraccion
            explicacion = """
            La abstracción en Programación Orientada a Objetos (POO) es el proceso de simplificar 
            un sistema complejo al enfocarse solo en los aspectos más relevantes y ocultar los detalles innecesarios. 
            En otras palabras, la abstracción permite representar conceptos esenciales de una manera general, 
            sin entrar en los pormenores de su implementación.
            Por ejemplo, cuando defines una clase "Coche" en POO, te enfocas en las características generales 
            como "modelo", "marca" y "velocidad", y en comportamientos como "acelerar" y "frenar". 
            No necesitas detallar cómo funciona internamente el motor para usar la clase "Coche". 
            La abstracción te permite trabajar con una representación simplificada del coche, ocultando la complejidad interna.
            """
        case 'E':
            # Encapsulamiento
            explicacion = """
            El encapsulamiento en Programación Orientada a Objetos (POO) es un principio que 
            consiste en agrupar los datos (atributos) y los métodos (funciones) que operan sobre esos datos 
            dentro de una misma clase, y restringir el acceso directo a algunos de estos elementos desde fuera 
            de la clase.
            Esto se logra utilizando modificadores de acceso como privado o protegido, lo que permite contro-
            lar cómo y quién puede interactuar con los datos. El encapsulamiento ayuda a proteger la integridad 
            del objeto al evitar que otros objetos interfieran directamente con su estado interno. 
            En lugar de acceder a los datos directamente, se utilizan métodos específicos (getters y setters) 
            para obtener o modificar los valores de manera controlada."""
        case 'H':
            # Herencia
            explicacion = """
            La herencia en Programación Orientada a Objetos (POO) es un mecanismo que permite 
            crear nuevas clases basadas en clases existentes, heredando atributos y métodos de la clase base o 
            "superclase". La nueva clase, llamada "subclase" o "clase derivada", puede reutilizar el código de 
            la superclase, además de agregar sus propios atributos y métodos o modificar el comportamiento heredado.
            La herencia facilita la reutilización de código y la creación de estructuras jerárquicas. 
            Por ejemplo, si tienes una clase Animal con atributos como nombre y edad, y métodos como comer y 
            dormir, puedes crear una subclase Perro que herede de Animal, añadiendo atributos específicos como 
            raza y métodos como ladrar. 
            La subclase Perro heredará todo lo que tiene Animal, pero también puede tener sus propias característi-
            cas distintivas.
            """
        case 'P':
            # Polimorfismo
            explicacion = """
            El polimorfismo en Programación Orientada a Objetos (POO) es la capacidad de que 
            diferentes clases puedan ser tratadas como si fueran de una misma superclase, pero cada una puede 
            comportarse de manera distinta. Es decir, el polimorfismo permite que un mismo método tenga dife-
            rentes implementaciones según la clase en la que se utilice.
            Existen dos tipos principales de polimorfismo:
            Polimorfismo de Sobrecarga: Ocurre cuando varios métodos en la misma clase tienen el mismo nombre 
            pero diferentes parámetros (por ejemplo, diferentes tipos o cantidad de argumentos).
            Polimorfismo de Sobrescritura: Se da cuando una subclase redefine un método heredado de su super-
            clase para cambiar o extender su comportamiento.
            """
        case 'S':
            exit("Vuelve si tienes mas dudas")

    print(explicacion)
    regresar = ""
    while True:
        print("Pulsa [R] cuando quieras volver al menu")
        regresar = input("").upper()
        if regresar == "R":
            return
        
def main():
    while True:
        menu() # El break se realiza en la funcion mediante sys.exit

if __name__=="__main__":
    main()