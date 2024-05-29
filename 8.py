# Programa que escribe los numeros pares de N a Y utilizando un bucle While
def main():
    n = 2
    y = 20
    while n <= y:
        if n % 2 == 0:
            print(f"Numero par: {n}")
        n += 1

main()