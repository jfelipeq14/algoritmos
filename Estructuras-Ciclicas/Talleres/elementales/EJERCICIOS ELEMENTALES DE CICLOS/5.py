# 5. Elabore un algoritmo que sume 5 números
numeros = 0
for i in range(5):
    numero = int(input(f"Digite el numero {i+1}"))
    numeros += numero
print(f"La suma de los numeros es {numeros}")
