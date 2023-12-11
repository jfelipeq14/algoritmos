# Leer 10 números e imprimir solamente los números positivos

for n in range(1, 11):
    numero = float(input(f"Digite un numero: "))
    if numero >= 0:
        print(numero)