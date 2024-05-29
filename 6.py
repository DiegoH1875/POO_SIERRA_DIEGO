#  Determinar entre dos numeros cual es el mayor o si son iguales
def main():
    #Pedir al usuario dos numeros
    x = get_float("X: ")
    y = get_float("Y: ")
    # Checar cual numero es mayor o si son iguales
    if x > y:
        print(f"X ({x}) es mayor que Y ({y})")
    elif y > x:
        print(f"Y({y}) es mayor que X({x})")
    else:
        print(f"X({x}) y Y({y}) son iguales")

def get_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            break
        except ValueError:
            continue
    return new_float

# Call the main function
main()
