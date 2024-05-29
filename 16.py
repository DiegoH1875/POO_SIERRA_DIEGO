# Pide al usuario que busque n promedios y que el sistema encuentre el mayor de todos ellos
def main():
    N = 3
    promedios = []
    mayor = 0
    for i in range(N):
        nuevo_promedio = get_float("Introduce un promedio: ")
        promedios.append(nuevo_promedio)
        if mayor < nuevo_promedio:
            mayor = nuevo_promedio
    # Imprimir el numero mayor
    print(f"El promedio mas alto de los {N} promedios ingresados es: {mayor}")
        
def get_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            break
        except ValueError:
            continue
    return new_float

main()