# Elabore un algoritmo que lea 10 números y muestre su suma y su promedio

suma = 0
for numeros in range(1, 11):
    numero = int(input(f"Digite el numero {numeros}: "))
    suma = suma + numero
promedio = suma / 10
print(f"la suma es: {suma}")
print(f"la promedio es: {promedio}")