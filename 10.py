def main():
    while True:
        try:
            print("Ingresa dos numeros O ingresa ""N"" para detenerte")
            x = get_number("X: ")
            y = get_number("Y: ")
            print(f"{x} + {y} = {x + y}")
        except EOFError:
            break 

def get_number(prompt):
    while True:
        try:
            new_number = input(prompt)
            if new_number.upper() == "N":
                raise EOFError
            new_number = float(new_number)
            break
        except ValueError:
            continue
    return new_number

main()