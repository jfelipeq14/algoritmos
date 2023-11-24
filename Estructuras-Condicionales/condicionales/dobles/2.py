#  Pedir al usuario un número. Si el número es par, imprimir "El número es par". Si no, imprimir "El número es impar".

#  entradas => Numero
#  proceso => Validar si es par o impar (modulo de 2)
# salida => mensaje de par o impar

numero = int(input("Digite el numero"))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
