def main():
    a = get_float("A: ")
    b = get_float("B: ")
    c = get_float("C: ")
    x1 = float((((-b) + (((b ** 2) - (4 * (a * c)))** 0.5)) / (2 * a)))
    x2 = float((((-b) - (((b ** 2) - (4 * (a * c)))** 0.5)) / (2 * a)))
    print(f"X1: {x1}")
    print(f"X2: {x2}")

def get_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            break
        except ValueError:
            continue
    return new_float

main()