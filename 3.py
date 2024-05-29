def main():
    peso = get_peso()
    altura = get_altura()
    imc = peso / (altura**2)
    print(f"IMC: {imc:.2f}")

def get_peso():
    while True:
        try:
            peso = float(input("Peso (KILOGRAMOS): "))
            if peso <= 0.0 or peso > 500:
                raise ValueError
            break
        except ValueError:
            continue
    return peso
def get_altura():
    while True:
        try:
            altura = float(input("Altura (EN METROS): "))
            if altura <= 0 or altura > 3.00:
                raise ValueError
            break
        except ValueError:
            continue
    return altura

main()

