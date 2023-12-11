# 11.Elabore un algoritmo que lea 12 números y muestre su suma

suma = 0
for i in range(12):
    numero = int(input(f"Digite el numero {i+1}"))
    suma += numero
print(f"La suma de los numeros es {suma}")
