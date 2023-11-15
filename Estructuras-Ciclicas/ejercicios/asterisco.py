# elabore un algoritmo hasta que el usuario ingrese un asterisco
i = ""
suma = 0
while i != "*":
    numero = input("Digite el numero")
    if numero != "*":
        numero = int(numero)
        suma += numero
    i = numero
print(suma)
