# Elabore un algoritmo que lea 5 números y muestre su suma
suma = 0
for numeros in range(1, 6):
    numero = int(input(f"Digite el numero {numeros}: "))
    suma = suma + numero
print(suma)