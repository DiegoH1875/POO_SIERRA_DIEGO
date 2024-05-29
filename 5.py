def main():
    print("ANTRO | SISTEMA DE VERIFICACION DE EDAD")
    edad = get_int("Dame tu edad: ")
    if edad >= 18:
        print("MAYOR DE EDAD, PUEDES PASAR")
    else:
        print("MENOR DE EDAD, NO PUEDES PASAR")

def get_int(prompt):
    while True:
        try:
            integer = int(input(prompt))
            break
        except ValueError:
            continue
    return integer

main()