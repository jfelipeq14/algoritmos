# Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.

positivos=0
negativos=0
neutros=0
for n in range(1, 21):
    numero = float(input(f"Digite un numero: "))

    if numero * 1 == numero:
        neutros+=1

    if numero > 0:
        positivos+=1
    elif numero < 0:
        negativos+=1

print(f"Numeros positivos {positivos}")
print(f"Numeros negativos {negativos}")
print(f"Numeros neutros {neutros}")