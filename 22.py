# Programa calculadora
def main():
    # Get the operation from the user
    a, type_operation, b = get_operation()
    result = 0.0
    match type_operation:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            result = a / b
        case _:
            raise ValueError(f"Invalid type operation '{type_operation}'")
    print(f"{a} {type_operation} {b} = {result}")

def get_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            break
        except ValueError:
            continue
    return new_float

def get_operation():
    while True:
        try:
            operation = input("Introduce your mathematical operation: ")
            first_number, kind_operation, second_number = split_operation(operation)
            first_number = float(first_number)
            second_number = float(second_number)
            break
        except ValueError:
            continue
    return first_number, kind_operation, second_number

def split_operation(operation):
    type_operations = ['+', '-', '*', '/']
    splited = False
    for i in range(4):
        try:
            x , y = operation.split(type_operations[i])
            operation_type = type_operations[i]
            splited = True
            break
        except ValueError:
            continue
    if splited:
        return x, operation_type, y
    else:
        raise ValueError

if __name__=="__main__":
    main()

