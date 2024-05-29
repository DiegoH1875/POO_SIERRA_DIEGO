# El costo del envio basado en el peso de un paquete ingresado 
def main():
    # Definir las constantes necesarias
    # Rango de kilogramos y sus precios
    MENOS_A_UNO = 50
    UNO_A_CINCO = 100
    CINCO_A_DIEZ = 200
    DIEZ_O_MAS = 500
    # Pedir al usuario el peso de su paquete
    peso_paquete = get_float("Dame el peso del paquete a enviar: ")
    #Calcula el costo del envio
    if peso_paquete < 1.0:
        tarifa = MENOS_A_UNO
    elif peso_paquete < 5.0:
        tarifa = UNO_A_CINCO
    elif peso_paquete < 10.0:
        tarifa = CINCO_A_DIEZ
    else:
        tarifa = DIEZ_O_MAS
    # Imprime el resultado final al usuario
    print(f"Las tarifa de envio del paquete es igual a ${tarifa:.1f}")

def get_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            break
        except ValueError:
            continue
    return new_float

main() # Call the main function