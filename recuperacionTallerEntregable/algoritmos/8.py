# Leer 10 números y obtener su cubo y su cuarta.

for n in range(1, 11):
    numero = float(input(f"Digite el numero {n}: "))
    cubo = numero**3
    print(f"El cubo de {numero} es {cubo}")
    cuarta = numero / 4
    print(f"El cuarta de {numero} es {cuarta}")