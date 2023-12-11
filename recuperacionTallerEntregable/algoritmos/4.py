# Elabore un algoritmo que lea 12 números y muestre su suma

suma = 0
for numeros in range(1, 13):
    numero = int(input(f"Digite el numero {numeros}: "))
    suma = suma + numero
print(suma)