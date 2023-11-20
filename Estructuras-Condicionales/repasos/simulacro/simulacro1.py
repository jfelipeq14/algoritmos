# La empresa “Salome lujos”lo contrata para hacer un algoritmo que imprima una factura completa. Tenga en cuenta que la factura tiene 3 productos con su código, nombre, precio y cantidad vendida. muestre la información que considere necesaria para el cliente. La factura tiene un descuento, estese basa en una balota (la factura tiene un solo descuento), si la balota es blanca es del 10%, si la balota es azul del 12%, si la balota es roja del 14%, si la balota es verde del 16%, si la balota es rosa es del 18%, si la balota es gris es del 20%, si la balota es amarilla tiene un descuento del 22%

#DE: codpr1, np1, prepr1, cantp1, codpr2, np2, prepr2, cantp2, codpr3, np3, prepr3, cantp3, colorBalota

#P:
#  valorTotalProducto1 = prepr1 * cantp1
#  valorTotalProducto2 = prepr2 * cantp2
#  valorTotalProducto3 = prepr3 * cantp3
#  valorFactura = valorTotalProducto1 + valorTotalProducto2 + valorTotalProducto3
#   si (colorBalota == 'blanca') => descuento = 0.10
#    sino
#     si (colorBalota == 'azul') => descuento = 0.12
#    sino
#     si (colorBalota == 'roja') => descuento = 0.14
#    sino
#     si (colorBalota == 'verde') => descuento = 0.16
#    sino
#     si (colorBalota == 'rosa') => descuento = 0.18
#    sino
#     si (colorBalota == 'gris') => descuento = 0.20
#    sino
#     si (colorBalota == 'amarilla') => descuento = 0.22
#   valorDescuento = valorFactura * descuento
#   valorPago = valorFactura - valorDescuento

#DS: valorPago

codpr1 = int(input("Digite el codigo del producto 1: "))
np1 = input("Digite el nombre del producto 1: ")
prepr1 = int(input("Digite el precio del producto 1: "))
cantp1 = int(input("Digite la cantidad del producto 1: "))
print("\n")
codpr2 = int(input("Digite el codigo del producto 2: "))
np2 = input("Digite el nombre del producto 2: ")
prepr2 = int(input("Digite el precio del producto 2: "))
cantp2 = int(input("Digite la cantidad del producto 2: "))
print("\n")
codpr3 = int(input("Digite el codigo del producto 3: "))
np3 = input("Digite el nombre del producto 3: ")
prepr3 = int(input("Digite el precio del producto 3: "))
cantp3 = int(input("Digite la cantidad del producto 3: "))
print("\n")

totalProducto1 = prepr1 * cantp1
totalProducto2 = prepr2 * cantp2
totalProducto3 = prepr3 * cantp3
subTotal = totalProducto1 + totalProducto2 + totalProducto3

print("Lista de balotas: ")
print("blanca: 10%")
print("azul: 12%")
print("roja: 14%")
print("verde: 16%")
print("rosa: 18%")
print("gris: 20%")
print("amarilla: 22%")
colorBalota=input("Digite el color de la balota para aplicar el descuento: ")

if colorBalota == 'blanca':
    descuento = subTotal * 0.10
elif colorBalota == 'azul':
    descuento = subTotal * 0.12
elif colorBalota == 'roja':
    descuento = subTotal * 0.14
elif colorBalota == 'verde':
    descuento = subTotal * 0.16
elif colorBalota == 'rosa':
    descuento = subTotal * 0.18
elif colorBalota == 'gris':
    descuento = subTotal * 0.20
elif colorBalota == 'amarilla':
    descuento = subTotal * 0.22

total = subTotal - descuento

print("Factura")
print("Codigo - Nombre - Cantidad - Precio - Total")
print(f'{codpr1} | {np1} | {cantp1} | {prepr1} | {totalProducto1}')
print(f'{codpr2} | {np2} | {cantp2} | {prepr2} | {totalProducto2}')
print(f'{codpr3} | {np3} | {cantp3} | {prepr3} | {totalProducto3}')
print("")
print(f"Subtotal: {subTotal}")
print(f"Descuento: {descuento}")
print(f"Total: {total}")
print("")
print("Gracias por su compra")