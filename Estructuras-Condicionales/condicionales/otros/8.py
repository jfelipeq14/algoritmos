# 8) Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%

# DE: cantidad, valorCamisa
# P: Si (cantidad >= 3) => descuento = 0.20
#    Sino
#     Si (cantidad < 3) => descuento = 0.10
# total = valorCamisa * cantidad
# descuento = total * descuento
# totalPago = total - descuento
# DS: totalPago

cantidad = int(input("ingrese cantidad de camisas: "))
valorCamisa = int(input("ingrese valor de camisa: "))

if cantidad >= 3:
    descuento = 0.20
elif cantidad < 3:
    descuento = 0.10

total = valorCamisa * cantidad
descuento = total * descuento
totalPago = total - descuento

print(totalPago)
