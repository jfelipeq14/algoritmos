# Elabore un algoritmo que lea 50 números y encuentre el menor de esos números

menor = 9999999999
for n in range(1, 51):
    numero = float(input("Digite un numero: "))
    if numero < menor:
        menor = numero
print(f"El numero menor es: {menor}")