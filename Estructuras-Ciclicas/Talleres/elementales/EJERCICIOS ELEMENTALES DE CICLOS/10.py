# 10.Elabore un algoritmo que lea 10 números y muestre su suma

suma = 0
for i in range(10):
    numero = int(input(f"Digite el numero {i+1}"))
    suma += numero
print(f"La suma de los numeros es {suma}")
