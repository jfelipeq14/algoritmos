# 10) Calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se compran 5 o más.

# DE:
# cantidadLlantas
# P:
# si (cantidadLlantas < 5) precioLlanta = 800
# sino
#  si (cantidadLlantas >= 5) precioLlanta = 700
# DS:
# total

cantidadLlantas = int(input("Digite la cantidad de llantas: "))

if cantidadLlantas < 5:
    precioLlanta = 800
elif cantidadLlantas >= 5:
    precioLlanta = 700

print(f'{cantidadLlantas * precioLlanta}')
