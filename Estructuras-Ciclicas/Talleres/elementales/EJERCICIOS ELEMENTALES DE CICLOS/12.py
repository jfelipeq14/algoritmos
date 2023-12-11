# 12.Elabore un algoritmo que lea 10 números y muestre su suma y su promedio

suma = 0
for i in range(10):
    numero = int(input(f"Digite el numero {i+1}"))
    suma += numero
promedio = suma / 10
print(f"La suma es {suma}")
print(f"El promedio es es {promedio}")
