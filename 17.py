# Conversion de Celsius a Farenheit y viceversa

def main():
    tipo_conversion()

def tipo_conversion():
    while True:
        print("Que tipo de conversion deseas: ")
        print("[F] para Farenheit a Celsius")
        print("[C] para Celsius a Farenheit")
        print("[E] para salir del programa")
        opcion_usuario = get_valid_option(["F", "C", "E"], "Elige entre una de las tres opciones: ")
        match opcion_usuario:
            case "F":
                farenheit_celsius()
            case "C":
                celsius_farenheit()
            case "E":
                return

def get_valid_option(options, prompt):
    while True:
        user_option = input(prompt).upper()
        if user_option not in options:
            print("Opcion Invalida, intenta de nuevo")
            continue
        else:
            break
    return user_option

def farenheit_celsius():
    farenheit = get_float("Grados Farenheit: ")
    celsius = (farenheit - 32) * 0.555
    print(f"Equivalente en grados celsius: {celsius:.2f}")

def celsius_farenheit():
    celsius = get_float("Grados Celsius: ")
    farenheit = (celsius * 1.8) + 32
    print(f"Equivalente en grados farenheit: {farenheit:.2f}")

def get_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            break
        except ValueError:
            continue
    return new_float

main()