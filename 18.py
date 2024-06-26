# Programa que actualize valores de un diccionario
# Crear diccionario con productos y precios
market = {
    "Tomate": 9.00,
    "Pan": 56.45,
    "Aguacate":99.00,
    "Limon": 34.45,
    "Papa":12.65,
    "Pepino":24.08
}
DISCOUNT = 10
DISCOUNT_APLIED = ((100 - DISCOUNT) * 0.01)
# Print the dictionary items with its respective discount
for product in market:
    print(F"{product} -> ORIGINAL PRICE -> {market[product]}")
    market[product] *= DISCOUNT_APLIED # Apply discount
    print(F"{product} -> PRICE WITH {DISCOUNT}% OF DISCOUNT -> {market[product]:.1f}")
    for i in range(3):
        print("")
 