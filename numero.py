def main():
    numero = get_float("Dame un numero: ")
    # Checar las condiciones del numero
    if numero > 0:
        print(F"Numero {numero} es POSITIVO")
    elif numero < 0:
        print(F"Numero {numero} es NEGATIVO")
    else:
        print(f"Numero {numero} es igual a 0")

def get_float(prompt):
    # Funcion para pedirle un numero FLOTANTE al usuario
    while True:
        try:
            float_number = float(input(prompt))
            break
        except ValueError:
            continue
    return float_number

main()

