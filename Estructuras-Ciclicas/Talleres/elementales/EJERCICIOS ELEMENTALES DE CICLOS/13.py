# 13.Elabore un algoritmo que lea 50 números y encuentre el menor de esos números
menor = 0
for i in range(3):
    numero = int(input(f"Digite el numero {i+1}: "))
    if i == 0:
        menor = numero
    elif i > 0 and numero < menor:
        menor = numero
print(f"El numero menor es {menor}")
