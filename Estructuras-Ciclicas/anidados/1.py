#1. La empresa “Salome lujos” lo contrata para hacer un algoritmo que imprima el total de facturación de un día. Sabiendo que cada día se hacen 3 facturas y cada  factura tiene 2 artículos, la factura debe tener el nombre del artículo, precio y su cantidad. El descuento se basa en una balota (la factura tiene un solo descuento), si la balota es blanca es del 10%, si la balota es azul del 12%, si la balota es roja del 14%, si la balota es verde del 16%, si la balota es rosa es del 18%.

valorFactura1 = 0
valorFactura2 = 0
valorFactura3 = 0

for factura in range(1,4):
    balota=input("Digite el color de la balota (blanca, azul, roja, verde, rosa):").lower()
    
    if balota == "blanca":
        porcentajeDescuento = 0.10
    elif balota == "azul":
        porcentajeDescuento = 0.12
    elif balota == "roja":
        porcentajeDescuento = 0.14
    elif balota == "verde":
        porcentajeDescuento = 0.16
    elif balota == "rosa":
        porcentajeDescuento = 0.18

    for producto in range(1, 3):
        nombreArticulo=input(f"Digite el nombre del articulo {producto}: ")
        precioArticulo=int(input(f"Digite el precio de {nombreArticulo}: "))
        cantidadArticulo=int(input(f"Digite la cantidad de {nombreArticulo}: "))
        totalArticulo = precioArticulo*cantidadArticulo

    if factura == 1:
        valorFactura1+=totalArticulo
    elif factura == 2:
        valorFactura2 += totalArticulo
    elif factura == 3:
        valorFactura3 += totalArticulo
    
descuentoFactura1 = valorFactura1*porcentajeDescuento
netoFactura1 = valorFactura1-descuentoFactura1

descuentoFactura2 = valorFactura2*porcentajeDescuento
netoFactura2 = valorFactura2-descuentoFactura2

descuentoFactura3 = valorFactura3*porcentajeDescuento
netoFactura3 = valorFactura3-descuentoFactura3

totalDia = netoFactura1 + netoFactura2 + netoFactura2

print(f"Valor de la factura 1: {valorFactura1}")
print(f"Descuento de la factura 1: {descuentoFactura1}")
print(f"Neto de la factura 1: {netoFactura1}")

print(f"Valor de la factura 2: {valorFactura2}")
print(f"Descuento de la factura 2: {descuentoFactura2}")
print(f"Neto de la factura 2: {netoFactura2}")

print(f"Valor de la factura 3: {valorFactura3}")
print(f"Descuento de la factura 3: {descuentoFactura3}")
print(f"Neto de la factura 3: {netoFactura3}")

print(f"Total del dia: {totalDia}")